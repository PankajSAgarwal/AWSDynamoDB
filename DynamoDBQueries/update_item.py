import boto3

client = boto3.client('dynamodb')
resp = client.update_item(
  TableName='Bank Account',
  Key={
    "AccountId" : { "S": "12345" }
  },
  ConditionExpression="#balance >= :payment",
  UpdateExpression="SET #balance = #balance - :payment",
  ExpressionAttributeNames={
    "#balance": "Balance"
  },
  ExpressionAttributeValues={
    ":payment" : { "N": "31.79" }
  }
)