'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''
n = 5
for row in range(1, n + 1):
    for collum in range(row):
        print("*", end="")
    print()