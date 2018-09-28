# Mysqlpython.py

from pymysql import connect


class MysqlHelp:
    def __init__(self, database,
                 host='localhost',
                 user='root',
                 password='123456',
                 charset='utf8',
                 port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
    # 连接数据库

    def open(self):
        self.conn = connect(
            database=self.database,
            host=self.host,
            user=self.user,
            password=self.password,
            charset=self.charset,
            port=self.port)

        self.cur = self.conn.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    # 执行SQL语句
    def work(self, sql, L=[]):
        self.open()
        try:
            self.cur.execute(sql, L)
            self.conn.commit()
            print('OK')
        except Exception as e:
            self.conn.rollback()
            print('Failed', e)
        self.close()
    # 查询

    def getAll(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        print('OK')
        result = self.cur.fetchall()

        self.close()
        return result


# if __name__ == '__main__':
    # 测试
    # mysql = MysqlHelp('db4')
    # sheng_insert = "insert into sheng(s_name) values('河北省');"
    # mysql.work(sheng_insert)
