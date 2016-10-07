#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 2
#
#Notes: Calories Burned

print("\nMin\t Cal\n")
for min in range(10, 35, 5):
    calories = min * 4.2
    print(str(min) + "\t" + str(calories))