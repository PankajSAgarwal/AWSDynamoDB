const AWS = require('aws-sdk')
const docClient = new AWS.DynamoDB.DocumentClient()

const resp = docClient.put({
  TableName: 'MovieRoles',
  Item: {
    'Actor': 'Tom Hanks',
    'Movie': 'Toy Story',
    'Role': 'Woody',
    'Year': 1995,
    'Genre': "Children's"
  }
})