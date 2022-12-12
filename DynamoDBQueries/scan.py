import boto3
client = boto3.client('dynamodb')

resp = client.scan(
  TableName='MovieRoles',
  IndexName='ByMovie'
)