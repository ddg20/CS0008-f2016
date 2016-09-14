#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 2
#
#Notes:

length1 = int(input("Enter length of first rectangle: "))
width1 = int(input("Enter width of first rectangle: "))
length2 = int(input("Enter length of second rectangle: "))
width2 = int(input("Enter width of second rectangle: "))

rectangle1 = length1 * width1
rectangle2 = length2 * width2

if rectangle1 > rectangle2:
    print("\nThe first rectangle has greater area")
if rectangle2 > rectangle1:
    print("\nThe second rectangle has greater area")
if rectangle1 == rectangle2:
    print("\nThe two rectangles have equal area")