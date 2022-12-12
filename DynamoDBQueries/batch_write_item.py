import boto3
client = boto3.client('dynamodb')

resp=client.batch_write_item(
  RequestItems={
    'MovieRoles': [
      {
        'PutRequest': {
          'Item': {
            'Actor': { 'S': 'Tom Hanks'},
            'Movie': { 'S': 'Toy Story'},
            'Role': { 'S': 'Woody'},
            'Year': { 'N': '1995'},
            'Genre': { 'S': "Children's"}
          }
        }
      },
      {
        'DeleteRequest': {
          'Key': {
            'Actor': { 'S': 'Tom Hanks'},
            'Movie': {'S': 'Cast Away'}
          }
        }
      }
    ]
  }
)