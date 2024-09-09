input: list of strings
output: new list of strings (don't mutate original list)

explicit rules:
    - sort based on number of adjacent consonants
    - if 2 strings haver same number, keep their original order
    - consonants are adjacent if next to each other in same word or if a space between them in adjacent words

implicit rules:
    - don't mutate original list
    - strings may contain more than 1 word

Questions:
    - Should order be ascending or descending?
        - descending order
    - Does this include non-English characters? 
        - If so, where can I get a list of international consonants?
    - what if there is more than one space between them?
    - what about other symbols, like hyphens?
    - y?
    - how to handle case?
    can strings be empty?

Data structures:
    - lists (input and output)
    - list of tuples [(adj_consonants, string), ...]?"
      OR
      dict: {'string': adj_consonants, ...}

Algorithm:
    1. GET number of adjacent consonants for each string in input
        A: Create empty dict (string = key, count = value)
        B: Iterate through input list.
        C: Count num of adjacent consonants for each string
            - remove spaces
            - initialize max_count to 0
            - Iterate through string
            - If current char AND next char are consonants, increment counter
            - return counter
        D: Add string and counter to dict
    2. SORT input list based on number of adjacent consonants (don't mutate)
        A: create empty list 
        B: Iterate through strings in original list 
        C: Create a tuple (# of adj. cons., string)
            1. How to calculate?
    3. RETURN sorted copied list
