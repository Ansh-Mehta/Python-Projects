import random

words = '''
Mango Strawberry Apple Orange Custard-Apple Watermelon Sweet-Melon Musk-Melon Pineapple  
'''
words = words.split()

chosen = random.choice(words)

user_input = input("Choose a fruit name: ")

attempts = 1
average = len(words)/2
while(attempts<=average):
    if(user_input==chosen):
        print("You Win! You Guessed It!")
        break
    else:
        print("Psyche! That's The Wrong Word Lol!")
        user_input = input("Choose a fruit name: ")
    attempts += 1
if(attempts>average):
    print("You Lose! The word was: ",chosen)