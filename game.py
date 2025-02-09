
#Let's Start
import random

number_to_guess = random.randint(1, 10)
number_of_attempts = 0

while True:
    user_guess = int(input("Enter your guess: "))
    number_of_attempts += 1
    
    if user_guess < number_to_guess:
        print("Too low! Try again.")

    elif user_guess > number_to_guess:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")
        break
