const AWS = require('aws-sdk')
const dynamodb = new AWS.DynamoDB()

const resp = dynamodb.putItem({
  TableName: 'MovieRoles',
  Item: {
    'Actor': { 'S': 'Tom Hanks' },
    'Movie': { 'S': 'Toy Story' },
    'Role': { 'S': 'Woody' },
    'Year': { 'N': '1995' },
    'Genre': { 'S': "Children's" }
  }
})
