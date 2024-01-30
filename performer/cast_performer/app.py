import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4
import json

region_name = getenv('APP_REGION')
performance_table = boto3.resource('dynamodb', region_name=region_name ).Table('PerformanceTable')
def lambda_handler(event, context):

    Performance_id = event['Performance Id']
    name = event['name']
    if "id" is not event or id is None:
        response(400, "Id is required")

    performance = performance_table.get_item(Key={"Id":id})["Item"]

    if performance is None:
        response(404, "TODO not found")
    if name is not None:
        performance.characters.append(name)

    performance_table.put_item(Item=todo)
    return response(200, todo)


def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
            },
        "body": json.dumps(body)
    }