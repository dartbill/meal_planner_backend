# Path 

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

        user_id=pref_information['user_id'], diet_id=pref_information['diet_id'], meals_id=pref_information['meals_id'],
        calores_limit=pref_information['calories_limit'], intolorences=pref_information[
            'intolorences'], budget=pref_information['budget']
