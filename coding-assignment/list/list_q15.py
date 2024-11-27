# Merge Two Sorted Lists
def merge_sorted_lists(lst1, lst2):
    i, j = 0, 0
    merged = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
