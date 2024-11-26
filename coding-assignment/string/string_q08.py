'''
Count Frequency of Each Character
Problem: Write a function to count the frequency of each character in a string.

Scenario: You are analyzing text data and need to find the frequency of individual characters.

Example:

Input: "apple"
Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
'''
# Input
input_string = input()  # Input string

# Step 1: Initialize an empty dictionary to store frequencies
char_frequency = {}

# Step 2: Iterate through each character in the string
for char in input_string:
    # Update frequency count for the character
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Step 3: Output the result
print(char_frequency)
