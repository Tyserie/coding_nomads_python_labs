'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
x = list_[0]

for i in list_:
    for y in list_[x:]:
        if i == y:
            unique_list = list.remove(i)
            print(unique_list)
            x += 1

    else:
        unique_list.append(i)
        # x += 1
print(unique_list)
