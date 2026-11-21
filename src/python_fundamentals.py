# Python Fundamentals

print("Welcome to AI/ML Internship!")

name = "Varshini"
age = 18

print("Name:", name)
print("Age:", age)

# Basic calculations
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Python Data Types

student_name = "Varshini"
student_age = 18
percentage = 85.5
is_student = True

print("Name:", student_name)
print("Age:", student_age)
print("Percentage:", percentage)
print("Is Student:", is_student)

print(type(student_name))
print(type(student_age))
print(type(percentage))
print(type(is_student))

# If-Else Statement

marks = 75

if marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

# For Loop

print("Numbers from 1 to 5:")

for i in range(1, 6):
    print(i)

# While Loop

i = 1

while i <= 5:
    print(i)
    i = i + 1

# Strings

name = "Varshini"

print(name)
print(name.upper())
print(name.lower())
print(len(name))
print(name[0])

# List - Can be changed
fruits = ["Apple", "Mango", "Orange"]
fruits.append("Banana")
print("List:", fruits)

# Tuple - Cannot be changed
numbers = (10, 20, 30)
print("Tuple:", numbers)

# Set - Stores unique values
colors = {"Red", "Blue", "Green"}
print("Set:", colors)

# Dictionary - Stores key-value pairs
student = {
    "name": "Varshini",
    "age": 18,
    "course": "AI/ML"
}
print("Dictionary:", student)
print(student["name"])

# Functions

def greet(name):
    print("Hello", name)

greet("Varshini")

def add(a, b):
    return a + b

result = add(10, 20)
print("Addition:", result)

# File Handling

# Writing into a file
with open("sample.txt", "w") as file:
    file.write("Welcome to AI/ML Internship!")

# Reading the file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)