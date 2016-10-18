#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 5, Exercise 3
#
#Notes: How Much Insurance?

def main():
    cost = float(input("Enter replacement cost of building: $"))
    insurance(cost)

def insurance(cost):
    final = 0.80 * cost
    print("\nThe minimum amount of insurance you should buy is: $" + format(final, '.2f'))

main()