import json
import Controller

def lambda_handler(event, context):

    httpMethod = event["requestContext"]["httpMethod"]
    url = event["requestContext"]["resourcePath"]

    controller = Controller.Controller(httpMethod, url)
    #print(controller)
    res = controller.getResponce()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
