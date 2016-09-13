#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 2, Exercise 10
#
#Notes: newline is not working

sugar = 300 / 48
butter = 240 / 48
flour = 330 / 48

cookies = int(input("How many cookies would you like to make?"))

totalSugar = cookies * sugar
totalButter = cookies * butter
totalFlour = cookies * flour

print 'You need: %s grams of sugar' % totalSugar
print str(totalButter) + ' grams of butter'
print('%s grams of flour') %totalFlour