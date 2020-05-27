'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_input = input("Please enter a string: ")
lngt = int(len(user_input))
result = {}
chckd = []
x = 1
for i in user_input:
    count = 1
    if i not in chckd:
        for e in user_input[x:lngt]:
            if i == e:
                count += 1
                chckd.append(i)
        result[i] = count
    x += 1
print(result)



