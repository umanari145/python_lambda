import json

###
###　関数名は固定
###
def lambda_handler(event, context):

    print('--------');
    print(event);
    print('---------');

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
