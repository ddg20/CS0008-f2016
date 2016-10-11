#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 7
#
#Notes: Pennies for Pay

days = int(input("Enter the number of days you would like the pennies to accumulate over: "))
totalAmount = 0
salary = 0.01
print("\nDay\t\tSalary")

for days in range(1, days + 1):
    print(str(days) + "\t\t$" + str(salary))
    totalAmount += salary
    salary *= 2
print("\nThe total amount at the end of the accumulation period is: $" + format(totalAmount, '.2f'))