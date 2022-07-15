# Path 

### Create a new user
- path: createuser/
- json:
`
{
    "name": 'name',
    'email': 'email',
    'password':'password'
}`

### Create preferences
- path addpref/
- json: 
`
{
    "calories_limit": 3,
    "intolorences": ["1","2"],
    "budget": 2
}
`
### Set diet
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

### Get meals
meals/
- json:
`
 {
     'breakfast': bool,
     'lunch': bool,
     'dinner': bool,
     'dessert': bool,
     'snack': bool
}
`

### Get meal history
mealhistory/
`
{
    "user_id": "billie",
    "recipes": ['1', '2', '3']
}
`
### Login
`
{
    "username": "billie",
    "password": "Hello"
}
`
### Logout
-just a get call to url