'''Functions:
a) Write a function named greet that takes a person's name as an argument and prints a greeting message.
b) Write a function named add_numbers that takes two numbers as arguments and returns their sum.

Usage of *args:
a) Write a function named print_args that takes any number of arguments and prints them.
b) Write a function named calculate_average that takes any number of numbers as arguments and returns their average.
'''

def greet (name):
    print("hello "+name)
greet('abebe')


def add_number(a,b):
    print(a+b)
add_number(2,4)



def print_args(*args):
    for i in args:
        print(i,end=" ")
print_args(1,2,3,4,5)



def calculate_average(*args):
    print(sum(args)/len(args))
    
calculate_average(1,2,3)
