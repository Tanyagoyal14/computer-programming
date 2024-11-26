'''
Find the Longest Word in a String
Problem: Write a function to find the longest word in a given sentence.

Scenario: You need to highlight the longest word from a text document.

Example:

Input: "The quick brown fox"
Output: "quick"
'''
# Input
sentence = input()  # Sentence input

# Step 1: Split the sentence into words
words = sentence.split()

# Step 2: Find the longest word
longest_word = max(words, key=len)

# Step 3: Output the longest word
print(longest_word)
