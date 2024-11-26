'''
 Find the First Non-Repeating Character
Problem: Write a function to find the first non-repeating character in a string.

Scenario: You need to identify the first character in a string that does not repeat.

Example:

Input: "swiss"
Output: "w"
'''
# Input
input_string = input()  # Input string

# Step 1: Count the frequency of each character
char_count = {}

# Count occurrences of each character in the string
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Step 2: Find the first non-repeating character
for char in input_string:
    if char_count[char] == 1:
        print(char)
        break
