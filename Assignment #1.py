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

if(system == "USC"):  # US Customary Units
    miles = int(input("Enter the number of miles driven: "))  # user inputs miles
    gallons = int(input("Enter the number of gallons used: "))  # user inputs gallons

    kilometers = miles * 1.60934  # converting miles to kilometers
    liters = gallons * 3.78541  # converting gallons to liters

    milesPerGallons = miles / gallons  # calculating mpg
    lPer100km = 100 * liters / kilometers  # calculating Lper100km

elif(system == "M"):
    kilometers = int(input("Enter the number of kilometers driven: "))  # user inputs kilometers
    liters = int(input("Enter the number of liters used: "))  # user inputs liters

    miles = kilometers * 0.621371  # converting kilometers to miles
    gallons = liters * 0.264172  # converting liters to gallons

    milesPerGallons = miles / gallons  # calculating mpg
    lPer100km = 100 * liters / kilometers  # calculating Lper100km

else:
    print("ERROR: You must either enter 'USC' or 'M' in all caps for program to work")  # error if USC or M isn't typed

# determines gas consumption rating based on Lper100km

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

# outputs distance, gas, consumption, and rating in both usc and metric

print("\n                                USC                    M")
print("Distance: " + format(miles, '25.3f') + " miles" + format(kilometers, '17.3f') + " Km")
print("Gas: " + format(gallons, '30.3f') + " gallons" + format(liters, '15.3f') + " Liters")
print("Consumption: " + format(milesPerGallons, '21.3f') + " mpg" + format(lPer100km, '19.3f') + " L/100Km")
print("\nGas Consumption Rating: " + gasConsumptionRating)
