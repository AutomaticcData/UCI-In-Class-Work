"""
Created on Thu Aug  10 9:35:33 2018

@author: aalvarez

Functions
In this activity, you will write a function to compute the arithmetic mean (average) for a list of numbers.

Instructions
Write a function called average that accepts a list of numbers.
The function average should return the arithmetic mean (average) for a list of numbers.
Test your function by calling it with different values and printing the results.

Hints
Arithmetic Mean (Average)

do some research on functions
https://www.tutorialspoint.com/python/python_functions.htm
def mytest(mylist):
    print(mylist)

mycolors = ["red","blue","green"]
mytest(mycolors)

"""

# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))

#*** define the function here ********
def my_average(num_list):
    #the number to divide by
    num_divisor = len(num_list)

    #create a variable to hold the sum of numbers
    num_total = 0.00

    #create a variable for the mean(average)
    num_mean = 0

    #iterate through the list and get a sum of the numbers
    for x in range(len(num_list)):
        #print(num_list[x])
        num_total += num_list[x]
    num_mean = (num_total/num_divisor)

    return num_mean
    #testing **********
    #print(num_mean)
    #print(num_total)
    #print(num_divisor)
    #print(num_list)
    #******************

#****end function *******************

#Create a number list prompt to return the mean
#number_list = []
#for i in range(3):
#    numbers = input("Please enter a number..")
#    number_list.append(int(numbers))
#i just realized i can change the for loop above to comprehension list
#hooray!
number_list = [int(input("Please enter a number..")) for i in range(3)]

#call the average function and return a value for the mean
#we could have assigned a variable to hold the return value of the function
print("The mean of the list of numbers:")
print(number_list)
print("is: " + str(my_average(number_list)))
