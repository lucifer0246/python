from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("Enter youe choice :").lower()

random_num = randint(0, 2)

if (random_num == 0):
    computer = "rock"
elif (random_num == 1):
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays: {computer}")

if player == computer:
    print("IT'S TIE!!")
elif player < computer:
    print("COMPUTER WINS!!")
else :
    print("PLAYER WINS!!")
