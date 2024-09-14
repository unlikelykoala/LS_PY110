def sum_of_odds(sublist):
    odds = [num for num in sublist if num % 2 == 1]
    return sum(odds)

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

print(sorted(lst, key=sum_of_odds))
