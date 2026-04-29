import random

# 1. The computer picks a secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
guess = 0

print("--- Welcome to the Number Guessing Game! ---")
print("I'm thinking of a number between 1 and 100.")

# 2. Use a while loop to keep asking until the user gets it right
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1 # Count this guess
    
    # 3. Check if the guess is too high, too low, or correct
    if guess > secret_number:
        print("Lower! Try again.")
    elif guess < secret_number:
        print("Higher! Try again.")
    else:
        print(f"🎉 Correct! You found it in {attempts} attempts.")

print("Thanks for playing!")