'''
Find the Largest Sum Subarray
Scenario:
You need to identify the best-performing time periods in sales data.

Problem Statement:
Write a program to find the subarray with the largest sum.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print the largest sum.
Example:
Input:

5  
-2 1 -3 4 -1 2 1 -5 4
Output:

6
'''
# Input
n = int(input())  # size of the array
arr = list(map(int, input().split()))  # array elements

# Step 1: Initialize variables
current_sum = arr[0]
max_sum = arr[0]

# Step 2: Apply Kadane's Algorithm
for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

# Step 3: Output the largest sum
print(max_sum)
