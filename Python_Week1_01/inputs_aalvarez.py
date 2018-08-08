## Basic Variables

## Instructions

##* Create two different variables that will take the input of your first name and your neighbors first name.

##* Create two more inputs that will ask how many months each of you have been coding.

##* Finally, display a result with both your names and the total amount of months coding.

my_first_name = "Anthony"
my_neighbors_name = input("What is your name?")

my_months_coding = 1
my_neighbor_months_coding = int(input("How many months have you been coding?"))

message = "My name is = " + my_first_name + "\n"
message += "I have been coding for " + str(my_months_coding) + " month(s)\n"
message += "My neighbors name is = " + my_neighbors_name + "\n"
message += "They have been coding for " + str(my_neighbor_months_coding) + " month(s)\n"



print(message)
