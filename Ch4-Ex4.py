#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 4
#
#Notes: Distance Travelled

speed = int(input("Enter speed of vehicle in mph: "))
hours = int(input("Enter number of hours vehicle has traveled: "))
print("Hour\t\tDistance Traveled")
for hours in range(1, hours + 1):
    distance = speed * hours
    print(str(hours) + "\t\t\t\t" + str(distance))