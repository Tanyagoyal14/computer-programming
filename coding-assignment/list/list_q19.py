#Flatten a Nested List
def flatten_list(nested_lst):
    flat_list = []
    for sublist in nested_lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list
print(flatten_list([[1, 2], [3, 4], [5, 6]]))  