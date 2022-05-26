import random

print("Number Guessing Game")
print("Guess a number between 1 and 9")
guess = input("Enter your guess")

# Generating a random number between 1 and 9
number = random.randrange(1,9)

# While loop to count the number of chances
chances = 5
while chances < 5:
    break

# Compare the user entered number with the number to be guessed
if guess == number:
    # if number entered by user is same as the generated
    # number by randint function then break from loop using loop
    # control statment "break"
    print("Congratulation YOU WON! ! !")


if not chances < 5:
    print("YOU LOSE!!! The number is", number)
