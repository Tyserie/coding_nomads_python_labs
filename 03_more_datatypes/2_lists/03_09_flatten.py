'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = ""
for i in starting_list:
    for t in i:
        s += str(t)
        #x.extend(str(t))

list = []
list.extend(s)
print(list)





#print(str)
#print(str(starting_list).strip('[]'))
