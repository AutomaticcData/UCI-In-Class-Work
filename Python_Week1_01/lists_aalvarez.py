"""
Created on Wed Aug  8 08:39:13 2018

@author: aalvarez
References: https://www.python.org/
Purpose:    learning lists and their functions
"""
#you can use help() for help on an object
#ie. help(len) will give you help info on the length item
#also, dir(__builtins__) will display the listing of all built in functions etc.


address = ["Flat Floor Street", 18, "New York"]

#access an item via index
print(address[1])

#check the type of the item
print(type(address[1]))

#if its an integer you can do math calcs with list item
print(address[1] + 20)

# --- Positive Indexing ---
#lists have an indexing system that start at 0

# --- Negative Indexing ---
#also lists have another indexing system that starts at -1
#good for long lists if you want to get the last item or the like.

# --- Slicing ---
#you can also access slices of the lists

#**upper bound exclusive
#returns only items up to the upper bound. this means that if you want the first 2
#items, you would use from 0 to 2, this returns the first and second item.
print(address[0:2])

#another way to do the same as above
print(address[:2])

#also slicing only works from left to right
#you can not go from right to left
print(address[-1:-2])

#$if you wanted to get 18 to New York, you would start at -2 up to the right most
print(address[-2:])

#you can start at set slices of a list using slicing syntax
print(address[1:])
#return all
print(address[:])
