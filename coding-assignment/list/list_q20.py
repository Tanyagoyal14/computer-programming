#Find the Longest Sublist
def find_longest_sublist(lst_of_lists):
    longest = lst_of_lists[0]
    for sublist in lst_of_lists:
        if len(sublist) > len(longest):
            longest = sublist
    return longest
print(find_longest_sublist([[1], [1, 2], [1, 2, 3]]))  