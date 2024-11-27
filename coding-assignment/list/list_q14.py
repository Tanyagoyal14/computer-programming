#  Find the Index of the First Occurrence 
def find_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1
print(find_index([1, 2, 3, 4, 5], 3))  
print(find_index([1, 2, 3, 4, 5], 6))  
