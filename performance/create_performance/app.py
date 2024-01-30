import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4
import json
from datetime import datetime

region_name = getenv('APP_REGION')
performance_table = boto3.resource('dynamodb', region_name=region_name ).Table('PerformanceTable')

def lambda_handler(event, context):
    performance_id = str(uuid4())
    title = event["title"]
    director = event["director"]
    castingDirector = event["castingDirector"]
    performanceDates = event["performanceDates"]
    characters = event["characters"]
    venue = event["venue"]
    db_insert(performance_id, title, director, castingDirector, performanceDates, characters, venue)
    
    return response(200, {"Id": performance_id, "newstuff": "here WAS HERE"})


# you can talk directly to dynamodb remotely in the cloud
def db_insert(performance_id, title, director, castingDirector, performanceDates, characters, venue):

    performance_table.put_item(Item={
        'Id': performance_id,
        'title': title,
        'director':director,
        'castingDirector':castingDirector,
        'performanceDates':performanceDates,
        'characters':characters,
        'venue':venue
    })