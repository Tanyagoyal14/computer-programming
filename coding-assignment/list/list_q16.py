# Find the Largest and Smallest Elements in a List
def find_largest_smallest(lst):
    largest = lst[0]
    smallest = lst[0]
    for item in lst[1:]:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item
    return largest, smallest
print(find_largest_smallest([1, 2, 3, 4, 5])) 

