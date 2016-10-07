num = int(input("Enter the number of squares you would like: "))
print("\nNum:\t" + "Sqr:")

for num in range(0, num + 1):
    square = num ** 2

    print(str(num) + " \t\t" + str(square))