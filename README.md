# python_lambda

## lambdaサンプル

- docker/Dockefile 2020/05現在 python3.8
- lambda
    - event.json (引数:通常であればこちらから送るデータ。cloudwatchでeventをデバッグしてここに書き出す)
    - lambda_function.py (実行稼働され、エントリーポイントとなるプログラム)
    - lambda.json (lambda-uploaderコマンドの定義になるJSONファイル)
    - lambda_function.py (実行稼働されるプログラム)

### event.jsonに関して

実際の開発ではAWS管理画面のcloudwatchでログを吐き`print(event)`、これらをevent.jsonとして作成する。

デバックコマンド
```
python-lambda-local -f lambda_handler lambda_function.py event.json

```
注意
eventをcloudwatchに吐き出し、コピペしてevent.jsonに書き出す場合、
1. JSONのプロパティ名がシングルクオートで囲まれているので、ダブルクオートに直す
2. False,Noneなどがクオートでかこまれていないため、"False"などと囲む必要あり(Atomなどのエディタではシンタックスハイライト出るのでわかるはず。


ログ(cloudwatchをみよ)
```
[root - INFO - 2020-05-02 20:28:50,022] END RequestId: e62cee64-a9a1-4f37-917b-2bbd5a7962b4
[root - INFO - 2020-05-02 20:28:50,023] REPORT RequestId: e62cee64-a9a1-4f37-917b-2bbd5a7962b4	Duration: 3.45 ms
[root - INFO - 2020-05-02 20:28:50,023] RESULT:
{'statusCode': 200, 'body': '"Hello from Lambda!"'}

```

### デプロイ

1. zipでlambda/ を固めてあげる
lambdaディレクトリ直下を一気に固めてあげる
```
cd lambda/
zip -r upload.zip *
```

2. コマンドで一気にあげる(lambda.jsonが必須)
```
cd lambda/
lambda-uploader

#自動で上げてくれる
#欠点としてはライブラリが大きいと、非常に時間がかかる(Dockerで仮想環境だから?)
#隠しファイル、隠しフォルダは上がっているが見えない状態(適当なファイルを.〜にリネームすると表示される)
Î» Building Package
Î» Uploading Package
Î» Fin

```


### Lambda + APIGateway

Lambda + APIGateway<br>
https://qiita.com/tamura_CD/items/46ba8a2f3bfd5484843f#-api-gateway%E3%81%A7rest-api%E3%82%92%E4%BD%9C%E6%88%90



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
