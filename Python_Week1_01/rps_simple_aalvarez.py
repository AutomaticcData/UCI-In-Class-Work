# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 08:19:33 2018

@author: aalvarez

References: https://www.python.org/
            https://stackoverflow.com/
            https://www.w3schools.com/python/default.asp
    
"""

#'import the random lib
import random

#'do some research on what the random lib can do
#'https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
#'have the computer pre select a random value for rock,paper,scissors
# using the randint function from the random lib and use values from 1 to 3
computer_choice = random.randint(1,3)
computer_text = ""

#figure out what the computer chose and assign it to a variable
#1 = Rock, 2 = Paper, 3 = Scissors
if computer_choice == 1: 
    computer_text = "Rock"        
elif computer_choice == 2:
     computer_text = "Paper"
elif computer_choice == 3:
     computer_text = "Scissors"


#define the user input and give brief instructions to use numbers
input_choice = input("Use 1 for Rock, 2 for Paper or 3 for Scissors")
your_text = ""

#1 = Rock, 2 = Paper, 3 = Scissors
#string doesnt match integer value so convert and set a value
if input_choice == "1" : 
    your_choice = 1
    your_text = "Rock"
elif input_choice == "2":
    your_choice = 2
    your_text = "Paper"
elif input_choice == "3":
    your_choice = 3
    your_text = "Scissors"

    
#define a message for the outcome
outcome = ""
result_message = "" 

#rule out any tie scores
if (computer_choice == 1 and your_choice == 1) or (computer_choice == 2 and your_choice == 2) or (computer_choice == 3 and your_choice == 3):
    #tie
    outcome = "We have a tie!"
    
else:
    
    #computer picks Rock-----
    if computer_choice == 1 and your_choice == 2:
        #you pick paper
        outcome = "Congratulations. You win!"
    elif computer_choice == 1 and your_choice == 3:
        #you pick scissors
        outcome = "Sorry. You lose!"
        
    #computer picks Paper-----
    elif computer_choice == 2 and your_choice == 1:
        #you pick Rock
        outcome = "Sorry. You lose!"
    elif computer_choice == 2 and your_choice == 3:
        #you pick Scissors
        outcome = "Congratulations. You win!"

    #computer picks Scissors-----
    elif computer_choice == 3 and your_choice == 1:
        #you pick Rock
        outcome = "Congratulations. You win!"    
    elif computer_choice == 3 and your_choice == 2:
        #you pick Paper
        outcome = "Sorry. You lose!"



#make a nice message showing the results
result_message = "\n"
result_message += "You chose: (" + input_choice + ")" + your_text
result_message += " the computer chose: (" + str(computer_choice) + ")" + computer_text
result_message += "\n" + outcome

print(result_message)
