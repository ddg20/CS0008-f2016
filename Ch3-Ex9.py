#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#description:   Introduction to programming with Python, Chapter 3, Exercise 9
#Notes:

number = input("Give me the number: ")
number = int(number)

if(number < 0 and number > 36):
    print("GIVE ME A NUMBER!!")
if(number == 0):
    color = "green"
elif((number >= 1 and number <= 10) or (number >= 19 and number >= 28)):
    if(number % 2 == 0):
        color = "black"
    else:
        color = "red"
elif((number >= 11 and number <= 18) or (number >= 29 and number <= 36)):
    if(number % 2 == 0):
        color = "red"
    else:
        color = "black"

print("EH YOUR COLOR IS " + color)
