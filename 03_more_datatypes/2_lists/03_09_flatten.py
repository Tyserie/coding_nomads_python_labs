'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
#Solution_1
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = []
a = starting_list[0]
b = starting_list[1]
c = starting_list[2]
flattened_list.extend(a + b + c)
print(flattened_list)

#Solution_2
flattened_list = []
x = len(starting_list)
while x != 0:
    for i in range(x):
        i = starting_list[0]
        flattened_list.extend(i)
        starting_list.pop(0)
        x -= 1

print(flattened_list)










