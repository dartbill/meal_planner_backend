# Paths 

### Create a new user
- path: `createuser/`
    - method: POST
        - accepts: `{ "name": 'name', 'email': 'email', 'password':'password'}`
        - returns: `{'message': 'user successfully created'}`
### Preferences
- path: `createprefs/`
    - method: POST
        - accepts: `{"prefs":{"calories_limit": 3, "intolorences": ["1","2"], "budget": 2},"diet":{"vegan": true,"vegetarian" : true,"glutenfree": true,"ketogenic": true, "pescetarian": true, "paleo": true},"meals":{"breakfast": true,"lunch": true,"dinner": true,"dessert": true,"snack": true}}`
        - returns: `{'message': 'Preferences successfully added'}`
- path `updateprefs/`
    - method: POST 
        - accepts: `{"prefs":{"calories_limit": 3, "intolorences": ["1","2"], "budget": 2},"diet":{"vegan": true,"vegetarian" : true,"glutenfree": true,"ketogenic": true, "pescetarian": true, "paleo": true},"meals":{"breakfast": true,"lunch": true,"dinner": true,"dessert": true,"snack": true}}`
        - returns: `{'message': 'Preferences successfully updated'}`

### Set meal history
- path `mealhistory/`
    - method: POST
        - accepts:`{"recipes": ['1', '2', '3']}`
        - returns: `{'message': 'Meal history successfully added'}`


<!-- to get back from meal history
     [   {date: "date", recipes: {
        breakfast: [{id:"", title: "", fave:""}], 
        lunch: [{id:"", title: "", fave:""}], 
        dinner: [{id:"", title: "", fave:""}], 
        dessert: [{id:"", title: "", fave:""}], 
        snacks: [{id:"", title: "fgdfgfd", fave:""}]}}, dateObj2, dateObj3
    ] -->
### Login
- path: `login/`
    - method: POST
        - accepts: `{"username": "billie","password": "Hello"}`
        - returns: `{'message': 'login successful'}`
### Logout
- path: `logout/`
    - method: GET
        - accepts: Null
        - returns: `{'message': 'User logged out'}`

