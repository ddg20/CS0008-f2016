#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 9
#
#Notes: Ocean Levels

millimeters = 0

print("Year\tMillimeters")
for year in range(1, 26):
    millimeters += 1.6
    print(str(year) + "\t\t\t" + format(millimeters, '.1f'))