#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 6
#
#Notes:

month = int(input("Enter a month: "))
date = int(input("Enter a date: "))
year = int(input("Enter a 2-digit year: "))

magicNumber = month * date

if (magicNumber == year):
    print("\nThe date is magic.")
else:
    print("\nThe date is not magic.")