#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#description:   Introduction to programming with Python, Chapter 3, Exercise 7
#Notes:

firstPrimary = input("Enter the name (all lowercase) of a primary color: ")
secondPrimary = input("Enter the name (all lowercase) of a second primary color: ")

if "blue" == firstPrimary:
    if "red" == secondPrimary:
        print("\nWhen you mix the 2 colors, you get the secondary color: purple")

if firstPrimary == "red":
    if secondPrimary == "blue":
        print("\nWhen you mix the 2 colors, you get the secondary color: purple")

if firstPrimary == "red":
    if secondPrimary == "yellow":
        print("\nWhen you mix the 2 colors, you get the secondary color: orange")

if firstPrimary == "yellow":
    if secondPrimary == "red":
        print("\nWhen you mix the 2 colors, you get the secondary color: orange")

if firstPrimary == "blue":
    if secondPrimary == "yellow":
        print("\nWhen you mix the 2 colors, you get the secondary color: green")

if firstPrimary == "yellow":
    if secondPrimary == "blue":
        print("\nWhen you mix the 2 colors, you get the secondary color: green")

else:
    print("\nERROR: You have to enter the names of two primary colors to mix (in all lowercase letters)")