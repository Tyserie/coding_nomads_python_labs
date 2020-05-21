'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list = [9, 2, 6, 1, 55, 2, "hi", 4, 6, 1, 13]
indexes = []
new_list = []

while len(list) > 0:
    len_lst = len(list) - 1
    item0 = list[0]
    for i in range(1, len_lst):
        if item0 == list[i]:
            indexes.append(i)
    if len(indexes) > 0:
        list.pop(indexes[0])
        indexes.clear()
    else:
        new_list.append(list[0])

    list.remove(item0)
print(new_list)