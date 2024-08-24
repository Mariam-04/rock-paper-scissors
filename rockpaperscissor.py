import random

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        return get_user_choice()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    
    return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")
