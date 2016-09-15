#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 3, Exercise 4
#
#Notes:

romanNumeral = int(input("Enter a number within the range of 1 through 10: "))

if romanNumeral == 1:
    print("\nThe roman numeral is: I")
elif romanNumeral == 2:
    print("\nThe roman numeral is: II")
elif romanNumeral == 3:
    print("\nThe roman numeral is: III")
elif romanNumeral == 4:
    print("\nThe roman numeral is: IV")
elif romanNumeral == 5:
    print("\nThe roman numeral is: V")
elif romanNumeral == 6:
    print("\nThe roman numeral is: VI")
elif romanNumeral == 7:
    print("\nThe roman numeral is: VII")
elif romanNumeral == 8:
    print("\nThe roman numeral is: VIII")
elif romanNumeral == 9:
    print("\nThe roman numeral is: IX")
elif romanNumeral == 10:
    print("\nThe roman numeral is: X")
else:
    print("\nERROR: THE VALUE MUST BE BETWEEN THE RANGE OF 1 THROUGH 10")