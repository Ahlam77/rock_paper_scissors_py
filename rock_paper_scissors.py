# Start the game
# Ask the player to make a move (r, p, s)
# PC would select a move radomly
# PC == Player -> Tie
# (Player == P and PC == Rock) or (Player == R and PC == Scissors) or (Player == Scissors and PC == Paper)
## User won / You won
# Any other case
## PC won / You lose

import random

# Start the game
# Ask the player to make a move (r, p, s)
user_choice = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors\n")

# PC selects a move randomly
pc_choice = random.choice(['r', 'p', 's'])

print("User played: " + user_choice)
print("PC played: " + pc_choice)

# Determine the winner
if user_choice == pc_choice:
    print("It's a tie!")
elif (user_choice == 'p' and pc_choice == 'r') or (user_choice == 'r' and pc_choice == 's') or (user_choice == 's' and pc_choice == 'p'):
    print("You won!")
else:
    print("PC won. You lose!")
