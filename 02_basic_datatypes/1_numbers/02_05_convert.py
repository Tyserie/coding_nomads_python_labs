'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
#Convert an int to a float
int = 5
fint = float(int)
print(type(int))

#Convert a float to an int
flot = 10.23
iflot = int(flot)
print(type(iflot))

#Perform floor division using a float and an int.
10.5//3

#Use two user inputted values to perform multiplication.
num1 = int(input('Please insert first number: '))
num2 = int(input('Please enter second number: '))
print(num1 * num2)