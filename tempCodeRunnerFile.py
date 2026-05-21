from functools import reduce
numbers = [10,20,30,40]
total = reduce(lambda x,y : x + y, numbers)
average = total / len(numbers)
print(average)

