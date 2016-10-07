#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 4, Exercise 5
#
#Notes: Average Rainfall

totalRainfall = 0
count = 0

years = int(input("Enter number of years: "))
for year in range(1, years + 1):
    for months in range(1, 13):
        inches = float(input("Enter the number of rainfall in inches for month " + str(months) + ": "))
        totalRainfall += inches
        count += 1
        averageRainfall = totalRainfall / count

print("\nNumber of months: " + str(count))
print("Total inches of rainfall: " + str(totalRainfall))
print("Average rainfall per month: " + format(averageRainfall, '.2f'))