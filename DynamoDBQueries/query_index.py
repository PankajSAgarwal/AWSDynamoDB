import boto3
client = boto3.client('dynamodb')

resp = client.query(
  TableName='MovieRole',
  IndexName='ByMovie',
  KeyConditionExpression="Movie = 'Toy Story' "
)