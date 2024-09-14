def all_even(lst):
    return all([ele % 2 == 0 for ele in lst]) 

def all_true(dictionary):
    return all([all_even(value) for value in dictionary.values()])

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

new = [dictionary for dictionary in lst
       if all_true(dictionary)]

print(new)
