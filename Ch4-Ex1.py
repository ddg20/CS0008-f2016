#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 1 - Bug Collector
#
#Notes:

totalBugs = 0
for days in range(1, 6):
    bugs = int(input("Enter number of bugs collected for day " + str(days) + ": "))
    if(bugs < 0):
        exit()
    totalBugs += bugs
print("Total number of bugs is: " + str(totalBugs))