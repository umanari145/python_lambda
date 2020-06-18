import json
import boto3

def lambda_handler(event, context):

    print('--------');
    print(event);
    print('---------');
    print('---本日は晴天なり--');

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
