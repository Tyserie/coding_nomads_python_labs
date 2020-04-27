'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
x = input("Please enter the string: ")
y = input("Please enter the symbol: ")
z = x[0]

new = x.replace(z, y, )
print()
print(new)



