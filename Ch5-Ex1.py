#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 5, Exercise 1
#
#Notes: Kilometer Converter: Write a program that asks the user to enter a distance in kilometers, and
#       then converts that distance to miles. The conversion formula is as follows: Miles = Kilometers * o.6214
miles = 0

def converter(km):
    miles = km * 0.6214
    print("\nThe distance in miles is: " + format(miles, '.1f'))

def main():
    km = float(input("Enter number of kilometers to convert: "))
    format(miles, '.1f')
    converter(km)

main()