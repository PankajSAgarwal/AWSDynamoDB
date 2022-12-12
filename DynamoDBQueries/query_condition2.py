import boto3

client = boto3.client('dynamodb')

resp = client.query(
  TableName='MovieRoles',
  KeyConditionExpression="#actor = :actor AND #movie BETWEEN :a and :m",
  ExpressionAttributeNames={
    '#actor': 'Actor',
    '#movie': 'Movie'
  }
  ExpressionAttributeValues={
    ':actor': { 'S': 'Tom Hanks' },
    ':a': { 'S': 'A' },
    ":m": { 'S': 'M' }
  }
)