from dao.dao import Dao
from conf.config import *
if __name__ == '__main__':
    mysql = Dao(HOST,PORT,USERNAME,PASSWORD,'develops','weapp_store_region')
    result = mysql.get_by_page(['id','name','pinyin'],'id<20')
    print(result)
