# This is a guess the number game.
import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Player has 6 attempts to guess the number
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('> '))  # Get player's guess and convert to integer

    # Provide feedback on the guess
    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break  # Exit loop if guess is correct

# Check if player guessed correctly and provide appropriate message
if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))