import psycopg2
import pymysql
import psycopg2.extras
from psycopg2.extras import DictCursor


class Mysqlhandler():
    def __init__(
            self,
            host=None,
            port=None,
            user=None,
            password=None,
            database=None
            ):
        """配置文件"""
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def query(self,sql,one = False):
        self.conn.commit()#提交事务（把最新的数据进行更新）
        self.cursor.execute(sql)
        if not one:
            columns = [desc[0] for desc in self.cursor.description]
            #转成字典
            results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            return results
            # return self.cursor.fetchall()
        else:
            columns = [desc[0] for desc in self.cursor.description]
            rows = self.cursor.fetchone()
            dict_data = {}
            #转成字典
            for i,row in enumerate(rows):
                dict_data[columns[i]] = row
            return dict_data


    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    pass