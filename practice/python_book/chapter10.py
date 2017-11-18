# 正则匹配 . \ [a-zA-Z0-9\_] | () ? * + ^ $ {m-n}
# re 模块 compile search match split sub escape group(start end span)
import re,fileinput
# re 函数compile，match，group
pat = re.compile('From: (.*)<.*?>$',re.VERBOSE)
for line in fileinput.input('D:\\log.log'):
    m = re.match(pat,line)
    if m:
        print(m.group(1),m.start(1),m.end(1),m.span(1))

# re.split 进行分割
print(re.split(r'\s+','a b   c  d'))
print(re.split(r'[\s\,]+','a, b,   c,,  d'))
print(re.split(r'[\s\,\;]+','a, b;   c  d'))

# re.sub 进行替换
print(re.sub(r'{name}','Mr Gummy','Dear {name}'))

# re.escape 进行转义
print(re.escape('www.python.org'))
print(re.escape('But where is the dog!'))
# 匹配邮箱
print(re.match(r'(.+?)@(.+?)\.(.+?)','someone@gmail.com'))

# compile，match，groups
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-123456').groups())