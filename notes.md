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
`
{
    "calories_limit": 3,
    "intolorences": ["1","2"],
    "budget": 2
}
`
# diet
- path diet/
- json:
`
 {
   "vegan": true,
   "vegetarian" : true,
   "glutenfree": true,
   "ketogenic": true,
   "pescetarian": true,
   "peleo": true
 }
 `

# meals
meals/
- json:
`
 {
     'breakfast': bool,
     'lunch': bool,
     'dinner': bool,
     'dessert': bool,
     'snack': bool
}`

# meal history
mealhistory/
{
    "user_id": "billie",
    "recipes": ['1', '2', '3']
}

# login
{
    "username": "billie",
    "password": "Hello"
}