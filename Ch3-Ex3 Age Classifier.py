#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 3
#
#Notes:

age = int(input("Enter person's age: "))

if age < 0:
    print('\nThis "person" is in the womb.')
elif age <= 1:
    print("\nThis person is an infant.")
elif age <= 13:
    print("\nThis person is a child.")
elif age <= 20:
    print("\nThis person is a teenager.")
else:
    print("\nThis person is an adult.")