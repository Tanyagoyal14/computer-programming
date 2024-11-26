'''
4. Count the Frequency of Elements
Scenario:
You need to analyze the frequency of keywords in search queries.

Problem Statement:
Write a program to count the frequency of each unique element in an array.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print each element and its frequency.
Example:
Input:

8  
4 5 6 5 4 6 5 6
Output:

4: 2  
5: 3  
6: 3

'''
n = int(input())
arr = list(map(int,input().split()))
c = {}
for i in arr:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
for key,value in c.items():
    print(f"{key} : {value}")