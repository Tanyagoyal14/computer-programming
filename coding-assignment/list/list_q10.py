'''
Find Pairs with Given Sum
Scenario:
You are tasked with matching items from two different catalogs based on a target cost.

Problem Statement:
Write a program to find all pairs of integers in an array that sum to a target value.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
The third line contains the target sum.
Output Format:

Print all pairs of integers.
Example:
Input:

5  
1 2 3 4 5  
5
Output:

1 4  
2 3
'''
# Input
n = int(input())  # size of the array
arr = list(map(int, input().split()))  # array of integers
target_sum = int(input())  # target sum

# Step 1: Initialize an empty set to store visited elements
visited = set()

# Step 2: Iterate through the array
for num in arr:
    complement = target_sum - num
    
    # Step 3: Check if the complement is in the visited set
    if complement in visited:
        print(complement, num)
    
    # Step 4: Add the current number to the visited set
    visited.add(num)
