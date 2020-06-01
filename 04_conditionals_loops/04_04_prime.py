'''
Print out every prime number between 1 and 100.

'''
prime_nr = []
for i in range(2, 100):
    for e in range(2, i):
        if (i % e) == 0:
            break
    else:
        prime_nr.append(i)
print(prime_nr)
