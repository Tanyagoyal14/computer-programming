def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f'"{string}" is a palindrome')
else:
    print(f'"{string}" is not a palindrome')
