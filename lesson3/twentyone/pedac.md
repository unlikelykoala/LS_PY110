input:
output:

Goal: get as close to 21 as possible without going over (bust)

Setup:
- 2 players: dealer and player
- both get dealt a hand of 2 cards
- player can see their two cards, but only one of dealer's cards

Card values:
- 2-10 are their number value
- Jack/Queen/King = 10
- Ace = 1 or 11
    - 11 if it doesn't make total go over 21, else 2
    - edge case: getting multiple aces

Questions:
- can an ace change value from 11 to 1 as you draw more cards?

Player turn:
- choose to hit (get another card) or stay
- turn is over when player either stays or busts
- bust means the game is over and the dealer won

Dealer's turn:
- when player stays, dealer's turn
- strict rule for deciding ot hit or stay: hit until total is at least 17
- if dealer busts, player wins

Compare cards:
- after both player and dealer stay, they compare the total value of the cards to see who has the highest value

Data structures:
- list of tuples for deck of cards (suit, num/face)
    - init using 2 tuples, one for suits and one for nums/faces

Algorithm:
1. Initialize the deck
    - list of suits and list of nums/faces
    - combine into list of tuples
    - note that suit doesn't actually matter except for game visuals. only the number of each value is important
    - how to handle 11
    -[(2, 'clubs', 2), ('jack', 'hearts', 10)....] (face, suit, value)
2. Initialize scoreboard
3. Instructions
3. Deal player cards
4. Deal dealer cards
5. Reveal 1 dealer card to player
6. Player Turn
    - Hit or stay
    - if bust, player loses
7. Dealer turn
    - hit until at least 17, then stay
    - if bust, player wins
8. Compare hands (if no busts)
    - highest number is winner
9. Record scores
10. Play again?

Player turn algorithm:
1. Show the player his hand:
    A: Calculate the point total for non-ace cards
    B: Calculate ace value based on overall total
        - Multiple aces how to handle
    C: Add ace value to get full total
    D: If over 21, bust! Dealer wins
    E: Display each card along with its face and number of points
        - make a note about how the ace value could change
    F: Display full point total
2. Show the player one card from the dealer's hand
3. Ask player if he wants to hit or stay
    A: If hit, repeat step 1 with new hand
    B: If stay, move to dealer's turn

Dealer's turn algorithm:
1. Calculate the point total for non-ace cards
2. Calculate ace value based on overall total
3. Add ace value to get full total
    - If over 21, bust! Dealer wins
4. If under 17 points, hit
    - repeat steps 1-4
5. If over 17, stay.
    - Compare cards

Compare cards algorithm:
1. Display all cards and point totals for both players
2. Decide winner based on who has highest score
3. Update scoreboard
4. Display scoreboard
5. If less than necesary wins, next round
6. If necessary wins reached, end of match.
    - play again?

Using player turn and dealer turn to decide winner and display results:
1. player turn:
    - player busts, or decides to hit or stay
    - if bust


NOTE: I need to fix the ace_total algorith
- if aces_only_total + no_aces_total is more than 21, then i need to reduce at least 1 ace
