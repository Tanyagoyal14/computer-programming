'''
Remove Spaces from a String
Problem: Write a function to remove all spaces from a given string.

Scenario: You are processing user input and need to remove any spaces for validation purposes.

Example:

Input: "hello world"
Output: "helloworld"
'''
# Input
input_string = input()  # User input string

# Step 1: Remove spaces from the string using replace()
output_string = input_string.replace(" ", "")

# Step 2: Output the result
print(output_string)
