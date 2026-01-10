import random

def game_play(attempts):
    number = random.randint(1, 101)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            return "Your guess is correct."
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        attempts -= 1
    return f"You have {attempts} attempts remaining to guess the number. You lose."

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game_mode = input("Choose a difficulty level. Type \'easy\' or \'hard\': ".lower())
attempts = 0
if game_mode == "easy":
    attempts = 10
elif game_mode == "hard":
    attempts = 5
else:
    print("Invalid difficulty. Type \'easy\' or \'hard\'.")

if attempts > 0:
    print(game_play(attempts))