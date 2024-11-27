'''
Count Frequency of Each Character
Problem: Write a function to count the frequency of each character in a string.

Scenario: You are analyzing text data and need to find the frequency of individual characters.

Example:

Input: "apple"
Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
'''
# Input
input_string = input() 
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
