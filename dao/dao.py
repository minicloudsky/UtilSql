import pymysql
from common import *


class Dao():
    host = '127.0.0.1'
    port = 3306
    username = ''
    password = ''
    databse = ''
    table_name = ''
    charset = 'utf8mb4'
    instance = None
    cursor = None

    def __init__(self, host='127.0.0.1', port=3306, username='root', password='', database='',
                 table_name='', charset='utf8mb4'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.databse = database
        self.table_name = table_name
        self.charset = charset
        self.connect()

    def connect(self):
        self.instance = pymysql.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            db=self.databse,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        if self.instance.server_status == 0:
            self.cursor = self.instance.cursor()
            return self.instance
        fail_data_format['msg'] = 'get mysql instance error'
        return fail_data_format

    def close(self):
        try:
            result = self.instance.close()
            return result
        except:
            return {'status': -1, 'msg': 'close error'}

    def create_table(self, columns={}):
        table = 0

    def drop_table(self, table_name):
        table = 0

    def find(self, columns=[], cond=[], order_by_column="", order="ASC", group_by_column=""):
        sql = "select "
        if columns:
            sql += ",".join(columns)
            sql += " from {}".format(self.table_name)
        else:
            sql += " * from {} ".format(self.table_name)
        if cond:
            sql += " where {}".format(cond)
        if order_by_column and order != "ASC" and order:
            sql += " order by {} {}".format(order_by_column, order)
        if group_by_column:
            sql += " group by {}".format(group_by_column)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            success_data_format['data'] = result
            return success_data_format
        except pymysql.Error:
            return {'status': -1, 'data': 'find error'}

    def update(self, record, cond):
        datas = " "
        for key, value in record.items():
            if isinstance(value, str):
                datas += "{} = '{}',".format(key, value)
            elif isinstance(value, int) or isinstance(value, float):
                datas += "{} = {},".format(key, value)
            else:
                datas += "{} = {},".format(key, value)
        datas = datas[:-1]
        datas += " "
        try:
            sql = "update {} set {} where {}".format(datas, self.table_name, cond)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except pymysql.Error:
            fail_data_format['msg'] = 'update error'
            return fail_data_format

    def delete_by_id(self, id):
        data = []

    def delete_by_cond(self, cond):
        data = []

    def count(self, cond):
        data = []
