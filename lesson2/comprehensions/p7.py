def is_3_multiple(lst):
    return [num for num in lst
                if num % 3 == 0]

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


new = [is_3_multiple(sublist) for sublist in lst]

print(new)

print()

new = [[num for num in sublist
        if num % 3 == 0]
        for sublist in lst]

print(new)
