import json

# Liste de tuples
data = [
    ('ceci est un test', 'user1', 1000.0, 0, 'pending'),
    ('this is a test', 'user3', 1000.0, 0, 'pending'),
    ('another test', 'user11', 1000.0, 0, 'pending')
]

# Transformation en liste de dictionnaires
json_data = [
    {
        'content': item[0],
        'owner': item[1],
        'price': item[2],
        'status': item[4]
    } for item in data
]

# Conversion en JSON
json_output = json.dumps(json_data, indent=4)

print(json_output)
