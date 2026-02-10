import random

hscore = 0
cscore = 0

while True:
    print(f"Current scores - {hscore}, computer - {cscore}")

    user = int(input("1 for stone, 2 for paper, 3 for scissor choose:- "))

    com = random.randint(1,3)

    if user == 1 and com == 3:
        hscore += 1
        print("You won the round \n")
    elif user == 3 and com == 2:
        hscore += 1
        print("You won the round \n")
    elif user == 2 and com == 1:
        hscore += 1
        print("You won the round \n")
    elif user == com:
        print("Draw \n")
    else:
        cscore += 1
        print("Computer won the round \n")
        

    if hscore == 5:
        print("You won the game \n")
        break
    elif cscore == 5:
        print("Computer won the game \n")
        break