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
lst_numbrs = [11, 23, 15, 7, 9, 1, 13, 5, 17, 21, 3, 68, 5, 13, 45, 69, 78]
lst_numbrs.sort()
odd_lngt = len(range(2, len(lst_numbrs)))
if odd_lngt % 2 != 0:
    lst_numbrs.append(0)
l = int(len(lst_numbrs) / 2) + 1
x = int(0)
y = int(2)
list1 = []
list2 = []
for i in range(1, l):
    for e in lst_numbrs[x:y:1]:
        list1.append(e)
    list2.append(tuple(list1))
    x += 2
    y += 2
    list1.clear()
for i in list2:
    print(i)
