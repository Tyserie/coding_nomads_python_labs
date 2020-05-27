'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
#usr_inp = input("Please enter a string: ")
user_input = "hello"
count = 1
for i in user_input:
    e = user_input[1]
    chckd = []
    if i not in chckd:
        if i == e:
            count += 1



