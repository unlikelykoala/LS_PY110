dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

VOWELS = 'aeiou'

def get_vowels(dictionary):
    return [letter for lst in dictionary.values()
            for word in lst
            for letter in word
            if letter in VOWELS]

list_of_vowels = get_vowels(dict1)

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
