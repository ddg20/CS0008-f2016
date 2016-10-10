#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 6
#
#Notes: Celsius to Fahrenheit Table

celsius = 0

print("C\t F")
while(celsius < 21):
    fahrenheit = ((9 / 5) * celsius) + 32
    print(str(celsius) + "\t " + format(fahrenheit, '.1f'))
    celsius += 1
