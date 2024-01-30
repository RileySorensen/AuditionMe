import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4
import json
from datetime import datetime

region_name = getenv('APP_REGION')
director_table = boto3.resource('dynamodb', region_name=region_name ).Table('DirectorTable')

def lambda_handler(event, context):
    director_id = str(uuid4())
    name = event["name"]
    email = event["email"]
    phoneNum = event["phoneNum"]   
    isCastingDir = event["isCasting"]
    password = event["password"]
    
    db_insert(director_id, name, email, phoneNum,isCastingDir, password)
    
    return response(200, {"Id": director_id, "newstuff": "here WAS HERE"})


# you can talk directly to dynamodb remotely in the cloud
def db_insert(director_id, name, email, phoneNum, isCastingDir, password):

    director_table.put_item(Item={
        'Id': director_id,
        'name' : name,
        'email' : email,
        'phoneNum': phoneNum,
        'isCastingDir':isCastingDir,
        'password':password
    })