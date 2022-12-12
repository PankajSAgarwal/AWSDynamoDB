import boto3

client = boto3.client('dynamodb')

resp = client.update_item(
  TableName='MovieRoles',
  Key={
    'Actor': { 'S': 'Tom Hanks' },
    'Movie': { 'S': 'Toy Story' }
  },
  UpdateExpression="SET #boxoffice = :boxoffice",
  ExpressionAttributeNames={
    "#boxoffice": "Box Office Receipts"
  },
  ExpressionAttributeValues={
    "boxoffice": { "N": "373600000" }
  }
)