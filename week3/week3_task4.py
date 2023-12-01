# Write a Python program to find and print the sum of all the even numbers from 1 to 50 (inclusive).
# Additionally, for each even number, if it is a multiple of 3, print "Three" instead of the number;
# if it is a multiple of 5, print "Five" instead of the number. Finally, print the total sum and the count of numbers
# replaced with "Three" or "Five."
even = 0
count = 0
for i in range(1, 51):
    if i % 2 == 0:
        even += i
        if i % 3 == 0:
            print("three")
            count += 1

        elif i % 5 == 0:
            print("five")
            count += 1
print(f"sum of even {even}  and count is {count}")
