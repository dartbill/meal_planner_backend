# Paths 

### Login
- path: `login/`
    - method: POST
        - accepts: `{"email": "billie@gmail.com","password": "Hello"}`
        - returns: `{'message': 'login successful'}`
### Logout
- path: `logout/`
    - method: GET
        - accepts: Null
        - returns: `{'message': 'User logged out'}`

### Create a new user
- path: `createuser/`
    - method: POST
        - accepts: `{ "name": 'name', 'email': 'email', 'password':'password'}`
        - returns: `{'message': 'user successfully created'}`
        <!-- update password/email  stretch goal -->
### Preferences
- path: `createprefs/`
    - method: POST

        - accepts: `{"prefs":{"calories_limit": {"breakfast":2,"lunch":2,"dinner":2,"snack":2,"dessert":2}, "intolorences": ["dairy","egg"], "budget": {"breakfast":2,"lunch":2, "dinner":2,"snack":2,"dessert":2}}, "diet":{"vegan": true,"vegetarian" : true,"glutenfree": true,"ketogenic": true, "pescetarian": true, "paleo": true}, "meals":{"breakfast": true,"lunch": true,"dinner": true,"dessert": true,"snack": true}}`

        - returns: `{'message': 'Preferences successfully added'}`
- path: `prefs/`
    - method: PATCH 
        - accepts: `{"prefs":{"calories_limit": {"breakfast":2,"lunch":2,"dinner":2,"snack":2 "dessert":2}, "intolorences": ["dairy","egg"], "budget": {"breakfast":2,"lunch":2,"dinner":2 "snack":2,"dessert":2}}, "diet":{"vegan": true,"vegetarian" : true,"glutenfree": true "ketogenic": true, "pescetarian": true, "paleo": true}, "meals":{"breakfast": true,"lunch": true,"dinner": true,"dessert": true,"snack": true}}`
        - returns: `{'message': 'Preferences successfully updated'}`
    - method: GET
        - accepts: Null
        - returns: `[
  {
    "calories_limit": "{'breakfast': 2, 'lunch': 2, 'dinner': 2, 'snack': 2, 'dessert': 2}",
    "intolorences": [
      "dairy",
      "egg"
    ],
    "budget": "{'breakfast': 2, 'lunch': 2, 'dinner': 2, 'snack': 2, 'dessert': 2}"
  },
  {
    "breakfast": true,
    "lunch": true,
    "dinner": true,
    "dessert": true,
    "snack": true
  }
]`


### Meal History
- path `mealhistory/`
    - method: POST
        - accepts:`    {
      "today_date": "18/07/2022",
      "recipes": {
        "breakfast": [{"id":"", "title": "", "fave":""}], 
         "lunch": [{"id":"", "title": "", "fave":""}], 
        "dinner": [{"id":"", "title": "", "fave":""}], 
         "dessert": [{"id":"", "title": "", "fave":""}], 
         "snacks": [{"id":"", "title": "", "fave":""}]}}`
        - returns: `{'message': 'Meal history successfully added'}`
    - method GET
        - accepts: Null
        - returns: `{
    "recipes": {
      "breakfast": [
        {
          "id": "",
          "title": "",
          "fave": ""
        }
      ],
      "lunch": [
        {
          "id": "",
          "title": "",
          "fave": ""
        }
      ],
      "dinner": [
        {
          "id": "",
          "title": "",
          "fave": ""
        }
      ],
      "dessert": [
        {
          "id": "",
          "title": "",
          "fave": ""
        }
      ],
      "snacks": [
        {
          "id": "",
          "title": "",
          "fave": ""
        }
      ]
    },
    "today_date": "18/07/2022"
  }`
        <!-- datetime to accept a string -->

### Email
- path `email/`
    - method: POST
        - accepts: `{"message":"hi this is from the web!",
"html": "<h1>test html</h1>"}`
        - returns: `{'message': 'email sent successfully'}`

