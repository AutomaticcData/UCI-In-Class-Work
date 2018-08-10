"""
Created on Fri Aug  10 3:20:44 2018


@author: aalvarez

References: in code below
#http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

Info in Dictionaries
Instructions
Create a dictionary to store the following:
Your name
Your age
A list of a few of your hobbies
A dictionary of a few times you wake up during the week

Print out your name, how many hobbies you have and a time you get up during the week.
"""
#2 ways to create a list of hobbies
#my_hobbies = ["Running","Gaming","Movies"]

#define a list and add hobbies to it
my_hobbies = []
my_hobbies.append("Running")
my_hobbies.append("Gaming")
my_hobbies.append("Reading")
my_hobbies.append("Movies")

#create a dictionary object to hold my information
#also add the list as a value to the dictionary
my_info = {"Name":"Anthony","Age":21,"Hobbies":my_hobbies}
#print(my_info["Hobbies"])

for key in my_info:
    #print(my_info[key])

    #lots of trial and error to get this string to print out the way i wanted
    out_msg = "Hello my name is " + str(my_info["Name"]) + ".\n"
    out_msg += "I am " + str(my_info["Age"]) + " and over.\n"
    out_msg += "Some of my hobbies are "

    my_hobbies = my_info["Hobbies"]
#for i in range(my_info["Hobbies"])
#for row in len(my_info["Hobbies"])
#print(my_hobbies[2])
#print(len(my_info["Hobbies"]))

#for this block of code, all i want to do is check to add a comma to each item
#if its the last item then substitute the word and for the comma

#for every list item in my_hobbies, add a comma..or not
for i in range(len(my_hobbies)):
    if i+1 == len(my_hobbies):
        out_msg = out_msg[0:-1] + " and " + my_hobbies[i] + "."
        #print(out_msg[:])
        #out_msg += " and " + my_hobbies[i] + "."
        # + " = " + str(i+1) + " | " + str(len(my_hobbies))
    else:
        out_msg += my_hobbies[i] + ","
        # + " = " + str(i+1) + " | " + str(len(my_hobbies))

print(out_msg)

#print(len(my_hobbies))
#print(range(len(my_hobbies)))

"""
#https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/9533754?start=0
Here are more operations you can do with dictionaries
Let's say we have the following dictionary:
>>> person97 = {"name":"Jack", "surname":"Smith", "age":"29"}
Removing pair "name":"Jack"
>>> person97.pop("name")
'Jack'
>>> person97
{'surname': 'Smith', 'age': '29'}

Adding new pair "name":"Jack"
>>> person97["name"] = "Jack"
>>> person97
{'surname': 'Smith', 'age': '29', 'name': 'Jack'}

Changing an existing value
>>> person97["age"] = 30
>>> person97
{'surname': 'Smith', 'age': 30, 'name': 'Jack'}

Mapping two lists to a dictionary:
>>> keys = ["a", "b", "c"]
>>> values = [1, 2, 3]
>>> mydict = dict(zip(keys, values))
>>> mydict
{'a': 1, 'b': 2, 'c': 3}
"""
