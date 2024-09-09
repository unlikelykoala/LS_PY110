CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'k', 
              'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def sort_by_consonant_count(lst):
    sorted_list = lst.copy()
    sorted_list.sort(key=adj_consonant_count, reverse=True)
    return sorted_list

def adj_consonant_count(str1):
    nospace_string = str1.replace(' ', '')
    adjacent_count = 0
    adj_cons_str = ''
    for char in nospace_string:
        if char in CONSONANTS:
            adj_cons_str += char
        elif len(adj_cons_str) > adjacent_count and len(adj_cons_str) > 1:
            adjacent_count = len(adj_cons_str)
            
            adj_cons_str = ''
    
    if len(adj_cons_str) > adjacent_count and len(adj_cons_str) > 1:
        adjacent_count = len(adj_cons_str)
    
    return adjacent_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
