# Find the Intersection of Two Lists
def intersection(lst1, lst2):
    return [item for item in lst1 if item in lst2]
print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  