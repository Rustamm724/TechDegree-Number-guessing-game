#%%
import random
import statistics

def start_game():
    attempts_list = []

    while True:
        print("\nWelcome to the Number Guessing Game!")
        solution = 55
        attempts = 0

        while True:
            guess = input("Guess a number between 1 and 100: ")

            # Check if the input is a number
            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            attempts += 1

            if guess > solution:
                print("It's lower")
            elif guess < solution:
                print("It's higher")
            else:
                print("Got it!")
                attempts_list.append(attempts)  # Add attempts to attempts_list
                break

        # Display statistics
        print("It took you {} attempts to guess the correct number.".format(attempts))
        if attempts_list:
            print(f"Mean of attempts: {statistics.mean(attempts_list):.2f}")
            print(f"Median of attempts: {statistics.median(attempts_list)}")
            try:
                print(f"Mode of attempts: {statistics.mode(attempts_list)}")
            except statistics.StatisticsError:
                print("Mode of attempts: No mode, each value is unique.")

        # Prompt to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
start_game()

#%%
