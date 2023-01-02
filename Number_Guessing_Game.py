import random
lower = int(input("Enter the lower bound: ")) 
upper = int(input("Enter the upper bound: "))

#taking the range from which random module will select a number

chosen = random.randint(lower, upper)

average = (upper + lower)/2
attempts = 1

#the loop will run till attempts becomes equal to average

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
