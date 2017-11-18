from math import pi
# 字符串格式化  %
format1 = "Hello %s. %s enough for ya ?"
values = ('world','Hot')
print(format1 % values)

format2 = "Pi with three decimals: %.3f"
print(format2 % pi)
# 字符串方法 find
subjects = "$$$ Get rich now !!! $$$"
print(subjects.find('$$$'))
print(subjects.find('$$$',1))
print(subjects.find('$$$',1,20))
# 字符串方法 join
sep = ['1','2','3','4']
seq = '+'
print(seq.join(sep))
dirs = '','usr','local','tomcat'
print('/'.join(dirs))
# 字符串方法 lower,upper
print("Ji Xing".upper())
print("Ji Xing".lower())
# 字符串方法 replace
str = "This is a test ."
print(str.replace('is','eez'))
# 字符串方法 split,strip
str1 = "  !! ++  1+2+3+4  !! ++"
print(str1.split("+"))
print(str1.strip(" !+"))
