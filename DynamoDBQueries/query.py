import boto3

client = boto3.client("dynamodb")

resp = client.query(
  TableName='MovieRoles',
  KeyConditionExpression="Actor = 'Tom Hanks' "
)