'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
usr_inp = int(input("Please enter a number: "))

if usr_inp < 13:
    if usr_inp == 1:
        print("January")
    elif usr_inp == 2:
        print("February")
    elif usr_inp == 3:
        print("March")
    elif usr_inp == 4:
        print("April")
    elif usr_inp == 5:
        print("May")
    elif usr_inp == 6:
        print("June")
    elif usr_inp == 7:
        print("July")
    elif usr_inp == 8:
        print("August")
    elif usr_inp == 9:
        print("September")
    elif usr_inp == 10:
        print("October")
    elif usr_inp == 11:
        print("November")
    elif usr_inp == 12:
        print("December")
else:
    print("Other")