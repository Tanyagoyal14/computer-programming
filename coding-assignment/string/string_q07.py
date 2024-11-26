'''
Replace Spaces with %20 (URL Encoding)
Problem: Write a function that replaces all spaces in a string with %20.

Scenario: You are working on URL encoding where spaces must be replaced with %20.

Example:

Input: "hello world"
Output: "hello%20world"
'''
# Input
input_string = input()  # Input string with spaces

# Step 1: Replace all spaces with %20
encoded_string = input_string.replace(" ", "%20")

# Step 2: Output the result
print(encoded_string)
