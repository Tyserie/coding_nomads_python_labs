'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
count = 0
nbrlist = []
while count < 10:
    numbers = int(input("Please, enter single number at a time until it's ten of them: "))
    count += 1
    nbrlist.append(numbers)
nbrlist.sort()
print(nbrlist)
result = 0
for n in nbrlist:
    result += n
print(result)

