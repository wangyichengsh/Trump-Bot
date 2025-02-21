import time
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup


def getTrumpTruthPost(n=30000)->Set[str]:
    driver = webdriver.Chrome()

    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless") 

    url = "https://truthsocial.com/@realDonaldTrump"
    # Open the page
    driver.get(url)
    time.sleep(5) 

    post_set = set()

    for _ in range(n):  # Adjust number of scrolls as needed
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.05);")
        try:
            posts = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME  , "p"))  # Adjust selector if needed
            )                
            post_texts = [post.text for post in posts]
            for post in post_texts:
                if len(post)>10:
                    print(post)
                    post_set.add(post)
        except Exception as e:
            print(f"Error fetching posts: {e}")
        sleep_time = random.uniform(5, 6)
        time.sleep(sleep_time)  

    driver.quit()
    return post_set

def getWhiteHouseNews(dir_path:str):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    news_map = {}
    for i in range(23):
        url = "https://www.whitehouse.gov/news/page/%s/" % (i+1)
        if i == 0:
            url = "https://www.whitehouse.gov/news/"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                # Find all news articles
                articles = soup.select("h2 a")
                # Store news data
                for article in articles:
                    news_map[article.text] = article["href"]
            time.sleep(random.uniform(1, 2))
        except Exception as e:
            print(f"Error fetching posts: {e}")
    for key in news_map:
        try:
            url = news_map[key]
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                # Find all news articles
                articles = soup.select("p")
                # Store news data
                texts = []
                for article in articles:
                    texts.append(article.text)
                title = key.replace('/','_')
                title = title.replace('\\','_')
                file_path = os.path.join(dir_path, title+'.txt')
                with open(file_path, mode='w',encoding="utf-8") as f:
                    f.write('\n'.join(texts))
                time.sleep(random.uniform(1, 2))
        except Exception as e:
            print(f"Error fetching posts: {e}")
    

if __name__=="__main__":
    post_set = getTrumpTruthPost()
    with open('./Data/Twitter',mode='w',encoding='utf-8') as f:
        for post in post_set:
            post_list = post.split('\n')
            line = ''.join(post_list)+'\n'
            f.write(line)
            
    getWhiteHouseNews('./Data/Website')



