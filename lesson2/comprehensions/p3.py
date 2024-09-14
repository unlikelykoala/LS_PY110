lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new = []

# for sublist in lst:
#     new.append(sorted(sublist, key=str))

new = [sorted(sublist, key=str) for sublist in lst]

print(new)
