#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 5, Exercise 2
#
#Notes: Sales Tax Program Refactoring:

def state(purchase):
    stateTax = purchase * 0.05
    print("The state tax is: $" + format(stateTax, '.2f'))
    return stateTax

def county(purchase):
    countyTax = purchase * 0.025
    print("The county tax is: $" + format(countyTax, '.2f'))
    return countyTax

def totalTax(purchase):
    totalTaxes = state(purchase) + county(purchase)
    print("The total tax is: $" + format(totalTaxes, '.2f'))
    return totalTaxes

def totalSale(purchase):
    totalSales = totalTax(purchase) + purchase
    print("The total sale is: $" + format(totalSales, '.2f'))

def main():
    purchase = float(input("Enter the amount of a purchase: $"))
    totalTax(purchase)
    totalSale(purchase)

main()
