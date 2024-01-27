import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # Get user and computer choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
        print(result)

        # Update scores
        if "win" in result.lower():
            user_score += 1
        elif "lose" in result.lower():
            computer_score += 1

        # Display scores
        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
