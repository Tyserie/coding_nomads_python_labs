'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
# test = {"a": 1, "b": 2, "c": 3, "a": 2, "c": 4 , "d": 2}
list1 = []
list2 = []
dict_3 = {}
s = 1
e = len(list1)

for i in dict_1:
    c = i, dict_1[i]
    list1.append(tuple(c))
for i in dict_2:
    c = i, dict_2[i]
    list1.append(tuple(c))
for tuples1 in list1:
    for tuples2 in list1[s:6]:
        if tuples1[0] == tuples2[0]:
            # print(tuples1)
            cnt_tup = tuples1[1] + tuples2[1]
            dict_3[tuples1[0]] = cnt_tup
            print(dict_3)
            continue

    s += 1
    # e += 2
