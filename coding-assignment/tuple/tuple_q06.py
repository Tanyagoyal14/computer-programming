# Update each element in tuple list
# initialize add element
add_ele = 4

# Update each element in tuple list
# Using list comprehension
res = [tuple(j + add_ele for j in sub ) for sub in test_list]

# printing result
print("List after bulk update : " + str(res))
