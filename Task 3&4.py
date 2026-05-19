# TASK 3
# Python Coding Statements

#  Break & Continue Practice

# 1. Write a loop that prints numbers from 1 to 10, but stops completely when the number is 6.

for i in range(1,11):
    if i == 6:
        break
    print(i)

# 2. Write a loop that prints numbers from 1 to 10, but skips printing the number 5.

for i in range(1,11):
    if i == 5:
        continue
    print(i)

# 3. Write a loop that prints only odd numbers between 1 and 10 using continue.

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

# 4. Write a loop that prints numbers from 1 to 20, but breaks when the number is divisible by 7.

for i in range(1,21):
    if i % 7 == 0:
        break
    print(i)

# 5. Write a loop that prints numbers from 1 to 10, but skips all even numbers.

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

# 6. Write a loop that prints numbers from 1 to 10, but stops when the number is greater than 8.

for i in range(1,11):
    if i > 8:
        break
    print(i)

# 7. Write a loop that prints numbers from 1 to 15, but skips numbers divisible by 3.

for i in range(1,16):
    if i % 3 == 0:
        continue
    print(i)

# 8. Write a loop that prints numbers from 1 to 10, but breaks when the number is equal to 4.

for i in range(1,11):
    if i == 4:
        break
    print(i)

# 9. Write a loop that prints numbers from 1 to 10, but skips printing 2 and 7.

for i in range(1,11):
    if i == 2 or i == 7:
        continue
    print(i)

# 10. Write a loop that prints numbers from 1 to 10, but breaks when the number is 9.

for i in range(1,11):
    if i == 9:
        break
    print(i)


#  Ternary Operator Practice

# 11. Write a program that checks if a number is even or odd using a ternary operator.

num = 8

result = "Even" if num % 2 == 0 else "Odd"

print(result)

# 12. Write a program that prints "Positive" if a number is greater than 0, otherwise "Negative or Zero".

num = -5

result = "Positive" if num > 0 else "Negative or Zero"

print(result)

# 13. Write a program that prints "Adult" if age ≥ 18, otherwise "Minor".

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# 14. Write a program that prints "Pass" if marks ≥ 40, otherwise "Fail".

marks = 35

result = "Pass" if marks >= 40 else "Fail"

print(result)


# 15. Write a program that prints "Big" if a number > 100, otherwise "Small".

num = 150

result = "Big" if num > 100 else "Small"

print(result)

# 16. Write a program that prints "Equal" if two numbers are the same, otherwise "Not Equal".

a = 10
b = 10

result = "Equal" if a == b else "Not Equal"

print(result)

# 17. Write a program that prints "Divisible by 5" if a number is divisible by 5, otherwise "Not Divisible".

num = 23

result = "Divisible by 5" if num % 5 == 0 else "Not Divisible"

print(result)

# 18. Write a program that prints "Leap Year" if a year is divisible by 4, otherwise "Not Leap Year".

year = 2024

result = "Leap Year" if year % 4 == 0 else "Not Leap Year"

print(result)

# 19. Write a program that prints "Yes" if a number is positive, otherwise "No".

num = 7

result = "Yes" if num > 0 else "No"

print(result)

# 20. Write a program that prints "First" if a > b, otherwise "Second".

a = 13
b = 7

result = "First" if a > b else "Second"

print(result)


# TASK 4
#  Section 1: Basic Function Creation (Positional Arguments)

# 1. Write a function add_numbers(a, b) that returns the sum of two numbers. Call it with add_numbers(3, 5).

def add_numbers(a,b):
    return a + b

result = add_numbers(3,5)
print(result)

# 2. Create a function multiply(x, y) that multiplies two numbers. Call it with positional arguments.

def multiply(x,y):
    return x * y

result = multiply(4,6)
print(result)

# 3. Define a function greet(name) that prints "Hello, <name>!". Call it with "Alice".

def greet(name):
    print("Hello,",name + "!")

greet("Alice")

# 4. Write a function power(base, exponent) that returns base ** exponent. Call it with power(2, 3).

def power(base,exponent):
    return base ** exponent

result = power(2,3)
print(result)

# 5. Create a function area_rectangle(length, width) that returns the area. Call it with area_rectangle(10, 5).

def area_rectangle(length,width):
    return length * width

result = area_rectangle(10,5)
print(result)


#  Section 2: Keyword Arguments
# 6. Modify greet(name) to accept a keyword argument. Call it as greet(name="Bob").

def greet(name):
    print("Hello,",name + "!")

greet(name = "Bob")

# 7. Write a function introduce(name, age) that prints "My name is <name> and I am <age> years old." Call it using keyword arguments.

def introduce(name,age):
    print("My name is",name,"and I am",age,"Years old")

introduce(name = "Siddiq",age = 23)

# 8. Create a function calculate_price(item, price) and call it with keyword arguments.

def calculate_price(item,price):
    print("Item:",item)
    print("Price:",price)

calculate_price(item = "Laptop",price = 50000)

# 9. Write a function student_info(name, grade) and call it as student_info(grade="A", name="John").

def student_info(name,grade):
    print("Name:",name)
    print("Grade:",grade)

student_info(name = "John",grade = "A")

# 10. Define book_details(title, author) and call it using keyword arguments.

def book_details(title,author):
    print("Title:",title)
    print("Author:",author)

book_details(title = "Python",author = "Siddiq")

#  Section 3: Default Arguments
# 11. Write a function greet(name="Guest") that prints "Hello, <name>!". Call it without passing a name.

def greet(name = "Guest"):
    print("Hello,",name + "!")
greet()

# 12. Create a function discount(price, percent=10) that applies a discount. Call it with and without the percent.

def discount(price,percent=10):
    final_price = price - (price * percent / 100)
    print("Final price:",final_price)

discount(1000) # calling with default percent
discount(1000,20) # calling with custom percent

# 13. Define welcome_message(message="Welcome to Python!"). Call it without arguments.

def welcome_message(message = "Welcome to Python!"):
    print(message)
welcome_message()

# 14. Write a function circle_area(radius, pi=3.14) that calculates area. Call it with only radius.

def circle_area(radius, pi=3.14):
    area = pi * radius * radius
    print("Area of Circle:",area)

circle_area(5)

# 15. Create print_date(day, month="March", year=2026) and call it with just day.

def print_date(day, month = "March", year = 2026):
    print(day,month,year)
print_date(15)

#  Section 4: Mixing Positional & Keyword Arguments
# 16. Write order_food(item, quantity=1) and call it with order_food("Pizza").

def order_food(item,quantity=1):
    print("Item:",item)
    print("Quantity:",quantity)

order_food("pizza")

# 17. Create travel(destination, days=7) and call it with travel("Paris", days=10).

def travel(destination,days = 7):
    


# 18. Define movie_ticket(movie, price=200, seat="Regular"). Call it with positional and keyword arguments.




# 19. Write exam_score(student, subject="Math", score=100) and call it with mixed arguments.




# 20. Create car_rental(car, days=5, insurance=True) and call it with both positional and keyword arguments.

