# 异常Exception
# raise ZeroDivisionError

#  try/except 语句
# try:
#     x = int(input('enter the first number:'))
#     y = int(input('enter the second number:'))
#     print(x / y)
# except (ZeroDivisionError,TypeError,Exception) as e:
#     print(e)

# try/except,else,finally
try:
    # a / 1
    # 1 / 0
    'a' / 1
    # 1 / 1
except NameError:
    print('Unknown variable')
except ZeroDivisionError:
    print('Division by zero')
except Exception as e:
    print(e)
else:
    print('Works well')
finally:
    print('Do some clear up')

