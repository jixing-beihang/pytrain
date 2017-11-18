'''
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

*** 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
        username | password
        ---------+---------------------------------
        michael  | e10adc3949ba59abbe56e057f20f883e
        bob      | 878ef96e86145580c38c87f0410ad153
        alice    | 99b1c2188db85afee403b1536010c2c9

*** 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
    def calc_md5(password):
        return get_md5(password + 'the-Salt')
'''

import hashlib

# 摘要算法 md5 得到128 bit、32位16进制的字符串
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 摘要算法 sha1 得到160 bit、40位16进制的字符串
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
