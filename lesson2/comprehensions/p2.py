lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new = []

# for sublist in lst:
#     new.append(sorted(sublist))

# print(new)

new = [sorted(sublist) for sublist in lst]

print(new)
