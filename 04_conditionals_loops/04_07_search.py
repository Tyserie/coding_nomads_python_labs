'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
usr_inp = int(input("Please chose a number between 0 and 1,000,000,000: "))
x = True
result_ = None

while x == True:
    for num_br in range(0, 1000000000):
        if num_br == usr_inp:
            result_ = num_br
            x = False
            break
print(result_)



