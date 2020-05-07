from dao.dao import Dao
from conf.config import *

if __name__ == '__main__':
    mysql = Dao(HOST, PORT, USERNAME, PASSWORD, 'develop', 'weapp_store_region')
    columns = ['name', 'parent_id', 'type', 'state', 'initial', 'pinyin',
               'uniqid_pinyin']
    datas = mysql.find(columns, 'parent_id>0 limit 1000')
    result = []
    for data in datas['data']:
        s = data.values()
        result.append([i for i in s])
    sql = []
    for r in result:
        col  = []
        for s in r:
            if isinstance(s,int):
                col.append(str(s))
            elif isinstance(s,str):
                col.append("'{}'".format(s))
        sql.append("( "+" , ".join(col)+" )")
    print(sql)

