# Path 

### create a new user
- path: createuser/
- json:
`
{
    "name": 'name',
    'email': 'email',
    'password':'password'
}`

- path addpref/
- json: 
`
{
    'user_id': 'name',
    'diet_id': 'diet id',
    'meals_id': 'meals id',
    'calories_limit': int,
    'intolorences': [],
    'budget': int
}
`

-json:
`
 {
   'vegan': bool,
   'vegetarian' : bool,
   'glutenfree': bool,
   'ketogenic': bool,
   'pescetarian': bool,
   'peleo': bool
 }
 `


- json:
`
 {
     'breakfast': bool,
     'lunch': bool,
     'dinner': bool,
     'dessert': bool,
     'snack': bool
}`



{
    "user_id": "billie",
    "recipes": ['1', '2', '3']
}

login
{
    "username": "billie",
    "password": "Hello"
}