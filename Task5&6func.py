# Functions Coding Questions
# List-based Questions
# 1.Write a function that takes a list of numbers and returns the sum.

def list_sum(numbers):
    return sum(numbers)
nums = [1,2,3,4,5]
print(list_sum(nums))

# 2. Pass a list of strings to a function and return the longest string.

def longest_string(words):
    return max(words,key=len)
word_list = ["apple","banana","watermelon","orange"]
print(longest_string(word_list))

# 3. Create a function that accepts a list and returns a new list with duplicates removed.

def remove_duplicates(items):
    return list(set(items))

numbers = [1,2,3,4,5,2,3,1]
print(remove_duplicates(numbers))

# 4. Write a function that takes a list of integers and returns only the even numbers.

def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
nums = [1,2,3,4,5,6,7,8,9,10]
print(even_numbers(nums))

# 5. Pass a list of numbers and return the maximum and minimum values.

def max_min(numbers):
    return max(numbers), min(numbers)

nums = [10,5,20,8]
print(max_min(nums))

# 6. Write a function that takes a list and returns it reversed.

def reverse_list(items):
    return items[::-1]
numbers = [1,2,3,4,5]
print(reverse_list(numbers))

# 7. Create a function that accepts a list of words and returns them sorted alphabetically.

def sort_words(words):
    return sorted(words)

names = ["banana","apple","cherry","date"]
print(sort_words(names))


# 8. Write a function that takes a list of integers and returns their average.

def average(numbers):
    return sum(numbers) / len(numbers)

nums = [10,20,30,40,50]
print(average(nums))

# 9. Pass a list of strings and return a list of their lengths.

def string_words(words):
    return [len(word) for word in words]

names = ["apple","banana","cherry","date"]
print(string_words(names))

# 10. Write a function that takes a list of numbers and returns the product of all elements.

def product(numbers):
    result = 1

    for num in numbers:
        result *= num 
    return result
    
nums = [1,2,3,4]
print(product(nums))


#  Tuple-based Questions
# 11. Write a function that takes a tuple of numbers and returns the sum.

def tuple_sum(numbers):
    return sum(numbers)
nums = (1,2,3,4,5)
print(tuple_sum(nums))

# 12. Pass a tuple of strings and return the shortest string.

def shortest_string(words):
    return min(words,key=len)
word_list = ("apple","banana","watermelon","orange")
print(shortest_string(word_list))

# 13. Create a function that accepts a tuple and returns it as a list.

def tuple_to_list(items):
    return list(items)

numbers = (1,2,3,4,5)
print(tuple_to_list(numbers))

# 14. Write a function that takes a tuple of integers and returns the count of odd numbers.

def count_odd(numbers):
    count = 0

    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count 
nums = (1,2,3,4,5,7)
print(count_odd(nums))

# 15. Pass a tuple of numbers and return the second largest value.

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

nums = (10,20,30,40)
print(second_largest(nums))

# 16. Write a function that takes a tuple and returns it reversed.

def reverse_tuple(items):
    return items[::-1]

nums = (1,2,3,4,5)
print(reverse_tuple(nums))

# 17. Create a function that accepts a tuple of words and returns them joined into a single string.

def join_words(words):
    return " ".join(words)
names = ("Hello","Python","World")
print(join_words(names))

# 18. Write a function that takes a tuple of integers and returns a tuple with each element squared.

def square_tuple(numbers):
    return tuple(num ** 2 for num in numbers)
nums = (1,2,3,4,5)
print(square_tuple(nums))

# 19. Pass a tuple of strings and return the one with the maximum vowels.

def max_vowels(words):
    def count_vowels(word):
        vowels = "aeiouAEIOU"
        return sum(1 for char in word if char in vowels)
    return max(words, key=count_vowels)
names = ("apple","banana","cherry","date")
print(max_vowels(names))


def max_vowels(words):
    vowels = "aeiou"

    return max(words, key=lambda word: sum(1 for char in word.lower() if char in vowels))

names = ("apple", "education", "sky", "orange")
print(max_vowels(names))

# 20. Write a function that takes a tuple and returns the number of unique elements.

def unique_count(items):
    return len(set(items))

nums = (1,2,3,4,5,2,3,1,5)
print(unique_count(nums))


# String-based Questions
#21.  Write a function that takes a string and returns it reversed.

def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello World"))

#22. Pass a string and return the count of vowels.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
print(count_vowels("Hello World"))

#23. Create a function that accepts a string and returns whether it is a palindrome.

def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("madam"))

#24. Write a function that takes a string and returns the frequency of each character.

def char_frequency(text):
    freq = {}

    for char in text:
        freq[char] = freq.get(char,0) + 1
    return freq

print(char_frequency("hello world"))


#25. Pass a string and return the first non-repeated character.

def first_non_repeated(text):
    for char in text:
        if text.count(char) == 1:
            return char
        
print(first_non_repeated("aaabbbcccddddefff"))

#26. Write a function that takes a string and returns it in uppercase.

def to_uppercase(text):
    return text.upper()
print(to_uppercase("hello world"))

#27. Create a function that accepts a string and returns the number of words.

def word_count(text):
    words = text.split()
    return len(words)

print(word_count("Python is easy to learn"))

#28. Write a function that takes a string and returns all unique characters.

def unique_characters(text):
    return set(text)
print(unique_characters("programming"))

#29. Pass a string and return the most frequent character.

def most_frequent(text):
    return max(text, key=text.count)
print(most_frequent("success"))

#30. Write a function that takes a string and returns it without spaces

def remove_spaces(text):
    return text.replace(" ","")
print(remove_spaces("Hello world python"))


# Dictionary-based Questions
# 31. Write a function that takes a dictionary and returns the sum of all values.

def sum_values(data):
    return sum(data.values())

numbers = {"a": 10, "b": 20, "c": 30}
print(sum_values(numbers))

# 32. Pass a dictionary and return the key with the maximum value.

def max_value_key(data):
    return max(data, key=data.get)

numbers = {"a": 10, "b": 50, "c": 30}
print(max_value_key(numbers))

# 33. Create a function that accepts a dictionary and returns a list of all keys.

def get_keys(data):
    return list(data.keys())

student = {"name":"Siddiq", "age":23, "city":"Hyderabad"}
print(get_keys(student))

# 34. Write a function that takes a dictionary and returns a list of all values.

def get_values(data):
    return list(data.values())

student = {"name":"Siddiq", "age":23, "city":"Hyderabad"}
print(get_values(student))

# 35. Pass a dictionary and return a new dictionary with keys and values swapped.

def swap_dict(data):
    return {value : key for key, value in data.items()}

data = {"a": 1, "b": 2, "c": 3}
print(swap_dict(data))

# 36. Write a function that takes a dictionary and returns the number of items.

def item_count(data):
    return len(data)

student = {"name":"Siddiq", "age":23}
print(item_count(student))

# 37. Create a function that accepts a dictionary and returns whether a given key exists.

def key_exists(data,key):
    return key in data

student = {"name":"Siddiq", "age":23}
print(key_exists(student,"age")) 

# 38. Write a function that takes a dictionary and returns the average of numeric values.

def average_values(data):
    return sum(data.values()) / len(data)

marks = {"Math": 85, "Science": 90, "English": 80}
print(average_values(marks))

# 39. Pass a dictionary and return the key with the longest string value.

def longest_value_key(data):
    return max(data, key=lambda key: len(data[key]))
info = {"a": "cat","b": "elephant","c": "dog"}
print(longest_value_key(info))

# 40. Write a function that takes a dictionary and returns a sorted list of keys.

def sorted_keys(data):
    return sorted(data.keys())
student = {"name":"Siddiq", "age":23, "course":"Python"}
print(sorted_keys(student))

#  Mixed Data Structure Questions
# 41. Write a function that takes a list of tuples and returns the tuple with the largest sum.

def largest_sum_tuple(data):
    return max(data, key = sum)

nums = [(1,2),(3,4),(5,6)]
print(largest_sum_tuple(nums))  

# 42. Pass a dictionary of lists and return the length of the longest list.

def longest_list_length(data):
    return max(len(value) for value in data.values())

items = {"a": [1, 2], "b": [1,2,3,4], "c": [5]}
print(longest_list_length(items))

# 43. Create a function that accepts a list of strings and returns a dictionary with word lengths.

def word_lengths(words):
    return {word: len(word) for word in words}

names = ["apple","banana","cherry"]
print(word_lengths(names))

# 44. Write a function that takes a tuple of strings and returns a dictionary with frequency of each word.

def word_frequency(words):
    freq = {}

    for word in words:
        freq[word] = freq.get(word,0)+ 1
    return freq 

data = ("apple","banana","apple","cherry","banana")
print(word_frequency(data))

# 45. Pass a list of dictionaries and return the dictionary with the maximum value for a given key.

def max_by_key(data,key_name):
    return max(data, key=lambda item: item[key_name])

students = [{"name": "Siddiq", "marks": 80},{"name": "Bob", "marks": 95},{"name": "Mahesh", "marks": 75}]
print(max_by_key(students,"marks"))

# 46. Write a function that takes a string and returns a dictionary with counts of each word.

def word_count(text):
    words = text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word,0) + 1
    return freq

print(word_count("hello world hello python"))

# 47. Create a function that accepts a list of numbers and returns a tuple of (sum, average, max, min).

def statistics(numbers):
    total = sum(numbers)
    avg = total / len(numbers)

    return (total, avg, max(numbers), min(numbers))
nums = [10,20,30,40]
print(statistics(nums))

# 48. Write a function that takes a tuple of strings and returns a list of strings sorted by length.

def sort_by_length(words):
    return sorted(words, key = len)
names = ("apple","banana","cherry","date")
print(sort_by_length(names))

# 49. Pass a dictionary of tuples and return the tuple with the maximum length.

def longest_tuple(data):
    return max(data.values(),key = len)
items = {"a": (1, 2),"b": (1, 2, 3, 4),"c": (5,)}

print(longest_tuple(items))

# 50. Write a function that takes a list of strings and returns a dictionary grouping them by their first letter.

def group_by_first_letter(words):
    result = {}

    for word in words:
        first = word[0]

        if first not in result:
            result[first] = []

        result[first].append(word)
    return result
names = ["apple","banana","cherry","date","avocado"]
print(group_by_first_letter(names))


#  Integer Function Questions (51–60)
# 51. Write a function that takes an integer and returns whether it is prime.

def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
print(is_prime(7))

# 52. Pass an integer to a function and return its factorial.

def factorial(number):
    result = 1

    for i in range(1,number + 1):
        result *= i
    return result 
print(factorial(5))

# 53. Create a function that accepts an integer and returns the sum of its digits.

def sum_of_digits(number):
    total = 0

    for digit in str(number):
        total += int(digit)
    return total
print(sum_of_digits(1234))

# 54. Write a function that takes an integer and returns whether it is an Armstrong number.

def is_armstrong(number):
    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == number
print(is_armstrong(153))

# 55. Pass an integer and return the reverse of its digits.

def reverse_digits(number):
    return int(str(number)[::-1])
print(reverse_digits(12345)) 

# 56. Write a function that takes an integer and returns whether it is a palindrome number.

def is_palindrome_number(number):
    return str(number) == str(number)[::-1]
print(is_palindrome_number(12321))

# 57. Create a function that accepts an integer and returns the count of even digits in it.

def count_even_digits(number):
    count = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            count += 1
    return count

print(count_even_digits(248913))
        
# 58. Write a function that takes an integer and returns the next Fibonacci number after it.

def next_fibonacci(number):
    a, b = 0, 1

    while b <= number:
        a, b = b, a + b
    return b
print(next_fibonacci(10))

# 59. Pass an integer and return the greatest common divisor (GCD) of that integer and another fixed number.

def gcd(number):
    fixed_number = 12

    while fixed_number:
        number, fixed_number = fixed_number, number % fixed_number
    return number
print(gcd(36))

# 60. Write a function that takes an integer and returns a list of all its divisors.

def divisiors(number):
    result = []

    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result
print(divisiors(12))


#  Map (10 Coding Questions)
# 1. Use map() to square each number in [2, 4, 6, 8].

numbers = [2, 4, 6, 8, 10]
result = list(map(lambda x: x ** 2, numbers))
print(result)

# 2. Convert an array of strings ["apple", "banana", "cherry"] into uppercase using map().

fruits = ["apple", "banana", "cherry"]
result = list(map(lambda x: x.upper(),fruits))
print(result)

# 3. Extract the id property from an array of objects: [{id:1,name:"A"}, {id:2,name:"B"}, {id:3,name:"C"}]

data = [{"id":1,"name":"A"}, {"id":2,"name":"B"}, {"id":3,"name":"C"}]
result = list(map(lambda x: x["id"], data))
print(result)

# 4. Add 5 to each element in [10, 20, 30] using map().

numbers = [10,20,30]
result = list(map(lambda x: x + 5, numbers))
print(result)

# 5. Convert an array of numbers [1,2,3,4] into strings using map().

numbers = [1,2,3,4]
result = list(map(str,numbers))
print(result)

# 6. Use map() to append "!" to each word in ["hi","hello","hey"].

words = ["hi","hello","hey"]
result = list(map(lambda x: x + "!", words))
print(result)

# 7. Create a new array of lengths from ["dog","elephant","cat"].

animals = ["dog","elephant","cat"]
result = list(map(len, animals))
print(result)

# 8. Use map() to transform [true,false,true] into ["YES","NO","YES"].

values = [True, False, True]
result = list(map(lambda x: "YES" if x else "NO", values))
print(result)

# 9. Given [1,2,3], use map() to return [1,4,9].

numbers = [1,2,3]
result = list(map(lambda x: x ** 2, numbers))
print(result)

# 10. Use map() to add a fullName property to each object in:[{first:"John",last:"Doe"}, {first:"Jane",last:"Smith"}]

people = [{"first":"John","last":"Doe"}, {"first":"Jane","last":"Smith"}]
result = list(map(lambda x : {**x,"fullName": x["first"] + " " + x["last"]}, people))
print(result)


#  Filter (10 Coding Questions)
# 1. Use filter() to get even numbers from [1,2,3,4,5,6].

numbers = [1,2,3,4,5,6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# 2. Filter out words shorter than 4 letters from ["hi","hello","hey","world"].

words = ["hi","hello","hey","world"]
result = list(filter(lambda x : len(x)<= 4, words))
print(result)

# 3. From [10,25,30,45], filter numbers greater than 20.

numbers = [10,25,30,45]
result = list(filter(lambda x: x > 20, numbers))
print(result)

# 4. Use filter() to get only truthy values from [0,1,false,2,"",3].

values = [0,1,False,2,"",3]
result = list(filter(bool, values))
print(result)

# 5. Filter out negative numbers from [5,-3,9,-1,0].

numbers = [5,-3,9,-1,0]
result = list(filter(lambda x: x <= 0, numbers))
print(result)

# 6. Use filter() to get names starting with "A" from ["Alice","Bob","Andrew","Charlie"].

names = ["Alice","Bob","Andrew","Charlie"]
result = list(filter(lambda x: x.startswith("A"), names))
print(result)

# 7. From [100,200,300,400], filter numbers divisible by 200.

numbers = [100,200,300,400]
result = list(filter(lambda x: x % 200 == 0, numbers))
print(result)

# 8. Use filter() to get objects with age > 18 from:[{name:"Tom",age:15},{name:"Jerry",age:20}]

people = [{"name":"Tom","age":15},{"name":"Jerry","age":20}]
result = list(filter(lambda x: x["age"] > 18, people))
print(result)

# 9. Filter out duplicate values from [1,2,2,3,4,4,5] using filter().

numbers = [1,2,2,3,4,4,5]
result = list(filter(lambda x: numbers.count(x) == 1, numbers)) 
print(result)

# ===================================
numbers = [1, 2, 2, 3, 4, 4, 5]

seen = []

result = list(filter(lambda x: x not in seen and not seen.append(x), numbers))

print(result)
# ======================================================

# 10. From ["red","blue","green","yellow"], filter colors containing "e".

colors = ["red","blue","green","yellow"]
result = list(filter(lambda x : "e" in x, colors))
print(result)

#  Reduce (10 Coding Questions)
# 1. Use reduce() to sum [1,2,3,4,5].

from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

# 2. Find the maximum number in [10,25,30,5] using reduce().

from functools import reduce
numbers = [10,25,30,5]
result = reduce(lambda x,y: x if x > y else y, numbers)
print(result)

# 3. Use reduce() to concatenate ["a","b","c"] into "abc".

from functools import reduce
letters = ["a","b","c"]
result = reduce(lambda x,y: x + y, letters)
print(result)

# 4. Count occurrences of each element in [1,2,2,3,3,3] using reduce().

from functools import reduce

numbers = [1, 2, 2, 3, 3, 3]

result = reduce(lambda acc, x: {**acc,x: acc.get(x, 0) + 1},numbers,{})

print(result)


# ============================================
from functools import reduce
numbers = [1, 2, 2, 3, 3, 3]
def count_occurrences(acc, x):
    acc[x] = acc.get(x, 0) + 1
    return acc
result = reduce(count_occurrences, numbers, {})
print(result)
# =====================================================

# 5. Use reduce() to flatten [[1,2],[3,4],[5]] into [1,2,3,4,5].

from functools import reduce
lists = [[1,2],[3,4],[5]]
result = reduce(lambda x,y: x + y, lists)
print(result)

# 6. Calculate the product of [2,3,4] using reduce().

from functools import reduce
numbers = [2,3,4]
result = reduce(lambda x,y : x * y, numbers)
print(result)

# 7. Use reduce() to find the longest word in ["cat","elephant","dog"].

from functools import reduce
words = ["cat","elephant","dog"]
result = reduce(lambda x,y: x if len(x) > len(y) else y, words)
print(result)

# 8. Build an object mapping names to ages from:[{name:"Tom",age:15},{name:"Jerry",age:20}]

from functools import reduce
people = [{"name":"Tom","age":15},{"name":"Jerry","age":20}]

result = reduce(lambda acc, x: {**acc,x["name"]: x["age"]},people,{})
print(result)
# ===========================================

# 9. Use reduce() to reverse ["a","b","c"] into "cba".

from functools import reduce
letters = ["a","b","c"]
result = reduce(lambda x, y: y + x, letters)
print(result)

# 10. Calculate the average of [10,20,30,40] using reduce().

from functools import reduce
numbers = [10,20,30,40]  
total = reduce(lambda x,y : x + y, numbers)
average = total / len(numbers)
print(average)




