# Count the occurrences of an element in a tuple.

# Solution 1:
def count_element(tup, value):
    return tup.count(value)

# Solution 2:
tup = (1, 2, 2, 3, 2, 4, 2)
count = tup.count(2)
print(count)  # Output: 4 