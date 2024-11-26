'''
Check if a String is Palindrome
Problem: Write a function to check if a given string is a palindrome.

Scenario: You need to verify if a user-entered string reads the same forward and backward.

Example:

Input: "madam"
Output: True

Input: "hello"
Output: False
'''
a = input()
if a == a[::-1]:
    print(True)
else:
    print(False)
