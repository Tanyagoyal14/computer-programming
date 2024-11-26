 # Check if an element exists in a tuple.

# Solution 1:
def element_exists(tup, value):
    return value in tup

# Solution 2:
tup = (10, 20, 30, 40, 50)
exists = 30 in tup
print(exists)  # Output: True  