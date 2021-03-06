# -*- coding:utf-8 -*-
import json
import re
from multiprocessing import Pool

import requests
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def parse_one_parse(html):
    partten = re.compile('<dd>.+?board-index.+?>(\d+)</i>.+?data-src="(.+?)".+?name"><a.+?>(.+?)'
                         '</a>.+?star">(.+?)</p>.+?releasetime">(.+?)</p>.+?'
                         'integer">(.+?)</i>.+?fraction">(.+?)</i></p>.+?</dd>', re.S)

    items = re.findall(partten, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_parse(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool(10)
    pool.map(main, [i * 10 for i in range(10)])
    # pool.map_async(main, [i * 10 for i in range(10)])
    pool.close()
    pool.join()
    print('finished ...')
