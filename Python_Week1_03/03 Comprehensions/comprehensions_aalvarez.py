"""
Created on Thu Aug  10 7:38:07 2018

@author: aalvarez
References: https://docs.python.org/3/library/stdtypes.html#str.title
            https://www.youtube.com/watch?v=1HlyKKiGg-4
            https://www.tutorialspoint.com/python/python_strings.htm

**********************
Manipulating CSV Files
In this activity, you will use list comprehensions to compose a wedding invitation to send to every name on your mailing list.

Instructions
Open the file called comprehensions.py.
Run the provided program. Note that nothing forces you to write the name "properly"—e.g., as "Jane" instead of "jAnE". You will use list comprehensions to fix this.

First, use list comprehensions to create a new list that contains the lowercase version of each of the names your user provided.
Then, use list comprehensions to create a new list that contains the title-cased versions of each of the names in your lower-cased list.

Bonuses
Instead of creating a lower-cased list and then a title-cased list, create the title-cased list in a single comprehension.
Hints
See the documentation for the title method.
"""


names = []
for _ in range(3):
    #name = input("Please enter the name of someone you know. ").lower()
    name = input("Please enter the name of someone you know. ")
    names.append(name)

#check to see how many values in the names list
#print(len(names))

#first create the for loop, then transition to list comprehension
#for x in range(len(names)):
#    print(names[x])
#**************************
lowercased = [names[x].lower() for x in range(len(names))]
lower_invitations = [f"Dear {item}, please come to the wedding this Saturday!" for item in lowercased]
for l_invitation in lower_invitations:
    print(l_invitation)
#**************************
#same for title cased
titlecased = [names[x].title() for x in range(len(names))]
title_invitations = [f"Dear {item}, please come to the wedding this Saturday!" for item in titlecased]
for t_invitation in title_invitations:
    print(t_invitation)

"""#***************************
squares = []
    for x in range(5):
        squares.append(x * x)
 ------------------------------
squares = [x * x for x in range(10)]
 ------------------------------
(values) = [ (expression) for (value) in (collection) ]
    ***Transforms into:***
(values) = []
for (value) in (collection):
    (values).append( (expression) )
________________________________

#using a list comprehension
#names = [input("Please enter the name of someone you know. ").lower() for i in range(2)]

#print(names)


#******************************
"""




"""
# @TODO: Use a list comprehension to create a list of lowercased names
#lowercased = ["YOUR CODE HERE!"]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
#titlecased = ["YOUR CODE HERE!"]

invitations = [f"Dear {name}, please come to the wedding this Saturday!" for name in names]
for invitation in invitations:
    print(invitation)
"""
