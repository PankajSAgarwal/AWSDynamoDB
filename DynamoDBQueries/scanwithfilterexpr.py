import boto3
client=boto3.client('dynamodb')
resp = client.scan(
  TableName='MovieRoles',
  FilterExpression="#genre = :genre",
  ExpressionAttributeNames={
    '#genre': 'Genre'
  }
  ExpressionAttributeValues={
    ':genre': { 'S': 'Drama' }
  }
)