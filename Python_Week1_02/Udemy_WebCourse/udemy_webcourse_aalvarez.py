"""
Created on Thu Aug  9 11:58:55 2018


@author: aalvarez

References: https://docs.python.org/3/tutorial/datastructures.html
            https://stackoverflow.com/
            https://www.w3schools.com/python/python_tuples.asp
            https://www.pythonforbeginners.com/os/pythons-os-module

"""

"""
Udemy - Web Course Breakdown

Instructions
Create a Python application that reads the data on Udemy Web Development offerings.
Then store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists.
Then zip these lists together into a single tuple.
Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your csv.

Notes:
Windows user may get an UnicodeDecodeError, to avoid this file pass in encoding="utf8" as an additional parameter when reading in the file.
As, with many datasets, the file does not include the header line. Use the below as a guide on the columns: "id,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime"

Bonus
Find the percent of subscribers that have also left a review on the course. Include this in your final output.
Parse the string associated with course length, such that we store it as an integer instead of a string. (i.e. "4 hours" should be converted to 4).
"""

#import the os Module
import os

#import the csv csvreader
import csv

#csv is currently in the same directory as the python script, using blank parameters as such
csvpath = os.path.join('', '', 'web_starter.csv')

#i opened the file and found the delimiter to be a comma. adding this to a variable
#creating this just in case i want to use an alternate delimiter such as a pipe:| or tab
the_delimiter = ","

#open the file, using the delimiter as the csv file
#i encountered a UnicodeDecodeError, adding encoding parameter to solve this jibberish 'ï»¿28295'
with open(csvpath, newline='', encoding="utf8") as csvfile:

    #assign the contents of the file to a variable called csvreader
    csvreader = csv.reader(csvfile, delimiter=the_delimiter)

    #print out the header
    #print(csvreader)

    #assign the header to the csv_header, this would be skipped if there was no header in the file
    ##csv_header = next(csvreader)
    ##print(f"CSV Header: {csv_header}")

    #since there is no header i will create one using the notes provided.
    #id	title	url	isPaid	price	numSubscribers	numReviews	numPublishedLectures	instructionalLevel	contentInfo	publishedTime
    #csv_header = ["id", "title", "url", "isPaid", "price", "numSubscribers", "numReviews", "numPublishedLectures", "instructionalLevel", "contentInfo", "publishedTime"]
    #get the number of items in the header list --> len(csv_header)

    #new csv Header
    #csv_header = ["Title","Price","Subscriber_Count","Number_Of_Reviews","Course_Length"]
    #bonus csv Header
    csv_header = ["Title","Price","Subscriber_Count","Number_Of_Reviews","Course_Length","Percent_Of_Subscribers_Reviews"]

    #print out the header for testing purposes****
    #print(csv_header)
    #print(csv_header[1])
    #*********************************************

    #create lists to store Title, Price, Subscriber Count, Number of Reviews, and Course Length
    #Title = csv_header[1], Price = csv_header[4], SubCount = csv_header[5], NumReview = csv_header[6], CourseLength = csv_header[9]
    #this was derived by directly looking at the file
    col_title = []
    col_price = []
    col_subcount = []
    col_numreview = []
    col_courselen = []

    #bonus contents
    col_percentleftreview = []

    #iterate through each row in the file, After the header
    for row in csvreader:
        #assign the slice value of the lists to its corresponding list
        col_title.append(row[1])
        col_price.append(row[4])
        col_subcount.append(row[5])
        col_numreview.append(row[6])

        #updating for bonus content
        #col_courselen.append(row[9])
        parse_courselen = str(row[9]).split(" ")
        col_courselen.append(parse_courselen[0])

        """Bonus
        Find the percent of subscribers that have also left a review on the course. Include this in your final output.
        Parse the string associated with course length, such that we store it as an integer instead of a string.
        (i.e. "4 hours" should be converted to 4).
        """
        #for the first part we divide the number of reviews which is Row[6]
        #by the number of subscribers Row[5] and multiply 100, then round 2 decimal places

        num_revs = row[6]
        num_subs = row[5]
        percent_subs = 0.00


        if (int(num_revs) < 1) or (int(num_subs) < 1):
            percent_subs = 0
            col_percentleftreview.append(percent_subs)
        else:
            percent_subs = round((int(num_revs)/int(num_subs) * 100),2)
            col_percentleftreview.append(percent_subs)

        #col_percentleftreview.append(str(5))

        """
            End Bonus
        """

        #strCurrent = str(row[0])
        #print(strCurrent)
        #print(csv_header[0] + " - " + strCurrent + " - " + str(len(str(row[0]))))

        # ***IF I wanted to loop through all of the items to do some formatting, searching, calculations *****
        #in the end, all of the lists should have the exact same number of rows
        #therefore if we iterate through one of the lists, it should apply to all of the Lists
        #print(len(col_title)) --just checking the number of rows, currently its 1200

        #for item in col_title:
            #print(item)
        #*****************************************************************************************************

    #zip all of the above lists into tuples
    #csv_body = zip(col_title,col_price,col_subcount,col_numreview,col_courselen)

    #updating for bonus content
    csv_body = zip(col_title,col_price,col_subcount,col_numreview,col_courselen,col_percentleftreview)

    #set a variable for the file path to save the csv
    csv_file = os.path.join("udemy_output_aalvarez.csv")

    # open the output file, create a header row, and then write the zipped object to the csv
    #open the csv file created and prepare for writing data
    with open(csv_file, "w", newline="") as csvoutputfile:
        writer = csv.writer(csvoutputfile)

        #first write the header defined earlier
        writer.writerow(csv_header[:])

        #lastly write the body of the document containing our data
        writer.writerows(csv_body)

#added a closing input to prevent script from exiting automatically in python shell
#https://stackoverflow.com/questions/3591807/how-can-i-stop-python-exe-from-closing-immediately-after-i-get-an-output
k = input("Press a key to exit")
