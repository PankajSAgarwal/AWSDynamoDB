import boto3
client = boto3.client('dynamodb')
resp = client.query(
  TableName='MovieRoles',
  KeyConditionExpression = "#actor = :actor",
  ProjectionExpression = "#actor, #movie, #role, #year, #genre",
  ExpressionAttributeNames={
    '#actor': 'Actor',
    '#movie': 'Movie',
    '#role': 'Role',
    '#year': 'Year',
    '#genre': 'Genre'
  }
  ExpressionAttributeValues={
    ':actor':{ 'S': 'Tom Hanks' }
  } 
)