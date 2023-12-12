"""filter functions

Example: Filtering even numbers from a list.
map function
Example: Double each number in a list.
try and catch
Example: take two numbers from the user and return the sum(validate user input)
Example: take two numbers from the users and divide the first number with the second one(try and catch division by zero error)"""

nums = [1, 2, 3, 4, 5, 6]
num = list(filter(lambda i: i % 2 == 0, nums))
double = list(map(lambda i: i * 2, nums))
print(num)
print(double)


a = int(input("enter num1"))
b = int(input("enter num2"))
try:
    a = int(a)
    b = int(b)
    # Code that might raise an exception
except ValueError as e:
    # Handle the exception
    print("you enter char")
else:
    c = a + b
    print(c)
    # Code that always runs


a = int(input("enter num1"))
b = int(input("enter num2"))
try:
    b == 0
    # Code that might raise an exception
except ZeroDivisionError as e:
    # Handle the exception
    print("error , divistion by zero " + e)
else:
    print(a / b)
    # Code that always runs
