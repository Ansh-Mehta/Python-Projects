import random
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

chosen = random.randint(lower, upper)

average = (upper + lower)/2
attempts = 1
while(attempts<=average):
    number = int(input("Enter Your Guess: "))
    if(number<chosen):
        print("You guessed too small")
    elif(number>chosen):
        print("You guessed too big")
    elif(number==chosen):
        print("You Guessed It!")
        break
    attempts += 1
