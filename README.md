# python_lambda

## lambdaサンプル

- event.json (引数:通常であればこちらから送るデータ)
- lambda_sample.py (lambdaに挙げるプログラムそのもの)

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
