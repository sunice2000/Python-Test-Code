'''

                            Simple Python Bot
                       Created by Crystal Richards
         For the purpose of demonstrating my coding style in Python

'''
import random
import datetime
from pytz import timezone
import pytz
mst = timezone('MST')

#function for printing out the appropriate question to ask the user, and obtaining an answer
def question(q):
    if(q == 0):
        answer = input("Would you like to know the time? ")
    elif(q == 1):
        answer = input("Would you like to know the date? ")
    elif(q == 2):
        answer = input("Would you like to know the weather? ")
    elif(q == 3):
        answer = input("Would you like to know the current lucky numbers? ")
    else:
	    answer = input("Would you like to know what your name is backwards? ")

    return answer
    
#function for printing the appropriate answer to a question answered 'yes'
def answers(q, n):
    if(q == 0):
        print(datetime.datetime.now(mst).time())
    elif(q == 1):
        print(datetime.datetime.now(mst).date())
    elif(q == 2):
        print("Low of 8, high of 12. 60% chance of precipitation.")
    elif(q == 3):
        num = []
        for i in range(6):
            num.append(random.randint(1, 49))
        print(num)
    else:
        print(n[::-1].lower().capitalize())

#Prompt user for name
name = input("Enter your name to start: ")
#Check for valid name: letters only and more than one letter long
while True:
    if(name.isalpha() and len(name) > 1):
        break
    else:
        name = input("That can't be your name, enter your name:")

name = name.capitalize()
#Begin Chat with user, explain how to answer before prompting questions
print("Hello, %s. It's a pleasure meeting you. \nYou can respond to me using y/n. At any time you can type 'exit' if you want to end our chat." % name)

#for yes: answer appropriately, for no: skip to next prompt, for exit code: end conversation, all other answers are met with a response restating the appropriate answers.
for q in range (0,5):
    answer = question(q)
    if(answer.lower().startswith('y')):
        answers(q, name)
    elif(answer.lower().startswith('n')):
        continue
    elif(answer.lower().find('exit') != -1):
        break
    else:
        print("It was a yes or no question.")
#say goodbye to user and exit program
print("\nWell it was nice meeting you %s, but I'm afraid that's all I've been programmed to do. Bye." % name)
    
