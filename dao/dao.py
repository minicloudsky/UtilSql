import pymysql
from conf.constants import *


class Dao():
    host = '127.0.0.1'
    port = 3306
    username = ''
    password = ''
    database = ''
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
        self.database = database
        self.table_name = table_name
        self.charset = charset
        self.connect()

    # get a mysql connect instance
    def connect(self):
        self.instance = pymysql.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            db=self.database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        if self.instance.server_status == 0:
            self.cursor = self.instance.cursor()
            return self.instance
        fail_format['msg'] = 'get mysql instance error'
        return fail_format

    # close mysql connection
    def close(self):
        try:
            result = self.instance.close()
            return result
        except:
            return {'status': -1, 'msg': 'close mysql connection error'}

    def create_table(self, columns={}):
        table = 0

    def drop_table(self, table_name):
        sql = 'drop table {}'.format(table_name)
        return self.execute_sql(sql, "drop table error")

    def add_column(self, table_name, column, type, default=0, is_null=True, comment=''):
        sql = ''

    # batch drop columns
    def drop_columns(self, table_name=[], columns=[]):
        sql = "alter table {} ".format(table_name)
        for column in columns:
            sql += "drop column {},".format(column)
        sql = sql[:-1]
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            success_format['data'] = result
            return success_format
        except pymysql.Error:
            return {'status': -1, 'data': 'drop column error'}

    def find(self, columns=[], cond=[], group_by_column='id', order_by_column="", order="ASC"):
        sql = "select "
        if columns:
            sql += ",".join(columns)
            sql += " from {}".format(self.table_name)
        else:
            sql += " * from {} ".format(self.table_name)
        if cond:
            sql += " where {}".format(cond)
        if group_by_column is not 'id' and isinstance(group_by_column, list):
            sql += " group by {}".format(",".join(group_by_column))
        elif group_by_column is not 'id' and isinstance(group_by_column, str):
            sql += " group by {}".format(group_by_column)
        if order_by_column and order != "ASC" and order:
            sql += " order by {} {}".format(order_by_column, order)
        return self.execute_sql(sql, "find error")

    def findone(self, columns=[], cond=[], order_by_column="", order="ASC", group_by_column=""):
        sql = "select "
        if columns:
            sql += ",".join(columns)
            sql += " from {}".format(self.table_name)
        else:
            sql += " * from {} ".format(self.table_name)
        if cond:
            sql += " where {}".format(cond)
        if group_by_column:
            sql += " group by {}".format(group_by_column)
        if order_by_column and order != "ASC" and order:
            sql += " order by {} {}".format(order_by_column, order)
        sql += " limit 1"
        return self.execute_sql(sql, 'find one error')

    # get data by page
    def get_by_page(self, table_name='', columns=[], cond='', page=1, page_size=20,
                    group_by='id', order_by='id', order='ASC'):
        sql = "select " + ",".join(columns) + "from {}".format(table_name)
        if cond:
            sql += cond
        if isinstance(group_by, list):
            sql += "group by " + " , ".join(group_by)
        elif group_by is not 'id':
            sql += "group by " + group_by
        if order_by is not 'id' or order is not 'ASC':
            sql += "order by {} {}".format(order_by, order)
        sql += "limit {},{}".format(page, page_size)
        return self.execute_sql(sql, 'get by page error')

    def update(self, table_name, record, cond):
        columns = " "
        for key, value in record.items():
            if isinstance(value, str):
                columns += "{} = '{}', ".format(key, value)
            else:
                columns += "{} = {}, ".format(key, value)
        sql = "update {} set {} where {}".format(table_name, columns, cond)
        return self.execute_sql(sql, 'update error')

    def delete_by_id(self, table_name, id):
        sql = "delete from {} where id = {}".format(table_name, id)
        return self.execute_sql(sql, 'delete by id error')

    def delete_by_cond(self, table_name, cond):
        sql = "delete from {} where {}".format(table_name, cond)
        return self.execute_sql(sql, 'delete by cond error')

    def count(self, cond):
        data = []

    # exec  sql
    def execute_sql(self, sql='', error_msg='execute sql error'):
        result  = []
        if sql:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                success_format['data'] = result
                return success_format
            except pymysql.Error:
                fail_format['data'] = result
                fail_format['msg'] = error_msg
                return fail_format
        fail_format['msg'] = 'sql can not be empty'
        return fail_format
