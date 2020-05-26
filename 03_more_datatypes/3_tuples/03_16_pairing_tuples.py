'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
lst_numbrs = [11, 23, 15, 7, 9, 1, 13, 5, 17, 19, 21, 3]
lst_numbrs.sort()
l = len(lst_numbrs)
print(lst_numbrs)
x = int(0)
y = int(2)
list1 = []
list2 = []

for i in range(1,l):
    for e in lst_numbrs[x:y:1]:
        list1.append(e)
    print()
    list2.append(tuple(list1))
    print(list2)
    x += 2
    y += 2
    list1.clear()


