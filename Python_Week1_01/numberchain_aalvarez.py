# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:47:53 2018

@author: antho
"""

#define a function so we can call it again if we have to
def numCounter( strTimes ):

  #check the length of the string to only be 1 digit and then check for only number values in the entry
  #'https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
  if (strTimes.isdigit()==False or int(strTimes) > 100):
        
      #exit the game and display a friendly message
      #https://docs.python.org/2/library/exceptions.html#exceptions.SystemExit
      #https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/19747562
    print(str(strTimes) + " is not valid.\nPlease enter a numeric value less than 100 next time.\nThanks for playing! XD")
    SystemExit()    
  
  else: 
      num_value = int(strTimes)
      #print(num_value)
      i = 1  
      while i < (num_value + 1):
          print(i)
          i += 1
          
          if i == num_value+1:
              print("All done")
              input_continue = input("Would you like to continue? [y] for YES, [n] for No\n")
              #slicing article --> https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
              #print(input_continue[:1])
              
              print("You chose " + str(input_continue[:1]) )
                            
              user_choice = input_continue[:1]
              if user_choice == "n":
                      print("Maybe next time.\nThanks for playing! XD")
                      SystemExit()
              elif user_choice =="y":
                      print(", Here we go: \n")
                      #recursive call to the function here
                      numCounter(strTimes)
              else:
                      print("Maybe next time.\nThanks for playing! XD")
                      SystemExit()
                  
        
def beginCount():
    #define a function to that calls the main process
    input_value = input("How many numbers would you like? (1 - 100)")
    numCounter(input_value)
    
def Main():
    #initiate the main function call
    beginCount()
  
    
    
    
Main()