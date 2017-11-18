import http.cookiejar
import urllib
from urllib import parse, error
from urllib.request import urlopen, Request

# urlopen
# with urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# Request 对象请求urlopen(Request)
# url = 'http://httpbin.org/post'
# header = {
#     'User-Agent':'Mozilla/4.0(compatible;MSIE  5.5;Windows NT)'
# }
# dizt = {
#     'name':'Peter'
# }
# data = bytes(parse.urlencode(dizt),encoding='utf-8')
# req = Request(url=url,data=data,headers=header,method='POST')
# res = urlopen(req)
# print(res.read().decode('utf-8'))

# ProxyHander
proxy_handler = urllib.request.ProxyHandler(
    {
        'http':'http://127.0.0.1:9743',
        'https':'https://127.0.0.1:9743'
    }
)
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org')
print(response.read())

# 保存cookie.save
# file = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(file)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=>' + item.value)
# cookie.save(ignore_discard=True, ignore_expires=True)


# # cookie.load
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))


try:
    with urlopen('http://www.baidu.com', timeout=1) as f:
        print(f.read().decode('utf-8'))
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except error.URLError as e:
    print(e.reason)
