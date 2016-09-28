#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 2, Exercise 3
#
#Notes:

system = input("""Enter either "USC" (US Customary Units) or "M" (Metric System): """)

if(system == "USC"):
    miles = int(input("Enter the number of miles driven: "))
    gallons = int(input("Enter the number of gallons used: "))

    kilometers = miles * 1.60934  # converting miles to kilometers
    liters = gallons * 3.78541  # converting gallons to liters

    milesPerGallons = miles / gallons
    lPer100km = 100 * liters / kilometers

elif(system == "M"):
    kilometers = int(input("Enter the number of kilometers driven: "))
    liters = int(input("Enter the number of liters used: "))

    miles = kilometers * 0.621371
    gallons = liters * 0.264172

    milesPerGallons = miles / gallons
    lPer100km = 100 * liters / kilometers

else:
    print("ERROR: You must either enter 'USC' or 'M' in all caps for program to work")

if(lPer100km > 20):
    gasConsumptionRating = "Extremely Poor"

elif(lPer100km > 15 and lPer100km <= 20):
    gasConsumptionRating = "Poor"

elif(lPer100km > 10 and lPer100km <= 15):
    gasConsumptionRating = "Average"

elif(lPer100km > 8 and lPer100km <= 10):
    gasConsumptionRating = "Good"

else:
    gasConsumptionRating = "Excellent"


print("\nDistance: " + format(miles, '25.3f') + " miles" + format(kilometers, '17.3f') + " Km")
print("Gas: " + format(gallons, '30.3f') + " gallons" + format(liters, '15.3f') + " Liters")
print("Consumption: " + format(milesPerGallons, '21.3f') + " mpg" + format(lPer100km, '19.3f') + " L/100Km")
print("\nGas Consumption Rating: " + gasConsumptionRating)
