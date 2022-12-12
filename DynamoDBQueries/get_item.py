import boto3
client = boto3.get_client('dynamodb')

resp = client.get_item(
  TableName='MovieRoles',
  Key={
    'Actor': { 'S': 'Tom Hanks'},
    'Movie': { 'S': 'Toy Story'}
  },
  ConsistentRead=True
)
