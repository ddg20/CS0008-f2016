#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 8
#
#Notes: Sum of Numbers

num = 0
sum = 0
while(num >= 0):
    num = int(input("Enter a positive number to add to the sum or enter negative to exit program: "))
    if(num > 0):
        sum += num
print("\nThe sum of the positive numbers is: " + str(sum))