from http import client
import boto3
client = boto3.client("dynamodb")

resp = client.put_item(
  TableName='MovieRoles',
  Item={
    'Actor': { 'S': 'Tom Hanks'},
    'Movie': { 'S': 'Toy Story'},
    'Role': { 'S': 'Woody'},
    'Year': { 'N': '1995'},
    'Genre': { 'S': "Children's"} 
  }
)