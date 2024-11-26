'''
 Check if Two Strings are Anagrams
Problem: Write a function to check if two strings are anagrams (i.e., they contain the same characters in different order).

Scenario: You are working on a text processing tool and need to check if two words are anagrams.

Example:

Input: "listen", "silent"
Output: True

Input: "apple", "pale"
Output: False

'''
# Input
str1, str2 = input().split()  # Get two strings as input

# Step 1: Sort both strings and compare
if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)
