import json
import re
import requests
from tqdm import tqdm
from parsel import Selector
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def get_article_url(newsurl: str):
    url = newsurl
    headers = {
    'pragma': 'no-cache',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.dongchedi.com',
    'referer': 'https://www.dongchedi.com/news',
}
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 查找标题标签
    a_tags = soup.find_all('a')
    article_list = []
    for a in a_tags:
        href = a.get('href')
        if isinstance(href, str) and href.startswith("/article"):
            article_list.append(href)
    article_set = set(article_list)
    article_list = list(article_set)
    return article_list


def get_articlelist_by_url(articleurl: str):
    url = articleurl
    # 创建一个参数对象，用来控制chrome以无界面模式打开
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    #构建对象
    driver = webdriver.Chrome()
    #打开浏览器链接
    driver.get(url)
    #获取元素所在位置（xpath方式）
    contents = driver.find_elements(By.XPATH,'//*[@id="article"]/p')
    content_list = [x.text for x in contents if x.text.strip()]
    return content_list



if __name__ == '__main__':
    # #搜索汽车名称url
    # all_article_list = []
    # for i in range(2,800):
    #     url = f"https://www.dongchedi.com/news/newcar/{i}"
    #     article_list = get_article_url(url)
    #     all_article_list.extend(article_list)
    #     print(f'{i+1} / 800,数有{len(article_list)}', end='\r')
    # all_article_set = set(all_article_list)
    # article_urls_path = "C:\\Users\\IDEA\\Desktop\\all_article_urls_list.json"
    # with open(article_urls_path, 'r', encoding='utf-8') as f:
    #     all_article_urls_list = json.load(f)
    # all_article_urls_set = set(all_article_urls_list)
    # difference = all_article_set - all_article_urls_set
    # all_article_list = list(difference)
    
    # json_file_path = "C:\\Users\\IDEA\\Desktop\\all_article_urls_list1.json"
    # with open(json_file_path, 'w', encoding='utf-8') as f:
    #     json.dump(all_article_list, f, ensure_ascii=False, indent=4)
    # print(len(all_article_list))

    article_urls_path = "C:\\Users\\IDEA\\Desktop\\all_article_urls_list1.json"
    with open(article_urls_path, 'r', encoding='utf-8') as f:
        all_article_urls_list = json.load(f)
    #print(all_article_urls_list)
    all_content_list = []
    for url in tqdm(all_article_urls_list):
        content_list = get_articlelist_by_url(f'https://www.dongchedi.com{url}')
        all_content_list.append(content_list)
        json_file_path = "C:\\Users\\IDEA\\Desktop\\dongchedidata1.json"
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(all_content_list, f, ensure_ascii=False, indent=4)


