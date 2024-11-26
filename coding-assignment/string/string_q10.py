'''
Check if Two Strings are Rotations of Each Other
Problem: Write a function to check if one string is a rotation of another string.

Scenario: You are developing a circular queue system and need to check if one sequence is a rotated version of another.

Example:

Input: "abcde", "deabc"
Output: True

Input: "abcde", "abced"
Output: False
'''
def are_rotations(s1, s2):
    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False
    
    # Concatenate s1 with itself
    concatenated = s1 + s1
    
    # Check if s2 is a substring of the concatenated string
    return s2 in concatenated

# Example usage
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Check if they are rotations
result = are_rotations(s1, s2)

# Output the result
print(result)