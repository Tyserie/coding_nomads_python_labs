'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
inv = int(input('Please enter investment amount: '))
inrat = int(input('Please enter interest rate: '))
years = int(input('Please enter number of years to invest: '))
inrat1 = (1 + inrat / 100)
count = inv * inrat1 ** years
print(count)


