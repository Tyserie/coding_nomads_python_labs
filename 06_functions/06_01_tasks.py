'''
Write a script that completes the following tasks.
'''
# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def num_div_by(number):
    x = number % 4 == 0
    y = number % 7 == 0
    return print("Is", number, "divisible by 4?", x, "\nIs", number, "divisible by 7?", y)
num_div_by(780)

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def num_div_by(number):
    x = number % 4 == 0 and number % 7 == 0
    return print("Is", number, "divisible by 4 and 7?",  x)
num_div_by(780)

# take in a number from the user between 1 and 1,000,000,000
# call your functions, passing in the user input as the arguments, and set their output equal to new variables
# print your new variables to display the results
def num_div_by(number):
    x = number % 4 == 0 and number % 7 == 0
    return print("Is", number, "divisible by 4 and 7?",  x)

usr_inp = int(input("Please enter number between 1 - 1 000 000 000: "))
num_div_by(usr_inp)






