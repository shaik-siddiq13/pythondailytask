# Generators 

# 1.Write a generator that yields numbers from 1 to 20, but only if they are even.

def even_numbers():
    for i in range(1,21):
        if i % 2 == 0:
            yield i
for num in even_numbers():
    print(num)

# 2.Create a generator that yields squares of numbers from 1 to 10 using a for loop.

def squares():
    for i in range(1,11):
        yield i**2

for square in squares():
    print(square)

# 3.Implement a generator that yields numbers divisible by 3 up to 30.

def divisible_by_three():
    for i in range(1,31):
        if i % 3 == 0:
            yield i
for num in divisible_by_three():
    print(num)

# 4.Write a generator that yields characters of a string, but skip vowels.

def skip_vowels(text):
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch not in vowels:
            yield ch
for char in skip_vowels("siddiq"):
    print(char)

# 5.Create a generator that yields Fibonacci numbers up to n using a while loop.

def fibonacci(n):
    a,b = 0,1
    while a <= n:
        yield a
        a,b = b,a+b
for num in fibonacci(50):
    print(num)

# 6.Implement a generator that yields prime numbers less than 50 (use conditionals).

def primes():
    for num in range(2,50):
        prime = True
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num 
for prime in primes():
    print(prime)

# 7.Write a generator that yields numbers from 1 to 10, but stops if the number is greater than 7.

def numbers():
    for i in range(1,11):
        if i > 7:
            return
        yield i
for num in numbers():
    print(num)

# 8.Create a generator that yields odd numbers up to 15 using if conditions.

def odd_numbers():
    for i in range(1,16):
        if i % 2 != 0:
            yield i 
for num in odd_numbers():
    print(num)

# 9.Implement a generator that yields factorials of numbers from 1 to 5.

def factorial():
    fact = 1
    for i in range(1,6):
        fact *= i
        yield fact
for num in factorial():
    print(num)

# 10.Write a generator that yields multiples of 5 up to 50.

def multiples_of_five():
    for i in range(1,51):
        if i % 5 == 0:
            yield i
for num in multiples_of_five():
    print(num)

# 11.Create a generator that yields numbers from 1 to n, but only if they are not divisible by 2.

def odd_numbers(n):
    for i in range(1,n+1):
        if i % 2 != 0:
            yield i
for num in odd_numbers(20):
    print(num) 

# 12.Implement a generator that yields the running sum of numbers in a list.

def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total
for s in running_sum([1,2,3,4,5]):
    print(s)

# 13.Write a generator that yields binary representations of numbers from 1 to 10.

def binary_numbers():
    for i in range(1,11):
        yield bin(i)
for b in binary_numbers():
    print(b)

# 14.Create a generator that yields elements of a list, but skips duplicates.

def unique_elements(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item 
for elements in unique_elements([1,2,2,3,3,3,4,4,5,5,5]):
    print(elements)

# 15.Implement a generator that yields rows of Pascal’s Triangle up to n.

def pascal_triangle(n):
    row = [1]
    for _ in range(n):
        yield row
        row = [1] + [row[i] + row[i-1] for i in range(1,len(row))] + [1]
for row in pascal_triangle(5):
    print(row)



#  Decorators
# 1.Write a decorator that prints "Function is starting" before running a function.

def start_decorator(func):
    def wrapper():
        print("Function is starting")
        func()
    return wrapper

@start_decorator
def greet():
    print("Hello")
greet()

# 2.Create a decorator that prints "Function has ended" after running a function.

def end_decorator(func):
    def wrapper():
        func()
        print("Function has ended")
    return wrapper

@end_decorator
def greet():
    print("Hello")


greet()

# 3.Implement a decorator that prints the arguments passed to a function using a loop.

def show_args(func):
    def wrapper(*args):
        print("Arguments")
        for i in args:
            print(i)
        func(*args)
    return wrapper

@show_args
def add(a, b):
    print(a + b)
add(10,20)    

# 4.Write a decorator that checks if the input number is positive before running a function.

def positive_check(func):
    def wrapper(num):
        if num > 0:
            func(num)
        else:
            print("Number is not positive")
    return wrapper

@positive_check
def display(num):
    print(num)

display(5)
display(-2)


# 5.Create a decorator that runs a function twice using a for loop.













# 6.Implement a decorator that converts the output of a function to uppercase.










# 7.Write a decorator that prints "Start" before and "End" after a function runs.




# 8.Create a decorator that counts how many times a function has been called.







# 9.Implement a decorator that multiplies the return value of a function by 2.







# 10.Write a decorator that only allows a function to run once.










# 11.Create a decorator that prints the name of the function being executed.










# 12.Implement a decorator that checks if the user is "admin" before running a function.









# 13.Write a decorator that retries a function up to 3 times if it fails.








# 14.Create a decorator that prints all items in a list returned by a function using a loop.









# 15.Implement a decorator that ensures a function always returns a dictionary.







