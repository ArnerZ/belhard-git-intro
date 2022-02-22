import json

data = {
    'age':41,
    'name': 'Stas',
    'children': [
        {
            'age': 10,
            'name': 'Masha'
        }
    ],
    'married': True,
    'city': None
}
serialized = json.dumps(data)
print(data)
deserialized = json.loads(serialized)
print(deserialized)
