'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
usr_inp = input("Please enter the string: ")
x = usr_inp.split()
result_list = []
tupl_ = ()

for i in x:
    result_list.append(tuple(i))
print(result_list)