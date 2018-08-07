#assignemtn 1
#* **Instructions**

#  * Create two variables called `name` and `country` that will hold strings.

#  * Create two variables called `age` and `hourly_wage` that will hold integers.

#  * Create a variable called `satisfied` which will hold a boolean.

#  * Create a variable called `daily_wage` that will hold the value of `hourly_wage` multiplied by 8.

#  * Print out statements using all of the above variables to the console.


name = input("What is your name? ")
country="country"

age = 21
hourly_wage = 13

satisfied = True

daily_wage = hourly_wage * 8

message = "name = " + name + "\n"
message += "country = " + country + "\n"
message += "age = " + str(age) + "\n"
message += "hourly_wage = " + str(hourly_wage) + "\n"
message += "daily_wage = " + str(daily_wage) + "\n"
message += "satisfied = " + str(satisfied) + "\n"


print(message)
