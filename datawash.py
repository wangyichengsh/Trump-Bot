import os
import re

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
   

def getPrompt():
    pass    
   
if __name__ =="__main__":
    clearDataFromStructData('./Data/Raw/Speech/archive', './Data/ClearData/speech.txt')
    clearDataFromStructData('./Data/Raw/Website', './Data/ClearData/news.txt')
    clearDataFromTwitter('./Data/ClearData/posts.txt')