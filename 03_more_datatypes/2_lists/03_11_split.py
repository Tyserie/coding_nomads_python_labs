'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
inpt_usr = input("Please enter a string: ")
c = True
g = 1
while g < 6:
    x = inpt_usr.split()
    d = len(x)
    list0 = []
    dict = {}
    #g = 1
    for i in x:
        temp = 1
        temp1 = []
        for e in range(g, d):
            if i == x[e] and i not in dict:
                temp += 1
                temp1 = i
        len(temp1)
        #print(len(temp1))
        if len(temp1) > 0:
            dict[temp1] = temp
        g += 1
print(dict)
