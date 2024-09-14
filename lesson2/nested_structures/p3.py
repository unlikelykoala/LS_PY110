munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

print(munsters['Herman']['age'])
for character in munsters:
    print(f"{character} is a {munsters[character]['age']}-year-old {munsters[character]['gender']}.")

print()

for character, info in munsters.items():
     print(f'{character} is a {info['age']}-year-old {info['gender']}.')
