"""
# House Of Pies
## Instructions
# Part 1
* Create an order form that will display a list of pies to the user in the following way:
```
Welcome to the House of Pies! Here are our pies:
---------------------------------------------------------------------
(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
```
* Then prompt the user to select which pie they'd like to order via number.
* Immediately after, follow the order with `Great! We'll have that <PIE NAME> right out for you.` and then ask if they would like to make another order. If so, repeat the process.
* Once the user is done purchasing pies, print the total number of pies ordered.
# Part 2 (Very Challenging!)
* Modify the application once again, this time conclude the user's purchases by listing out the total pie count broken by _each_ pie.
"""
#add a welcome message, then get fancy
#https://asciiart.website//index.php?art=objects/buildings
welcome_msg = "\n\n________Welcome to the House of Pies!_______________\n"
welcome_msg += "                          (     \n"
welcome_msg += "                       (   )  )\n"
welcome_msg += "                        )  ( )\n"
welcome_msg += "                        .....\n"
welcome_msg += "                     .:::::::::.\n"
welcome_msg += "                     ~\_______/~\n"
welcome_msg += "************  Here are our pies: **********************"
welcome_msg += "\n"

#start the pie list
pie_list = ["(1) Pecan", "(2) Apple Crisp", "(3) Bean", "(4) Banoffee",  "(5) Black Bun", "(6) Blueberry", "(7) Buko", "(8) Burek",  "(9) Tamale", "(10) Steak"]


#add a base price for each price
base_price = 3.99

#add a special item tax
special_tax = 0.05

#add state taxes
state_tax = 0.0725

#total amount
total_amount = 0

#add a count of pies
pie_count = []

#add the prices for each pie
pie_price = []

for pieitems in pie_list:
    pie_count.append(0)
    #print(pie_count[:])
    if ("Banofee" in pieitems) or ("Bean" in pieitems) or ("Steak" in pieitems):
        pie_price.append(base_price + (base_price*special_tax))
    else:
        pie_price.append(base_price)

#loop through the items
#welcome_msg += pie_list[:]
for items in pie_list:
    welcome_msg += items + "\n"
print(welcome_msg)

#add items to the pie shopping cart
pie_cart = []

#define a variable to indicate if we are still ordering
order_more = "YES"

#initialize a variable to the summary message
#on second thought, i should stop, i believe i acheived what i was after, ie. too fancy already imo. :(

#while we are still ordering perform some actions
while order_more == "YES":

    #ask the user what they would like to order
    order_pies = input("Which pie would you like to order?")
    pie_index = int(order_pies)-1

    #add the selected pie to the pie_cart List
    pie_cart.append(pie_list[pie_index])

    #add the count of pies to the pie_count List
    #pie_count[whatever the index is ] = pie_count[xxx] + 1
    #ie. pie_count[i] = pie_count[i] + 1
    pie_count[pie_index] += 1

    print("Great! We'll have that " + pie_list[int(order_pies) -1] + " right out for you.\n")

    continue_order = input("Would you like to make another purchase? \nEnter 'y' to continue 'n' to end.")
    print("-------------------------------------------------------\n\n")
    if continue_order == "n":
        #no more orders, clean up
        order_more = "NO"

        #display a friendly summary to the user
        print("*********    Excellent Pie Choices!    *****************")
        print("You purchased a total of " + str(len(pie_cart)) + " pie(s)")
        #print("_____________________________________________________")
        #print("Your selections were made in the following order: ")
        #print(pie_cart[:])
        print("_____________________________________________________")
        print("Your total is as follows: ")
        print("------------------------")
        pie_text = ""
        sub_total = 0.00

        #set up the range of the for loop to be the upper bound of the pie_list
        for eachpie in range(len(pie_list)):
            pies_name = pie_list[eachpie]
            pies_bought = pie_count[eachpie]
            #round for neatness
            pies_prices = round(pie_price[eachpie],2)

            #get the current amount
            current_amount = (pies_bought*pies_prices)

            #start adding the subtotal
            sub_total += current_amount

            #if a pie was bought then show what they are paying for, if not just show the name of the pie
            if pies_bought > 0:
                #convert to strings for concatenation
                pie_text += str(pies_name) + " - " + str(pies_bought) + " @ $" + str(pies_prices) + "each =     " + str(current_amount) + "\n"
            else: pie_text += str(pies_name) + "\n"

        print(pie_text)
        print("_____________________________________________________")

        #do some calculations for the prices
        total_sales_tax = sub_total * state_tax
        total_amount = sub_total + total_sales_tax

        #display a summary message to the user
        #round the values for neatness
        print("State Tax: %" + str(round((state_tax*100),2)))
        print("----------------------------------------------")
        print("Subtotal: $" + str(round(sub_total,2)))
        print("Sales Tax: $" + str(round(total_sales_tax,2)))
        print("Total : $" + str(round(total_amount,2)))
        print("----------------------------------------------")
        print("_____________________________________________________")
        print("*********Thank you for shopping at The House of Pies!*****************\n")

#add some flair
#create a string for the ascii pie -----------
# http://ascii.co.uk/art/pie
pie_pic = "        )\n"
pie_pic += "    (     \n"
pie_pic += "  (   )  )\n"
pie_pic += "  )  ( )\n"
pie_pic += "()()()()()()\n"
pie_pic += "|\         |\n"
pie_pic += "|.\. . . . |\n"
pie_pic += "\'.\       |\n"
pie_pic += " \.:\ . . .|\n"
pie_pic += "  \'o\     |\n"
pie_pic += "   \.'\. . |\n"
pie_pic += "    \".\   |\n"
pie_pic += "     \'`\ .|\n"
pie_pic += "      \.'\ |\n"
pie_pic += "       \__\|\n"
pie_pic += " \n"

print(pie_pic)

#added a closing input to prevent script from exiting automatically in python shell
#https://stackoverflow.com/questions/3591807/how-can-i-stop-python-exe-from-closing-immediately-after-i-get-an-output
k = input("Press a key to exit")
