#Sort a List of Tuples by the Second Item
def sort_by_second_item(tuples_lst):
    return sorted(tuples_lst, key=lambda x: x[1])
print(sort_by_second_item([(1, 3), (2, 1), (3, 2)]))  