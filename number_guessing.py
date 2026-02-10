import random

num = random.randint(1,100)

tries = 0


while True:

    guessed = int(input("Guess the number between 1 - 100: "))
    tries += 1
    if guessed == num:
        print(f"Congratulation you guessed the number in {tries} tries")
        break
    elif guessed > num:
        print("Sorry you need to go lower\n")
    elif guessed < num:
        print("Sorry you need to go higher\n")