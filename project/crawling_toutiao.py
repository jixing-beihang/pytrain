# -*- coding:utf-8 -*-
import json
import os
import re
from hashlib import md5
from json import JSONDecodeError
from multiprocessing import Pool
from urllib.parse import urlencode

import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from project.config import *

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        ' count': ' 20',
        'cur_tab': '3'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException as e:
        print(e)
        return None


def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException as e:
        print(e)
        return None


def parse_page_datail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].text
    images_pattern = re.compile(r'gallery: JSON.parse\("(.+?)"\),', re.S)
    result = re.search(images_pattern, html)
    if result:
        # print(result.group(1))
        try:
            data = json.loads(result.group(1).replace('\\', ''))
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                for image in images: download_image(image)
                return {
                    'title': title,
                    'url': url,
                    'images': images
                }
        except JSONDecodeError as e:
            print(e)


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('save mongo success.', result)
        return True
    else:
        return False


def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return save_image(response.content)
        else:
            return None
    except RequestException as e:
        print(e)
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.path.join(os.path.abspath('.'), 'images'), md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_datail(html, url)
            print(result)
            if result: save_to_mongo(result)


if __name__ == '__main__':
    pool = Pool(10)
    pool.map(main, [x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.close()
    pool.join()
    print('download finished')
