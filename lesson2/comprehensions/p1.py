munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total = 0

for character, info in munsters.items():
    if info['gender'] == 'male':
        total += info['age']

print(total)

print()

ages = [info['age'] for info in munsters.values()
        if info['gender'] == 'male']

total = sum(ages)
print(total)
