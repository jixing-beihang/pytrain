# coding: utf-8
import re
from util import *

print('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title> ...</title><body>')
title = True
for block in blocks('D:\\test_input.txt'):
    block = re.sub(r'\*(.+?)\*',r'<em>\l</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></head></html>')
