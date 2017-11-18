import fileinput
# 操作文件 file
# 使用try/except finally 语句完成读取文件
# try:
#     f = open('D:\\file.txt','r',1)
#     print(f.readline())
# except IOError as e:
#     print(e)
# finally:
#     f.close()
#
# 使用 with 语句，读文件 read(n)，read，readline，readlines
with open('D:\\file.txt','r+',1) as f:
    for line in f.readlines():
        if len(line) > 2:
            print(line.strip())
            f.write(line.strip())
# 使用 with 语句，写文件 write，writelines
# with open('D:\\test.txt', 'w', 1) as f:
#     f.write('01234567890123456789')
#     f.seek(5)
#     f.write('Hello World!')

# 使用 fileinput
# for line in fileinput.input('D:\\file.txt'):
#     print(line)

