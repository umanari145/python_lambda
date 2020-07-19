import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

class DBUtil():

    def __init__(self,table_name, primary_key_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table    = self.dynamodb.Table(table_name)
        self.primary_key_name = primary_key_name

    #
    # データの取得
    # @params dictonary where_dic 検索キー
    # @return 値(配列)
    #
    def getData(self, where_dic):

        where_name = where_dic['key']
        value = where_dic['value']

        items = self.table.get_item(
            Key = {
                 where_name: value
            }
        )

        return items

    #
    # 全データの取得
    # @return 値(配列)
    #
    def getAllData(self):
        items = self.table.scan()
        return items

    #
    # 全データの取得
    # @return 値(配列)
    #
    def getAllDataCount(self):
        return self.table.scan()['Count']

    #
    # 新規データの作成、更新
    # @params dictonary item
    # @return 値(配列)
    #
    def createData(self, item):
        #主キーが一緒なら更新になる
        if (self.primary_key_name in item) == False:
            item['product_id'] = self.getAllDataCount() + 1

        res = self.table.put_item(Item=item)
        return res
    #
    # データの削除
    # @params string primary_key_value 主キーの値
    # @return 値(配列)
    #
    def deleteData(self, primary_key_value):
        res = self.table.delete_item(Key={
            self.primary_key_name:primary_key_value
        })

        return res
