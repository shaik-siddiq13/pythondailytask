#  Python Basic Programs

# A. Data Types & Literals (1–7)

# 1. Store your name, age, and city in variables and print them.

name = "Siddiq"
age = 23
city = "Hyderabad"

print("Name:",name)
print("Age:",age)
print("City:",city)


# 2.Create a tuple with 5 fruits and print the third fruit.

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Third fruit:", fruits[2])


# 3. Store marks of 3 subjects in a dictionary and print the marks of "Math".

marks = {"Math":85, "Science":90, "English":88}

print("Marks in Math:", marks["Math"])


# 4. Write a program to store 3 integers and print their sum.

a = 10
b = 20
c = 30

total = a + b + c
print("Sum of integers:",total)

# 5. Create a tuple of 4 colors and print the last color.

colors = ("Red","Green","Blue","Black")

print("Last color:",colors[3])


# 6. Store employee details (name, ID, department) in a dictionary and print the department.

employee = {"name":"Siddiq","ID":1307,"department":"IT"}

print("Employee department:",employee["department"])


# 7. Write a program to store a float, int, and string in variables and print their types.

num1 = 13.7
num2 = 13
text = "Siddiq"

print(type(num1))
print(type(num2))
print(type(text))


#. Strings (8–14)
# 8. Check if "Python" is present in "I am learning Python programming".

text = "I am Learning Python Programming"

print("Python" in text)

# 9. Print only the first 5 characters of "Hello World".

text = "Hello World"

print(text[:5])

# 10. Concatenate two strings "Good" and "Morning".

str1 = "Good"
str2 = "Morning"

result = str1 + " " + str2
print(result)

# 11. Count how many times "o" appears in "Hello World".

text = "Hello World"

count = text.count("o")

print("Number of o:",count)


# 12. Reverse the string "Python".

text = "Python"

reversed_text = text[::-1]

print("Reversed string:",reversed_text)

# 13. Check if a string entered by the user starts with "A".

text = input("Enter a string:") 

print(text.startswith("A"))

# 14. Check if "apple" contains "p".

text = "apple"

print("p" in text)

#. Operators (15–21)
# 15. Take two numbers and print their sum, difference, product, and quotient.

num1 = 10
num2 = 20

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)


# 16. Check if 25 is greater than 20 and less than 30.

num = 25
if num > 20 and num < 30:
    print("25 is greater than 20 and less than 30")


# 17. Ask the user for two numbers. Print "Both are positive" if both are greater than 0, else "At least one is not positive".

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 > 0 and num2 > 0:
    print("Both are positive")
else:
    print("At least one is not positive")


# 18. Check if a number is divisible by both 2 and 3.

num = 12

if num % 2 == 0 and num % 3 == 0:
    print("Number is divisible by both 2 and 3")


# 19. Check if "a" is in "apple".

text = "apple"
print("a" in text)

# 20. Check if a number is between 1 and 100 (inclusive).

num = 13
if num >= 1 and num<= 100:
    print("Number is between 1 and 100")


# 21.Compare two strings "cat" and "dog".

str1 = "Cat"
str2 = "Dog"

print(str1 == str2)


# Conditional Statements (22–30)

# 22.Check if a number is positive, negative, or zero.

num = 13

if num > 0:
    print("Number is positive")
elif num < 0:
    print("umber is negative")
else:
    print("Number is zero")


# 23. Ask the user to enter their age. If age ≥ 18, print "Eligible to vote", else "Not eligible".

age = int(input("Enter your age:"))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 24 . Check if a given number is even or odd.

num = 13

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 25.  Input a number and check if it is divisible by 5.

num = int(input("Enter a number:"))

if num % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# 26. Ask the user to enter a password. If it matches "admin123", print "Access Granted", else "Access Denied".\

password = input("Enter password:")

if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")


# 27. Check if a character entered by the user is a vowel or consonant.

ch = input("Enter a character:")

if ch in "aeiouAEIOU":
    print("Character is a vowel")
else:
    print("Character is a consonant")


#  28. Check if a given year is a leap year.

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")


# 29. Ask the user for marks. Print "Grade A" if marks ≥ 90, "Grade B" if ≥ 75, "Grade C" if ≥ 50, else "Fail".

marks = int(input("Enter marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# 30. Check if a number is odd and greater than 50.

num = 53

if num % 2 != 0 and num > 50:
    print("Number is odd and greater than 50")
else:
    print("Number is not odd and greater than 50")


# . Tuples (31–35)
# 31. Create a tuple with 6 numbers. Print the largest and smallest number.

numbers = (10,20,13,7,50,5)

print("Largest number:",max(numbers))
print("Smallest number:",min(numbers))


# 32. Check if 50 exists in (10, 20, 30, 40, 50, 60).

numbers = (10,20,30,40,50,60)

print(50 in numbers)


# 33. Store 5 colors in a tuple. Ask the user to enter a color name. Check if it exists.

colors = ("Red","Green","Blue","Black","Pink")

user = input("Enter a color name:")

if user in colors:
    print("Color exists")
else:
    print("Color does not exist")


# 34. Print the length of a tuple (1, 2, 3, 4, 5).

numbers = (1,2,3,4,5)
print(len(numbers))


# 35.Create a tuple with 4 strings. Print them one by one using indexing.

names = ("Siddiq","Bob","Mahesh","Pawankalyan")

print(names[0])
print(names[1])
print(names[2])
print(names[3])


#  Dictionaries (36–41)
# 36.Create a dictionary with 3 countries as keys and their capitals as values. Print the capital of "India".

countries = {"India":"New Delhi","USA":"Washington D.C.","France":"paris"}

print("Capital of India:",countries["India"])

# 37. Add a new country-capital pair to an existing dictionary.

countries = {"India":"New Delhi","USA":"Washington D.C."}

countries["France"] = "Paris"

print(countries)


# 38. Given a dictionary of student marks, check if "Anita" is present as a key. If yes, print her marks.

marks = {"Siddiq":85,"Anita":90,"Bob":78}
if "Anita" in marks:
    print("Anita marks:",marks["Anita"])


# 39. Create a dictionary with usernames and passwords. Ask the user to enter a username and password. If both match, print "Login Successful", else "Login Failed".

users = {"admin":"admin123","user1":"password123"}

username = input("Enter username:")
password = input("Enter password:")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Login Failed")


# 40. Print all keys of a dictionary.

student = {"name":"Siddiq","age":23,"city":"Hyderabad"}

print(student.keys())

# 41. Create a dictionary with 3 items and their prices. Ask the user to enter an item name. Print the price if it exists, else "Item not found".


prices = {"Apple":10,"Banana":5,"Mango":15}

item_name = input("Enter item name:")

if item_name in prices:
    print("Price of",item_name,":",prices[item_name])
else:
    print("Item not found")

#  Lists (42–61)
# 42. Create a list of 5 numbers and print the first and last elements.

numbers = [10,20,30,40,50]

print("First element:",numbers[0])
print("Last element:",numbers[-1])


# 43. Add a new element to a list.

fruits = ["Apple","Banana","Mango"]

fruits.append("Orange")
print(fruits)


# 44. Remove an element from a list.

colors = ["Red","Green","Blue","Black"]

colors.remove("Green")

print(colors)

# 45. Create a list of 4 colors and print its length.

colors = ["Red","Green","Blue","Black"]

print(len(colors))

# 46. Check if "red" exists in a list of colors.

colors = ["Red","Green","Blue","Black"]

print("Red" in colors)


# 47. Print the second to fourth elements of a list.

numbers = [10,20,30,40,50]

print(numbers[1:4])


# 48. Print the last 3 elements of a list.

numbers = [10,20,30,40,50]

print(numbers[-3:])


# 49. Store 5 names in a list and print the name at index 2.

names = ["siddiq","Bob","Mahesh","Pawankalyan","Prabha"]

print(names[2])

# 50. Reverse a list.

numbers = [10,20,30,40,50]

numbers.reverse()

print(numbers)


# 51. Replace the second element of a list with "Python".

languages = ["java","C++","AWS"]

languages[1] = "Python"

print(languages)

# 52.Create a list of 5 numbers. Check if a number entered by the user exists in the list.

numbers = [10,20,30,40,50]

user_num = int(input("Enter a number:"))

if user_num in numbers:
    print("Number exists in the list")
else:
    print("Number does not exist in the list")


# 53. Store 5 subjects in a list. Ask the user to enter a subject name. If it exists, print "Found", else "Not Found".

subjects = ["Math","Science","English","Social","Telugu"]

user_sub = input("Enter a subject name:")

if user_sub in subjects:
    print("Found")
else:
    print("Not Found")


# 54. Create a list of marks. If the average is ≥ 50, print "Pass", else "Fail".

marks = [85,90,78,60,45]

average = sum(marks) / len(marks)

if average >= 50:
    print("Pass")
else:
    print("Fail")

# 55. Check if the first and last elements of a list are equal.

numbers = [10,20,30,40,10]

if numbers[0] == numbers[-1]:
    print("First and last elements are equal")
else:
    print("First and last elements are not equal")

# 56. Create a list of strings. Print "Contains Python" if "Python" is in the list.

languages = ["Java","Python","C++"]

if "Python" in languages:
    print("Contains Python")
else:
    print("Does not contain Python")


# 57. Create a list of 5 numbers. Print the largest and smallest numbers.

numbers = [10,20,30,40,50]

print(max(numbers))
print(min(numbers))

# 58. Count how many times "apple" appears in a list.

fruits = ["Apple","Banana","Mango","Apple","Orange"]

count = fruits.count("Apple")
print(count)


# 59. Store 5 numbers in a list. Print only the even numbers.

numbers = [10, 15, 20, 25, 30]

for num in numbers:
    if num % 2 == 0:
        print(num)

# 60. Check if a list is empty.

my_list =[]

if not my_list:
    print("List is empty")
else:
    print("List is not empty")


# 61. Create a list of 5 numbers. If all numbers are positive, print "All Positive", else "Contains Negative".

numbers = [10,20,30,40,50]

if all(num > 0 for num in numbers):
    print("All Positive")
else:
    print("Contains Negative")

#  Mixed Concept Questions (62–70)
# 62.Store 5 numbers in a tuple. Check if the number 10 is present.


numbers = (10,20,30,40,50)

print(10 in numbers)


# 63. Create a dictionary with student names as keys and marks as values. Check if "Rahul" is in the dictionary.

students = {"Siddiq":85,"Rahul":80,"Bob":78}

if "Rahul" in students:
    print("Rahul is present")
else:
    print("Rahul is not present")


# 64. Take a string input and check if it contains "Python".

text = input("Enter a string:")

if "Python" in text:
    print("String contains Python")
else:
    print("String does not contain Python")


# 65. Ask the user for two numbers. Print "Equal" if they are equal, "First is greater" if the first is larger, else "Second is greater".

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 == num2:
    print("Equal")
elif num1 > num2:
    print("First is greater")
else:
    print("Second is greater")


# 66. Check if a number is divisible by 2 OR 5.

num = 10

if num % 2 == 0 or num % 5 == 0:
    print("Number is divisible by either 2 or 5")
else:
    print("Number is not divisible by either 2 or 5")


# 67. Create a dictionary with 3 employees and their salaries. Print the salary of the employee with the highest pay.


salaries = {"Siddiq":100000,"Bob":80000,"Mahesh":60000}

highest_salary = max(salaries.values())

print("Highest salary:",highest_salary)


# 68. Check if a string entered by the user contains both "a" and "b".

text = input("Enter a string:")

if "a" in text and "b" in text:
    print("String contains both a and b")
else:
    print("String does not contain both a and b")


# 69. Store 5 subjects in a tuple. Ask the user to enter a subject name. If it exists, print "Subject Found", else "Not Found".

subjects = ("Math","Science","English","Social","Telugu")

user_sub = input("Enter a subject name:")
if user_sub in subjects:
    print("Subject found")
else:
    print("Subject is not found")

# 70. Check if a number entered by the user is both even and between 10 and 50.

num = int(input("Enter a number:"))

if num % 2 == 0 and num >= 10 and num <= 50:
    print("Number is even and between 10 and 50")
else:
    print("Number is not even and between 10 and 50")

# . Strings – Built-in Practice (71–80)
# 71.Convert a string to uppercase.

name = "siddiq"

print(name.upper())

# 72.Convert a string to lowercase.

name = "SIDDIQ"
print(name.lower())

# 73.Remove extra spaces from a string.

name = "  Siddiq  "

print(name.strip())

# 74.Replace one word in a string with another.

text = "Hello World"

new_text = text.replace("World","Siddiq")

print(new_text)

# 75.Split a string into a list of words.

text = "Hello World"

words = text.split()

print(words)


# 76.Join a list of words into a single string.

words = ["Hello","World"]

sen = " ".join(words)

print(sen)

# 77.Count how many times a letter appears in a string.

text = "Hello World"

count = text.count("o")

print(count)


# 78.Find the position of a character in a string.

text = "Python"

position = text.find("o")

print(position)


# 79.Check if a string contains only letters and numbers.

text = "Python123"

print(text.isalnum())

# 80.Check if a string contains only digits.


text = "12345"

print(text.isdigit())

#  Lists – Built-in Practice (81–90)
# 81. Add an element to the end of a list.

numbers = [10,20,30]
numbers.append(40)

print(numbers)

# 82. Add multiple elements to a list at once.

numbers = [10,20,30]
numbers.extend([40,50,60])

print(numbers)

# 83. Insert an element at a specific position in a list.

numbers = [10,20,30]
numbers.insert(1,15)

print(numbers)

# 84. Remove a specific element from a list.

numbers = [10,20,30,40,50]

numbers.remove(30)

print(numbers)


# 85. Remove the last element from a list.

numbers = [10,20,30,40,50]

numbers.pop()

print(numbers)


# 86. Arrange the elements of a list in ascending order.

numbers = [20,30,40,10,15]

numbers.sort()
print(numbers)


# 87. Reverse the order of elements in a list.

numbers = [10,20,30,40,50]

numbers.reverse()

print(numbers)


# 88. Find the position of an element in a list.

numbers = [10,20,30,40,50]

position = numbers.index(30)

print(position)


# 89. Count how many times a number appears in a list.

numbers = [10,20,30,10,20,10]

count = numbers.count(10)

print(count)

# 90. Remove all elements from a list.

numbers = [10,20,30,40,50]

numbers.clear()

print(numbers)


#  Dictionaries – Built-in Practice (91–100)


# 91. Print all keys of a dictionary.

student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad" }

print(student.keys())

# 92. Print all values of a dictionary.

student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad" }

print(student.values())


# 93. Print all key-value pairs of a dictionary.


student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad" }

print(student.items())


# 94. Access the value of a key safely.

student = {
    "name": "Siddiq",
    "age": 23
}

print(student.get("city","key not found"))

# 95. Add a new key-value pair to a dictionary.

student = {
    "name": "Siddiq",
    "age": 23
}

student["city"] = "Hyderabad"

print(student)


# 96. Remove a specific key from a dictionary.

student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad"
}

student.pop("age")

print(student)


# 97. Remove the last inserted item from a dictionary.

student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad"
}

student.popitem()

print(student)

# 98. Check if a key exists in a dictionary.

student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad"
}

print("name" in student)

# 99. Create a dictionary with given keys and the same default value.

keys = ["a","b","c"]

new_dict = dict.fromkeys(keys,0)

print(new_dict)

# 100. Make a copy of a dictionary.

student = {
    "name": "Siddiq",
    "age": 23,
    "city": "Hyderabad"
}

copy_dict = student.copy()

print(copy_dict)

# Python Coding Questions 

#  Lists
# 1. Write a loop that prints only the even numbers from a list.

numbers = [10, 15, 20, 25, 30, 35]

for num in numbers:
    if num % 2 == 0:
        print(num)

# 2. Given a list of integers, use a loop and conditionals to separate positive and negative numbers into two new lists.

numbers = [10,-5,20,-8,15,-2]

positive = []
negative = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive Numbers:",positive)
print("Negative Numbers:",negative)

# 3. Write a loop that prints "Big" if a list element is greater than 50, otherwise print "Small".

numbers = [25,60,45,80,30]

for num in numbers:
    if num > 50:
        print("Big")
    else:
        print("Small")

# 4. Use a loop to count how many elements in a list are divisible by 3.

numbers = [3,5,9,12,14,18]

count = 0

for num in numbers:
    if num % 3 == 0:
        count += 1

print("count:",count)

# 5. Write a loop that replaces all negative numbers in a list with 0.

numbers = [10,-5,20,-8,15]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)

#  Tuples

# 6. Write a loop that prints elements of a tuple only if they are greater than 10.

numbers = (5,12,8,20,15)

for num in numbers:
    if num > 10:
        print(num)


# 7. Given a tuple of numbers, use a loop to print "Odd" or "Even" for each element.

numbers = (10,15,22,7,30)

for num in numbers:
    if num % 2 == 0:
        print(num,"- Even")
    else:
        print(num,"- odd")


# 8. Write a loop that finds the largest odd number in a tuple.

numbers = [12,45,33,28,51,19]

largest_odd = 0

for num in numbers:
    if num % 2 != 0 and num > largest_odd:
        largest_odd = num

print("Largest odd number:",largest_odd)

# 9. Use a loop to count how many elements in a tuple are prime numbers.

numbers = (2,4,5,7,9,11)

count = 0

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

print("Prime numbers count:",count)

# 10. Write a loop that prints "High" if a tuple element is above 100, otherwise "Low".

numbers = (50,120,80,150,30)

for num in numbers:
    if num > 100:
        print("High")
    else:
        print("Low")

# Sets
# 11. Write a loop that prints only odd numbers from a set.

numbers = {10, 15, 22, 7, 30, 9}

for num in numbers:
    if num % 2 != 0:
        print(num)

# 12. Given a set of integers, use a loop to remove all numbers less than 5.

numbers = {1,3,5,7,2,9}

for num in list(numbers):
    if num < 5:
        numbers.remove(num)

print(numbers)

# 13. Write a loop that prints "Found" if the set contains the number 10, otherwise "Not Found".

numbers = {5,10,15,20}

found = False

for num in numbers:
    if num == 10:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")

# 14. Use a loop to build a new set containing only squares of even numbers from another set.

numbers = {1, 2, 3, 4, 5, 6}

even_squares = set()

for num in numbers:
    if num % 2 == 0:
        even_squares.add(num ** 2)

print(even_squares)

# 15. Write a loop that prints "Duplicate" if an element already exists in a set while iterating through a list.

numbers = [1,2,3,2,4,1]

seen = set()

for num in numbers:
    if num in seen:
        print(num,"- Duplicate")
    else:
        seen.add(num)

# Strings
# 16. Write a loop that counts vowels in a string using conditionals.

text = "Python Programming"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowel count:",count)

# 17. Use a loop to print "Digit" if a character is numeric, otherwise print "Letter".

text = "Python123"

for ch in text:
    if ch.isdigit():
        print(ch,"- Digit")
    else:
        print(ch,"- Letter")


# 18. Write a loop that prints only uppercase characters from a string.

text = "PYTHon PROgRAMming"

for ch in text:
    if ch.isupper():
        print(ch)

# 19. Given a string, use a loop to count how many times "a" appears.

text = "banana"

count = 0

for ch in text:
    if ch == "a":
        count += 1

print("Count of a:",count)

# 20. Write a loop that prints "Palindrome" if a string reads the same forward and backward, otherwise "Not Palindrome".

text = "madam"

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#  Dictionaries
# 21. Write a loop that prints dictionary keys only if their values are greater than 50.

marks = {"Math": 75,"Science": 45,"English": 90}

for key,value in marks.items():
    if value > 50:
        print(key)

# 22. Given a dictionary of student names and marks, use a loop to print "Pass" if marks ≥ 40, otherwise "Fail".

students = {"Siddiq": 85,"Bob": 35,"Mahesh": 60}

for name, marks in students.items():
    if marks >= 40:
        print(name,"- pass")
    else:
        print(name,"- Fail")

# 23. Write a loop that counts how many dictionary values are even.

numbers = {"a":10,"b":15,"c":20,"d":7}

count = 0

for values in numbers.values():
    if values % 2 == 0:
        count += 1

print("Even values count:",count)

# 24. Use a loop to print "Starts with A" if a key begins with "A", otherwise print "Other".

students = {"Siddiq": 90,"Bob": 85,"Arjun": 78,"Mahesh": 88}

for key in students.keys():
    if key.startswith("A"):
        print(key,"- starts with A")
    else:
        print(key,"- other")

# 25. Write a loop that finds the maximum value in a dictionary and prints the corresponding key

employees = {"Bob": 50000,"Siddiq": 65000,"Mahesh": 55000}

max_key = ""
max_value = 0

for key, value in employees.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Employee with max salary:", max_key)
print("Salary:",max_value)


# Mixed Loops + Conditionals

# 26. Write a loop that prints numbers from 1 to 20, but skips multiples of 5.

for num in range(1,21):
    if num % 5 == 0:
        continue

    print(num)

# 27. Use a loop to print numbers from 1 to 15, but stop when you reach 10.

for num in range(1,21):
    if num == 10:
        break

    print(num)

# 28. Write a loop that prints "Prime" if a number is prime, otherwise "Not Prime", for numbers 2–20.

for num in range(2,21):
    is_prime =True

    for i in range(2,num):
        if num % 2 == 0:
            is_prime = False
            break 
    if is_prime:
        print(num,"- Prime")
    else:
        print(num,"- Not Prime")

# 29. Use a loop to print squares of numbers from 1 to 10, but only if the square is less than 50.

for num in  range(1,11):
    square = num ** 2

    if square < 50:
        print(square)

# 30. Write a loop that iterates through a list of tuples (name, age) and prints "Adult" if age ≥ 18, otherwise "Minor".

people = [("Siddiq",23),("Bob",17),("Mahesh",26)]

for name,age in people:
    if age >= 18:
        print(name,"- Adult")
    else:
        print(name,"- Minor")