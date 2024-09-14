lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new = [{key: value+1} for dictionary in lst
       for key, value in dictionary.items()]

print(new)
