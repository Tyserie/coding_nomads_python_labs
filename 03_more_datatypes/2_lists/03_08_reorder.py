'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
n = 0
nrlist = []
while n != 10:
    numbers = int(input("Please, enter single number at a time until it's ten of them: "))
    nrlist.append(numbers)
    n += 1
    result = nrlist[1::2]
    result1 = nrlist[-2:-11:-2]
print(str(result).strip('[]'), str(result1).strip('[]'))




