# mysql1.py
import pymysql
import re
from Mysqlpython import MysqlHelp

mysql = MysqlHelp('dict')
fr = open('dict.txt')
# for i in fr:
#     a = re.match(r'\S*', i).group()
#     b = re.sub(r'^\S*', '', i).strip()
    # print(b)
    # print(a)
    # lll = "insert into words values(null,%s,%s)"
    # mysql.work(lll, L = [a, b])



s = fr.readline()
l = re.split(r'\s+',s)
print(l)
inte = ' '.join(l[1:])
print(inte)