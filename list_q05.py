'''
. Find the Intersection of Two Arrays
Scenario:
Two research teams are comparing overlapping samples.

Problem Statement:
Write a program to find the intersection of two arrays.

Input Format:

The first line contains an integer n, the size of the first array.
The second line contains n space-separated integers.
The third line contains an integer m, the size of the second array.
The fourth line contains m space-separated integers.
Output Format:

Print the elements in the intersection of the two arrays.
Example:
Input:

5  
1 2 3 4 5  
4  
3 4 5 6
Output:

3 4 5
'''
n = int(input())  
arr1 = list(map(int, input().split()))  
m = int(input())  
arr2 = list(map(int, input().split()))  
set1 = set(arr1)
set2 = set(arr2)
intersection = set1.intersection(set2)
print(*sorted(intersection))
