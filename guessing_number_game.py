import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎲 Guess the number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < secret_number:
        print("🔼 Too low, try again.")
    else:
        print("🔽 Too high, try again.")
import random