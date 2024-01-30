import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4
import json
from datetime import datetime

region_name = getenv('APP_REGION')
performer_table = boto3.resource('dynamodb', region_name=region_name).Table('PerformerTable')


def lambda_handler(event, context):
    if "body" in event and event["body"] is not None:
        event = json.loads(event["body"])
    #GITHUB EDIT
    performer_id = str(uuid4())
    name = event["name"]
    email_address = event["emailAddress"]
    phone_num = event["phoneNum"]
    past_performances = event["pastPerformances"]
    current_performances = event["currentPerformances"]
    password = event["password"]
    print(region_name)
    db_insert(performer_id, name, email_address, phone_num, past_performances, current_performances, password)
    print("here2")
    return response(200, {"Id": performer_id, "newstuff": "here WAS HERE"})


# you can talk directly to dynamodb remotely in the cloud
def db_insert(performer_id, name, email_address, phone_num, past_performances, current_performances, password):
    performer_table.put_item(Item={
        'Id': performer_id,
        'name': name,
        'emailAddress': email_address,
        'phoneNum': phone_num,
        'pastPerformances': past_performances,
        'currentPerformances': current_performances,
        'password': password
    })


def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body),
        "isBase64Encoded": False
    }
