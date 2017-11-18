# coding: utf-8

import MySQLdb
# db = MySQLdb.connect('192.168.2.91','root','_SKYc%123','django')
# cursor = db.cursor()
# cursor.execute("select version()")
# data = cursor.fetchone()
# print('Database version is %s.' % data)
# db.close()

# 创建数据表
# db = MySQLdb.connect('192.168.2.91','root','_SKYc%123','django')
# curse = db.cursor()
# sql = "CREATE TABLE EMPLOYEE(" \
#       "INAME CHAR(20) NOT NULL, " \
#       "AGE INT," \
#       "SEX CHAR(1)," \
#       "INCOME FLOAT )"
# try:
#     curse.execute(sql)
# except Exception as e:
#     db.rollback()
#     print(e)
# finally:
#     db.close()

# 操作数据，insert，delete，update
# db = MySQLdb.connect('192.168.2.91','root','_SKYc%123','django')
# curse = db.cursor()
# # sql = "INSERT INTO EMPLOYEE(INAME,AGE,SEX,INCOME) VALUES('Apache',12,'f',12345)"
# sql = "INSERT INTO EMPLOYEE(INAME,AGE,SEX,INCOME) VALUES('%s',%d,'%c',%f)" % ('Tomcat',27,'m',14000.0) # 插入操作
# # sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')  # 更新操作
# # sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20) # 删除操作
# try:
#     curse.execute(sql)
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)
# finally:
#     db.close()


# 查询操作
db = MySQLdb.connect('192.168.2.91','root','_SKYc%123','django')
curse = db.cursor()
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %d" % (10000) # 查询操作
try:
    curse.execute(sql)
    results = curse.fetchall()
    for result in results:
        name = result[0]
        age = result[1]
        sex = result[2]
        income = result[3]
        print("name:%s,age:%d,sex:%c,income:%f" % (name,age,sex,income))
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.close()