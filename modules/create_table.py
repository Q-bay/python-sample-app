import os
import boto3

dynamodb = boto3.resource(
    os.environ['DYNAMODB'],
    region_name= os.environ['REGION_NAME'],
    endpoint_url= os.environ['ENDPOINT_URL_PORT'],
    aws_access_key_id= os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key= os.environ['AWS_SECRET_ACCESS_KEY']
)

table = dynamodb.create_table(
    TableName='test',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print('Table status:', table.table_status)