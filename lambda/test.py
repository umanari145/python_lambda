import DBUtil
import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TABLE_NAME = os.environ.get("TABLE_NAME")
#print(TABLE_NAME)
dbUtil = DBUtil.DBUtil(TABLE_NAME, 'product_id')


##data = dbUtil.getData({
## 'key':'product_id',
## 'value':1
##})
##
##print(data)

#data = dbUtil.getAllDataCount()
#print(data+1)


#res = dbUtil.createData({
# #重複すると自動的に更新になる
# "product_id":8,
# "product_name": "宇都宮検事",
# "price_min": "1234",
# "price_max": "345987"
#})
#print(res)

#res = dbUtil.deleteData(6)
#print(res)
