'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
test = True
while test == True:
    print()
    usr_inp = int(input("Please enter a number between 1 and 1,000,000,000: "))
    if usr_inp > 1000000000:
        print("Please choose only number between 1 and 1,000,000,000: ")
        continue
    if usr_inp % 3 == 0 and usr_inp < 1000000000:
        print("The number is divisible by 3!")
        test = False
    else:
        print("The number is not divisible by 3!")

