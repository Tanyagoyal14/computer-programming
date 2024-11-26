'''
Find All Subarrays with Zero Sum
Scenario:
You are analyzing financial data and need to identify periods where there was no net profit or loss.

Problem Statement:
Write a program to find all subarrays of an array that have a sum of zero.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print the starting and ending indices of all subarrays with zero sum.
Example:
Input:

6  
3 4 -7 1 3 3
Output:

[0, 2]  
[3, 4]
'''
n = int(input())  
arr = list(map(int, input().split()))  


for start in range(n):
    sum_subarray = 0
    for end in range(start, n):
        sum_subarray += arr[end]
        if sum_subarray == 0:
            print([start, end])
