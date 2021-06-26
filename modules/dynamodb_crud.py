import os
import uuid
import boto3

def read_dynamodb():
    # write logic
    print('hoge')

def post_dynamodb():
    # write logic
    print('hoge')

def update_dynamodb():
    # write logic
    print('hoge')

def delete_dynamodb():
    # write logic
    print('hoge')

print('choose this convert type.' )
print('1: read_dynamodb' )
print('2: post_dynamodb' )
print('3: update_dynamodb' )
print('4: delete_dynamodb' )

print(os.environ['DYNAMODB'])
print(os.environ['REGION_NAME'])
print(os.environ['ENDPOINT_URL_PORT'])
print(os.environ['AWS_ACCESS_KEY_ID'])
print(os.environ['AWS_SECRET_ACCESS_KEY'])