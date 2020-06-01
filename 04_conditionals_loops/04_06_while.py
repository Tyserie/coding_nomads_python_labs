'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
x = 0
while x < 1000:
    result = x + 5
    x = result
    print(result, end=" ")
