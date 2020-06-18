# python_lambda

## lambdaサンプル

- docker/Dockefile 2020/05現在 python3.8
- event.json (引数:通常であればこちらから送るデータ)
- lambda_sample.py (lambdaに挙げるプログラムそのもの)


### event.jsonに関して

実際の開発ではAWS管理画面のcloudwatchでログを吐き`print(event)`、これらをevent.jsonとして作成する。

デバックコマンド
```
python-lambda-local -f lambda_handler lambda_sample.py event.json

```

ログ
```
[root - INFO - 2020-05-02 20:28:50,022] END RequestId: e62cee64-a9a1-4f37-917b-2bbd5a7962b4
[root - INFO - 2020-05-02 20:28:50,023] REPORT RequestId: e62cee64-a9a1-4f37-917b-2bbd5a7962b4	Duration: 3.45 ms
[root - INFO - 2020-05-02 20:28:50,023] RESULT:
{'statusCode': 200, 'body': '"Hello from Lambda!"'}

```

### Lambda + APIGateway + DynamoDB

Lambda + APIGateway
https://qiita.com/tamura_CD/items/46ba8a2f3bfd5484843f#-api-gateway%E3%81%A7rest-api%E3%82%92%E4%BD%9C%E6%88%90


Lambda + dynamodb
https://qiita.com/hellscare/items/d80c9ff0290966eb0cf8




### DynamoDB

cliコマンド
https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html#cli-aws-dynamodb

```
#全件取得
aws dynamodb scan \
--table-name テーブル名

#特定キーで取得
aws dynamodb get-item \
--table-name product_conditions \
--key '{"product_id":{"N":"1"}}'

#新規データ追加
aws dynamodb put-item \
    --table-name product_conditions \
    --item '{
        "product_id": {"N": "3"},
        "product_name": {"S": "本"} ,
        "price_min": {"N": "111"},
        "price_max": {"N": "222"}         
      }'

```
botob<br>

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
