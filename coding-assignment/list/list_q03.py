'''
3. Find the Missing Number in a Sequence
Scenario:
A data logger is tracking sequential numbers but occasionally misses an entry. Your job is to identify the missing number.

Problem Statement:
Write a program to find the missing number in an array containing n unique integers from 1 to n+1.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print the missing number.
Example:
Input:

5  
1 2 4 5 6
Output:

3
'''
n = int(input())
arr = list(map(int,input().split()))
for i in range(1,n+1):
    if i not in arr:
        print(i)