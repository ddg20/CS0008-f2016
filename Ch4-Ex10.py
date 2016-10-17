#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 10
#
#Notes: Tuition Increase

tuition = 8000
print("Year\t\tTuition")
for year in range(1, 6):
    tuition *= 1.03
    print(str(year) + "\t\t\t$" + format(tuition, '.2f'))