'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
user = input("Please enter a string: ")
a = "a"
i = "i"
o = "o"
u = "u"
e = "e"

a = user.count(a)
i = user.count(i)
o = user.count(o)
u = user.count(u)
e = user.count(e)

print('Vowel "a" is used', a, "times.")
print('Vowel "i" is used', i, "times.")
print('Vowel "o" is used', o, "times.")
print('Vowel "u" is used', u, "times.")
print('Vowel "e" is used', e, "times.")



