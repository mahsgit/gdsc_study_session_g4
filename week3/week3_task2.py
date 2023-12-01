# Write a program that prints the following pattern.
# The program should accept the input for character
# The pattern consists of a series of lines
# The characters in each line should follow a specific pattern based on the line number.
# Use conditional statements to determine the pattern for each line.
# Use a loop to iterate through the lines and print the characters accordingly.
# You are not allowed to use functions in your code.
# Do not store the pattern or any intermediate results in variables.
pattern=input("Please Enter pattern to be printed: ")
vowel=['a','e','i','o','u']
if pattern  in vowel:
    print("vowels are not allowed ")
    
elif len(pattern)>2:
    print("only one character ")
else:
    for i in range(9):
        for j in range(i):
            print(pattern,end="")
        print()
            