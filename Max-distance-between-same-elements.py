'''
Max distance between same elements 
Easy Accuracy: 50.34% Submissions: 16649 Points: 2
Given an array with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Example 1:

Input
n= 6
arr = {1, 1, 2, 2, 2, 1}

Output
5

Explanation
arr[] = {1, 1, 2, 2, 2, 1}
Max Distance: 5
Distance for 1 is: 5-0 = 5
Distance for 2 is : 4-2 = 2
Max Distance 5
Example 2:

Input
n = 12
arr = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}

Output
10

Explanation



arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}
Max Distance 10
maximum distance for 2 is 11-1 = 10
maximum distance for 1 is 4-2 = 2
maximum distance for 4 is 10-5 = 5
Your Task:
Complete maxDistance() function which takes both the given array and their size as function arguments and returns the maximum distance between 2 same elemenrs.


Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:

1<=T<=100
1<=N<=1000
'''

# Your task is to Complete this function
# functtion should return an integer
def maxDistance(arr, n):
    # Code here
    d={}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]].append(i)
        else:
            d[arr[i]]=[i]
    for i in d:
        d[i]=max(d[i])-min(d[i])
    return max(d.values())