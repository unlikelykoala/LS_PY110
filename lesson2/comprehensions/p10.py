'''
output: string
    - 8-4-4-4-12 pattern of hex digits
'''
from random import randrange
hex_range = list(range(10)) + ['a', 'b', 'c', 'd', 'e', 'f']

eight_str = ''.join([str(hex_range[randrange(16)]) for i in range(9)])

four_str1 = ''.join([str(hex_range[randrange(16)]) for i in range(5)])

four_str2 = ''.join([str(hex_range[randrange(16)]) for i in range(5)])

four_str3 = ''.join([str(hex_range[randrange(16)]) for i in range(5)])

four_str4 = ''.join([str(hex_range[randrange(16)]) for i in range(5)])

twelve_str = ''.join([str(hex_range[randrange(16)]) for i in range(13)])

print(f'{eight_str}-{four_str1}-{four_str2}-{four_str3}-{four_str4}-{twelve_str}')
