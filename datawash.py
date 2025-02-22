import os
import re
import json

import requests

def clearDataFromStructData(raw_data_path:str, output_file:str):
    files = os.listdir(raw_data_path)
    texts = []
    for file in files:
        file_path = os.path.join(raw_data_path, file)
        with open(file_path, mode='r',encoding='utf-8') as f:
            text = f.read()
            text = text.replace('\n',' ').replace('\r',' ')
            text = re.sub(r"\s+", " ", text)
            text.strip()
            text += '\n'
            texts.append(text)
    with open(output_file, mode='w', encoding='utf-8') as f:
        f.writelines(texts)

def clearDataFromTwitter(output_file):
    posts = []
    with open('./Data/Raw/Twitter/posts.txt', mode='r',encoding='utf-8') as f:
        for line in f:
            if len(line)>100:
                posts.append(line)
    with open(output_file, mode='w', encoding='utf-8') as f:
        f.writelines(posts)
   
def postLLM(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'prompt': prompt,
        "model": "llama3.2",
        "stream": False
    })
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            res = response.json()
            try:
                res_ = json.loads(res['response'])
                if isinstance(res_, dict) and 'prompt' in res_:
                    res_ = res_['prompt']
                return res_
            except Exception as e:
                print(str(e))
                print(res['response'])
                return res['response']
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(e)


def getPrompt(data_path:str, output_file:str):
    res = []
    prompt = """### Instruction ###
    I want to to finetune a LLM. Please use the follwing content as raw data to generate an input json file. Generate the prompt and use the content as response. Make the prompt more general and brief. Only output the prompt.
    
    ### Example ###
    {"prompt":"Describe the significance of the Battle of Iwo Jima during World War II and its lasting impact on American history and culture."}
    
    text:%s"""
    with open(data_path, mode='r', encoding='utf-8') as f:
        for i,line in enumerate(f):
            print(i)
            if len(line)>100:
                prompt_line = prompt % line
                gen_prompt = postLLM(prompt_line)
                if gen_prompt and len(gen_prompt)<400:
                    res.append({"prompt":gen_prompt, "response":line})
    with open(output_file, mode='w', encoding='utf-8') as f:
        json.dump(res, f, indent=1)
 
if __name__ =="__main__":
    # clearDataFromStructData('./Data/Raw/Speech/archive', './Data/ClearData/speech.txt')
    # clearDataFromStructData('./Data/Raw/Website', './Data/ClearData/news.txt')
    # clearDataFromTwitter('./Data/ClearData/posts.txt')
    # getPrompt('./Data/ClearData/news.txt', './Data/Prompt/news.json')
    getPrompt('./Data/ClearData/speech.txt', './Data/Prompt/speech.json')
    # getPrompt('./Data/ClearData/posts.txt', './Data/Prompt/posts.json')

