import random

def get_user_choice():
    while True:
        user_choice = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return "You won!"
    else:
        return "You lost!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(['r', 'p', 's'])
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
