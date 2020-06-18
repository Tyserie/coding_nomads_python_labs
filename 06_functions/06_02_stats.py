'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  # define the function here
  list_min = min(list)
  list_max = max(list)
  list_sum = sum(list)
  list_avr = list_sum / 7
  print(f"list min number is {list_min}\n"
        f"list max number is {list_max}\n" 
        f"list sum is {list_sum}\n" 
        f"list average is {list_avr}"
        )

# call the function below here
stats(example_list)