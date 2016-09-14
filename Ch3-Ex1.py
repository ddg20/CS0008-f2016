#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 1
#
#Notes: newline is not working

day = int(input("Enter a number in the range of 1 through 7:"))

if day == 1:
    print("\nThe day of the week is: Monday")
if day == 2:
    print("\nThe day of the week is: Tuesday")
if day == 3:
    print("\nThe day of the week is: Wednesday")
if day == 4:
    print("\nThe day of the week is: Thursday")
if day == 5:
    print("\nThe day of the week is: Friday")
if day == 6:
    print("\nThe day of the week is: Saturday")
if day == 7:
    print("\nThe day of the week is: Sunday")
else:
    print("\nERROR: USER MUST ENTER NUMBER WITHIN RANGE OF 1-7")