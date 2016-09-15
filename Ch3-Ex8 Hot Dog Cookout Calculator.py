#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 7
#
#Notes:

people = int(input("How many people will be attending the cookout?"))
hotDogsPerPerson = int(input("How many hot dogs will each person eat?")
minimumHotDogs = people * hotDogsPerPerson

totalHotDogPackages = minimumHotDogs * 10 / 100
totalHotDogBuns = minimumHotDogs * 8 / 10
hotDogsLeftOver = totalHotDogPackages - minimumHotDogs
hotDogBunsLeftOver = totalHotDogBuns - minimumHotDogs

print("\nThe minimum number of packages of hot dogs required is: %s") %totalHotDogPackages
print("The minimum number of packages of hot dog buns required is: %s") %totalHotDogBuns
print("The number of hot dogs that will be left over is: %s") %hotDogsLeftOver
print("The number of hot dog buns that will be left over is: %s") %hotDogBunsLeftOver
