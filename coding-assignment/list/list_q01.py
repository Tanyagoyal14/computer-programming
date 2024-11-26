'''
1. Find the Second Largest Element in an Array
Scenario:
A company is evaluating scores from a competition and needs to identify the second-highest score.

Problem Statement:
Write a program to find the second largest element in an array of integers.

Input Format:

The first line contains an integer n, the number of elements in the array.
The second line contains n space-separated integers representing the elements of the array.
Output Format:

Print the second largest element in the array.
Example:
Input:

6  
10 20 4 45 99 77
Output:

77
'''
n = int(input())
arr = list(map(int,input().split()))
arr = list(set(arr))
arr.sort(reverse=True)
if len(arr)>=2:
    print(arr[1])
else:
    print("no second largest number")