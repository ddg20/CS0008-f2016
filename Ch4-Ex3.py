#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 3
#
#Notes: Budget Analysis

x = "y"
total = 0
budget = int(input("Enter the amount you have budgeted for a month: $"))

while(x == "y"):
    expense = int(input("Enter expense amount: $"))
    total += expense
    x = input("Enter 'y' if you would like to add another expense, otherwise press any key: ")
if(total > budget):
    over = total - budget
    print("You went over your budget by: $" + str(over))
elif(total < budget):
    under = budget - total
    print("You went under your budget by: $" + str(under))
else:
    print("You spent exactly what you were supposed to!")