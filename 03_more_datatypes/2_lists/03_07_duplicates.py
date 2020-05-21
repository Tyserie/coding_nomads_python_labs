'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]
test = 0
for n in list_:
    ind = 1 + test
    for m in list_[ind:]:
        if n == m:
            list_.pop(ind)
        ind += 1
    test += 1
print(list_)

#solution_2
test = []
for n in list_:
    if n not in test:
        test.append(n)
print(test)


