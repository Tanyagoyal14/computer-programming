'''
Merge Two Sorted Arrays
Scenario:
You are building a tool to merge user data sorted by creation dates.

Problem Statement:
Write a program to merge two sorted arrays into a single sorted array.

Input Format:

The first line contains an integer n, the size of the first array.
The second line contains n sorted integers.
The third line contains an integer m, the size of the second array.
The fourth line contains m sorted integers.
Output Format:

Print the merged sorted array.
Example:
Input:

4  
1 3 5 7  
3  
2 4 6
Output:

1 2 3 4 5 6 7

'''
n = int(input())  
arr1 = list(map(int, input().split()))  
m = int(input())  
arr2 = list(map(int, input().split()))  
merged_array = arr1 + arr2
merged_array.sort()
print(*merged_array)
