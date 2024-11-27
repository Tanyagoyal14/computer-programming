# Count Occurrences of Each Element
def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences
print(count_occurrences([1, 2, 2, 3, 3, 3]))  