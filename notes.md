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
        - accepts: `{"prefs":{"calories_limit": 3, "intolorences": ["dairy","egg"], "budget": 2},"diet":{"vegan": true,"vegetarian" : true,"glutenfree": true,"ketogenic": true, "pescetarian": true, "paleo": true},"meals":{"breakfast": true,"lunch": true,"dinner": true,"dessert": true,"snack": true}}`
        - returns: `{'message': 'Preferences successfully added'}`
- path: `prefs/`
    - method: PATCH 
        - accepts: `{"prefs":{"calories_limit": 3, "intolorences": ["1","2"], "budget": 2},"diet":{"vegan": true,"vegetarian" : true,"glutenfree": true,"ketogenic": true, "pescetarian": true, "paleo": true},"meals":{"breakfast": true,"lunch": true,"dinner": true,"dessert": true,"snack": true}}`
        - returns: `{'message': 'Preferences successfully updated'}`
        <!-- add budget for each meals -->
    - method: GET
        - accepts: Null
        - returns: `{'calories_limit': 3, 'intolorences': ['1', '2'], 'budget': 2}`
        <!-- return meal prefs as well  -->
{'breakfast':{'budget':2, "calories':2},'lunch':{'budget':2, "calories':2},'dinner':{'budget':2, "calories':2}, 'dessert':{'budget':2, "calories':2},'snack':{'budget':2, "calories':2}}

### Meal History
- path `mealhistory/`
    - method: POST
        - accepts:`{"recipes": ["1", "2", "3"]}`
        - returns: `{'message': 'Meal history successfully added'}`
    - method GET
        - accepts: Null
        - returns: `{'recipes': {'breakfast': [{'id': '', 'title': '', 'fave': ''}], 'lunch': [{'id': '', 'title': '', 'fave': ''}], 'dinner': [{'id': '', 'title': '', 'fave': ''}], 'dessert': [{'id': '', 'title': '', 'fave': ''}], 'snacks': [{'id': '', 'title': 'fgdfgfd', 'fave': ''}]}, 'date': datetime.datetime(2022, 7, 15, 16, 43, 29, 504997, tzinfo=datetime.timezone.utc)}`
        <!-- datetime to accept a string -->

### Email
- path `email/`
    - method: POST
        - accepts: `{"message":"hi this is from the web!"}`
        - returns: `{'message': 'email sent successfully'}`

