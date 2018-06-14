#-*- coding:utf-8 -*-
# Do not delete the following import lines
import time

file = open('D:\\Users\\qiuyi.shen\\Work\\TMT131B_3D_Section\\Section38m.jnl')

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        print(line)
        time.sleep(0.1)