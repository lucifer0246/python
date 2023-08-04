import random

random_number = random.randint(1,10)   # inclusive numbers 1-10    while working with range 10 is exclusive
guess = None

# while random_number != guess :
# 	guess =  int(input("What is your guess from numbers 1 - 10 ?: "))
# 	if guess > random_number :
# 		print("Too high, try again!")
# 		break
# 	elif guess < random_number :
# 	    print('Too low, try again!')
# 	    break
# 	else :
# 		print("YOU WON!!!")

# print(random_number)

while True :
    guess = int(input("Guess number between 1-9 : "))

    if guess < random_number:
        print("TOO low, TRY AGAIN!!")
    elif guess > random_number:
        print("TOO HIGH, TRY AGAIN!!")
    else:
        print("YOU WIN!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)  # numbers 1 - 10
            guess = None
        else :
            print("Thank you for playing!")
	    