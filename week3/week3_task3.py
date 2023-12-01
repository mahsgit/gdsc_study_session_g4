# Develop a program that checks if a user-inputted word is a palindrome. A palindrome is a word that reads the same backward as forward (e.g., "radar").
palindrom=input("enter word: ")
if palindrom==palindrom[::-1]:
    print("palindrom")
else:
    print("not palindrom")