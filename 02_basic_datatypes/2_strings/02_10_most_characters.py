'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
users1, users2, users3 = input("Please enter three strings: ").split()
#print(len(users1),"," users1)
#print(len(users2),"," users2)
#print(len(users3),"," users3)



#Chalenge
usr1 = len(users1)
usr2 = len(users2)
usr3 = len(users3)


if usr1 > usr2 or usr1 > usr3:
    print(usr1, ",", users1)
elif usr2 > usr1 and usr2 > usr3:
    print(usr2, ",", users2)
else:
    print(usr3, ",", users3)

















