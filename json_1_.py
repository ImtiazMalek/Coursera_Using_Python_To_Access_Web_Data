import json
data = '''[
{"id" : "16101068","name": "imtiaz", "phone":{"type":"intl","number":"01988148871"}} ,
{"id" : "16301153","name" : "nanji", "phone":{"type":"intl","number":"01718098691"}}
]'''
tree = json.loads(data)
print(tree)
print(type(tree))
for item in tree:
    print('Name:', item['name'])
    print('Number:',item['phone']['number'])
    print('id:', item['id'])
    print()