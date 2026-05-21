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
    print("Destination:",destination)
    print("Days:",days)

travel("paris",days = 10)

# 18. Define movie_ticket(movie, price=200, seat="Regular"). Call it with positional and keyword arguments.

def movie_ticket(movie, price = 200, seat = "Regular"):
    print("Movie:",movie)
    print("Price:",price)
    print("Seat:",seat)

movie_ticket("VARANASI",seat = "VIP")

# 19. Write exam_score(student, subject="Math", score=100) and call it with mixed arguments.

def exam_score(student, subject = "Math", score = 100):
    print("Student:",student)
    print("Subject:",subject)
    print("Score:",score)

exam_score("Siddiq")

# 20. Create car_rental(car, days=5, insurance=True) and call it with both positional and keyword arguments.

def car_rental(car, days = 5, insurance = True):
    print("Car:",car)
    print("Days:",days)
    print("Insurance:",insurance)

car_rental("BMW",insurance=False)

#  Section 5: Using *args
# 21. Write a function sum_all(*args) that returns the sum of all numbers passed.

def sum_all(*args):
    return sum(args)

result = sum_all(10,20,30,40)
print(result)

# 22. Create print_names(*args) that prints all names given.

def print_names(*args):
    for name in args:
        print(name)

print_names("Siddiq","Bob","Mahesh")

# 23. Define multiply_all(*args) that multiplies all numbers.

def multiply_all(*args):
    result = 1

    for num in args:
        result = result * num
    return result

answer = multiply_all(2,3,4)
print(answer)

# 24. Write max_number(*args) that returns the largest number.

def max_numbers(*args):
    return max(args)

result = max_numbers(12,45,7,89,23)

print(result)

# 25. Create average(*args) that calculates the average of numbers.

def average(*args):
    total = sum(args)
    avg = total / len(args)
    return avg
result = average(10,20,30,40)

print(result)

# Section 6: Using **kwargs
# 26. Write a function print_info(**kwargs) that prints all key-value pairs.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name = "Siddiq",age = 23,city = "Hyderabad")

# 27. Create student_profile(**kwargs) that prints student details.

def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
    
student_profile(name = "Siddiq",garde = "A",marks = 95)

# 28. Define car_details(**kwargs) that prints car attributes.

def car_details(**kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)

car_details(brand="BMW", color="Black", price=5000000)

# 29. Write employee_data(**kwargs) that prints employee info.
 
def employee_data(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_data(name="Siddiq", department="IT", salary=60000)

# 30. Create settings(**kwargs) that prints configuration settings.

def settings(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

settings(theme="Dark", language="English", notifications=True)

# Section 7: Combining *args and **kwargs
# 31. Write mixed_function(*args, **kwargs) that prints both.

def mixed_function(*args, **kwargs):

    print("Positional Arguments:")
    for value in args:
        print(value)

    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(key, ":", value)

mixed_function(10, 20, 30, name="Siddiq", city="Hyderabad")

# 32. Create register_user(*args, **kwargs) that prints positional and keyword arguments.

def register_user(*args, **kwargs):
    
    print("User Data:")

    for value in args:
        print(value)

    for key, value in kwargs.items():
        print(key, ":", value)

register_user("siddiq","siddiq@gmail.com",age = 23, country = "India")

# 33. Define shopping_cart(*args, **kwargs) that prints items and details.

def shopping_cart(*args, **kwargs):
    
    print("Items:")
    for item in args:
        print(item)

    print("Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

shopping_cart("Laptop","Mouse",price = 60000, delivery = "Tomorrow")

# 34. Write event_details(*args, **kwargs) that prints event info.

def event_detials(*args, **kwargs):

    print("Event Information")

    for value in args:
        print(value)

    for key, value in kwargs.items():
        print(key, ":", value)

event_detials("Tech Fest","Auditorium",day = "20 May",time = "10 AM")

# 35. Create log_data(*args, **kwargs) that prints logs.

def log_data(*args, **kwargs):

    print("Logs:")

    for value in args:
        print(value)

    for key, value in kwargs.items():
        print(key, ":", value)

log_data("Error Found","Restart System",status = "Failed", code = 500)

#  Section 8: Practice Challenges
# 36. Write a function calculate_total(price, quantity=1, tax=5) that returns total cost.

# 1. calculate_total(price, quantity=1, tax=5)

def calculate_total(price, quantity=1, tax=5):

    total = price * quantity
    total_with_tax = total + (total * tax / 100)

    return total_with_tax

result = calculate_total(1000, 2)

print(result)

# 37. Create greet_people(*args, greeting="Hello") that greets multiple people.

def greet_people(*args, greetings= "Hello"):
    
    for name in args:
        print(greetings,name)

greet_people("Siddiq","Bob","Mahesh",greetings="Hi")

# 38. Define student_report(name, *args, **kwargs) that prints name, subjects, and extra info.

def student_report(name, *args, **kwargs):

    print("Name:", name)

    print("Subjects:")
    for subject in args:
        print(subject)

    print("Extra Information:")
    for key, value in kwargs.items():
        print(key, ":", value)

student_report("Siddiq","Math","Science",grade="A",marks=95)

# 39. Write recipe(ingredient1, ingredient2, *args, **kwargs) that prints recipe details.

def recipe(ingredient1, ingredient2, *args, **kwargs):

    print("Main Ingredients:")
    print(ingredient1)
    print(ingredient2)

    print("Extra Ingredients:")
    for item in args:
        print(item)

    print("Recipe Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

recipe("Rice","Chicken","Spices","Oil",cooking_time="45 mins",servings=4)

# 40. Create bank_account(name, balance=0, **kwargs) that prints account info.

def bank_account(name, balance=0, **kwargs):

    print("Account Holder:", name)
    print("Balance:", balance)

    print("Extra Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

bank_account("Siddiq",5000,account_type="Savings",branch="Hyderabad")

#  Section 9: Real-Life Scenarios
# 41. Write flight_booking(destination, *args, **kwargs) that prints booking details.

def flight_booking(destination, *args, **kwargs):

    print("Destination:", destination)

    print("Passengers:")
    for passenger in args:
        print(passenger)

    print("Booking Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

flight_booking("Dubai","Bob","Siddiq",seat="Window",class_type="Business")

# 42. Create hotel_reservation(name, nights=1, **kwargs) that prints reservation info.

def hotel_reservation(name, nights=1, **kwargs):

    print("Guest Name:", name)
    print("Nights:", nights)

    print("Reservation Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

hotel_reservation("Siddiq",3,room_type="Deluxe",breakfast=True)

# 43. Define order_summary(item, quantity=1, *args, **kwargs) that prints order details.

def order_summary(item, quantity=1, *args, **kwargs):

    print("Item:", item)
    print("Quantity:", quantity)

    print("Extra Items:")
    for extra in args:
        print(extra)

    print("Order Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

order_summary("Laptop",2,"Mouse","Keyboard",delivery="Tomorrow",payment="Online")

# 44. Write game_score(player, *args, **kwargs) that prints scores.

def game_score(player, *args, **kwargs):

    print("Player:", player)

    print("Scores:")
    for score in args:
        print(score)

    print("Game Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

game_score("Siddiq",50,70,90,level="Advanced",status="Winner")

# 45. Create conference_registration(name, *args, **kwargs) that prints registration details.

def conference_registration(name, *args, **kwargs):

    print("Participant Name:", name)

    print("Sessions:")
    for session in args:
        print(session)

    print("Registration Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

conference_registration("Siddiq","AI Workshop","Cloud Computing",ticket="Premium",city="Hyderabad")

#  Section 10: Advanced Practice
# 46. Write calculator(operation, *args) that performs sum, multiply, etc.

def calculator(operation, *args):

    if operation == "sum":
        result = sum(args)

    elif operation == "multiply":
        result = 1

        for num in args:
            result = result * num
    else:
        result = "Invalid operation"
    print("Result:",result)

calculator("sum",10,20,30)
calculator("multiply",2,3,4)

# 47. Create profile(name, age, *args, **kwargs) that prints full profile.

def profile(name, age, *args, **kwargs):

    print("Name:",name)
    print("Age:",age)

    print("Skills:")
    for skill in args:
        print(skill)

    print("Extra Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

profile("Siddiq",23,"Python","SQL",city="Hyderabad",experience="Fresher")

# 48. Define task_manager(task, priority="Medium", *args, **kwargs) that prints task details.

def task_manager(task, priority="Medium", *args, **kwargs):

    print("Task:",task)
    print("Priority:",priority)

    print("Sub Tasks:")
    for subtask in args:
        print(subtask)

    print("Task Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

task_manager("Project Submission","High","Prepare Report","Upload Files",deadline = "Tomorrow",status = "Pending")

# 49. Write music_playlist(*args, **kwargs) that prints songs and playlist info.

def music_playlist(*args, **kwargs):

    print("Songs:")
    for song in args:
        print(song)

    print("Playlist Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

music_playlist("Song 1","Song 2","Song 3",playlist_name="Chill Beats",total_songs=3)

# 50. Create smart_home(device, *args, **kwargs) that prints device settings.

def smart_home(device, *args, **kwargs):

    print("Device:", device)

    print("Connected Devices:")
    for item in args:
        print(item)

    print("Settings:")
    for key, value in kwargs.items():
        print(key, ":", value)

smart_home("Smart TV","Speaker","WiFi Router",volume=50,mode="Night")


# Nested Ternary Operator
age = 70

ticket_price = 5 if age < 12 else (7 if age >= 65 else 12)

print(ticket_price)


# Grade System

marks = 85

grade = "A" if marks >= 90 else ("B" if marks >= 70 else "C")

print(grade)


# Maximum of three numbers

a = 10
b = 40
c = 25

largest = a if a > b and a > c else (b if b > c else c)

print(largest)

# Using with input

num = int(input("Enter a number: "))

print("Even") if num % 2 == 0 else print("Odd")



# Using List Comprehension

numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)



# Write a function add_numbers(a, b) that returns the sum of two numbers. Call it with add_numbers(3, 5).


# def add_num(a,b):
#     return a + b
# result = add_num(1,2)
# print(result) 



def add_num(a,b):
    return a + b
result = add_num(1,2)
print(result)