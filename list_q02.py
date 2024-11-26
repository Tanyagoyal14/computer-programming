'''
2. Rotate an Array
Scenario:
You are tasked with implementing a feature for a digital carousel that rotates content based on user input.

Problem Statement:
Write a program to rotate an array k steps to the right.

Input Format:

The first line contains two integers, n (size of the array) and k (number of steps to rotate).
The second line contains n space-separated integers representing the elements of the array.
Output Format:

Print the rotated array.
Example:
Input:

6 2  
1 2 3 4 5 6
Output:

5 6 1 2 3 4
'''
n , k = map(int,input().split())
arr = list(map(int,input().split()))
rotated_arr= arr[-k:] + arr[:-k]
print(*rotated_arr)