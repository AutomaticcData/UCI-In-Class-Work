"""
Created on Thu Aug  10 1:35:19 2018


@author: aalvarez

References: in code below

******* BONUS **************
Bonus
Try the following again but this time using cereal_bonus.csv, which does not include a header.
"""

#import the os Module
import os

#import the csv csvreader
import csv

#csv is currently in the same directory as the python script, using blank parameters as such
csv_path = os.path.join('','','cereal_bonus.csv')

#open the file, using the delimiter as the csv file
#another UnicodeDecodeError, adding encoding parameter to solve this jibberish 'ï»¿name'
#unfortunately utf8 did not work and so research ensued
#https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
with open(csv_path, newline='', encoding='utf-8-sig') as csv_file:

    #assign the contents of the file to a variable called csvreader
    csv_reader = csv.reader(csv_file, delimiter=',')

    #assign the header to the csv_header variable, we are using this to skip the entire

    #first row which contains the header
    #BONUS *** OMIT THE CSV HEADER **********************
    #csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        #print(row)
        #open the file and see which column contains the fiber values
        #convert col values to Integers
        #https://stackoverflow.com/questions/1094717/convert-a-string-to-integer-with-decimal-in-python
        num_decimal = int(float(str(row[7])))
        if num_decimal>= 5:
            print(num_decimal)
