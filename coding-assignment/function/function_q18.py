# Python3 code to demonstrate working of
# Join Tuples if similar initial element
# Using recursion

def join_tuples(test_list, index):
	if index == len(test_list) - 1:
		return test_list
	elif test_list[index][0] == test_list[index + 1][0]:
		test_list[index] += test_list[index + 1][1:]
		test_list.pop(index + 1)
		return join_tuples(test_list, index)
	else:
		return join_tuples(test_list, index + 1)
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
print("The original list is : " + str(test_list))
res = join_tuples(test_list, 0)
print("The extracted elements : " + str(res))
