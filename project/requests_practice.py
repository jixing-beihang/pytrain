import requests
from pymongo import MongoClient
from selenium import webdriver
from redis import Redis

# print(requests.get('http://www.baidu.com'))
# webdriver = webdriver.Firefox()

# client = MongoClient('localhost',27017)
# db = client['newtestdb']
# db['table'].insert({'name':'Bob'})

# r = Redis('localhost',6379)
# r.set('name','Bob')
# print(r.get('name'))


# requests.get
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"
}
data = {
    'name':'Peter',
    'age':28
}
# response = requests.get('https://zhihu.com/explore',headers=headers)
# print(response.text)

# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)
# print(response.json())

# response = requests.get('http://httpbin.org/get', params=data, headers=headers)
# print(response.text)
# print(response.json())

# response = requests.get('https://github.com/favicon.ico')
# print(response.text)
# print(response.content)
# with open('favicon.ico','wb') as f:
#     f.write(response.content)

# requests.post
# res = requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(res.text)
# print(res.json())

# upload file
# files = {'file':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post', files=files)
# print(response.text)

# cookies : Session
# response = requests.get('http://www.baidu.com')
# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key + '=>' + value)


# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# response = requests.get('https://www.12306.cn', verify=False, timeout=1)
# print(response.status_code)