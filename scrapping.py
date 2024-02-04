import sys
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_latest_python_articles():
    url="https://www.python.org/"
    response=requests.get(url)

    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        latest_articles=[]

        for article in soup.select(".blog-widget li"):
            title=article.a.text.strip()
            latest_articles.append(title)

        return latest_articles
    else:
        print(f"fail to retrieve information.status code:{response.status_code}")
        return[]

if __name__=="__main__":
    python_articles=get_latest_python_articles()

    if python_articles:
        art=[]
        print("New News in python .org section")
        for index,article in enumerate(python_articles,1):
            art.append(article)
            print(f"{index},{article}")
          
        new_article=open('new_article.txt','w',encoding='utf-8')   
        new_article.write(' '.join(art))
        new_article.close()        
    else:
        print("No article found") 
               
