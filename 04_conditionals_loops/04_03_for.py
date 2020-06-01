'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
for nr in range(1, 100):
    if nr % 2 != 0:
        print(nr, end=", ")
