#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 5
#
#Notes:

mass = (int(input("Enter an object's mass: ")))

weight = mass * 9.8

if weight > 500:
    print("\nThe object is too heavy.")
elif weight < 100:
    print("\nThe object is too light")
else:
    print("\nThe object's weight is: %s") %weight