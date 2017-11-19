import re
import requests_practice
from requests import exceptions

try:
    response = requests_practice.get('http://www.douban.com')
    # print(response.text)

    partten = re.compile('<li>.*?<a\sclass="cover.+?<a\sclass="title"\shref="(.+?)">(.+?)</a>.+?<span.+?>(.+?)</span>.+?</li>',re.S)
    # partten = re.compile('<li>.*?<a\shref="(.+?)">(.+?)</a>.+?<span.+?>(.+?)</span>.+?</li>', re.S)
    results = re.findall(partten, response.text)
    for result in results:
        href, name, span = result
        print(href, name, span)

except exceptions.HTTPError as e:
    print(e)
