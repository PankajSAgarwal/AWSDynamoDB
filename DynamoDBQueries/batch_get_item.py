import boto3

client = boto3.client('dynamodb')

resp = client.batch_get_item(
  RequestItems={
    'MovieRoles': {
      'Keys': [
        {
          'Actor': {'S': 'Tom Hanks'},
          'Movie': {'S': 'Toy Story'}
        },
        {
          'Actor': {'S': 'Tom Hanks'},
          'Movie': {'S': 'Cast Away'}
        }
      ]
    }
  }
)