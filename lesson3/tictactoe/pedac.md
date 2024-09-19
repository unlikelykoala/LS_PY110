High-level pseudocode:
    1. Display the initial empty 3x3 board.
    2. Ask the user to mark a square.
    3. Computer marks a square.
    4. Display the updated board state.
    5. If it's a winning board, display the winner.
    6. If the board is full, display tie.
    7. If neither player won and the board is not full, go to #2
    8. Play again?
    9. If yes, go to #1
    10. Goodbye!

    keep score:
    rules:
    - no global variables
    - possible: global constant for number of games to win match
    algorithm:
    1. initialize the win count for player and computer
        - tell the player it's best of 3
    2. increment each count depending on who wins
    3. If someone wins twice, end of the match
        - ask player if they're up for another match
        - reset scores to 0
    
    
    join_or function:
    input: sequence, string (delimiter, default = ', '), string (conjunction, default = 'or')
    output: string (with delimiter and final conjunction)

    rules:
    - each item should be separated by the delimiter
    - the final delimiter should be followed by a conjunction 
    - default delimiter = ', '
    - default conjunction - 'or'

    edge cases:
    - if empty list- return empty string
    - if 1 ele, return string of ele
    - if 2 ele, return with conjunction but without ele

    
    
    data structure:
    - list
    - string

    algorithm:
    1. Convert all elements to strings because str.join won't work otherwise
    2. Combine all elements into a string EXCEPT for the last one
    3. Concatenate the new string with the last element prepended with the delimiter and conjunction
    4. return the new string
