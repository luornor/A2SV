"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""


def validMountainArray(arr):
    n = len(arr)
    strict_increase = False
    strict_decrease = False
    max_val = max(arr)
    idx = arr.index(max_val)
    if n < 3:
        return False
    if idx==0 or idx==n-1:
        return False
    for i in range(idx):
        if arr[i]<arr[i+1]:
            strict_increase = True
        else:
            return False
    for i in range(idx,n-1):
        if arr[i]>arr[i+1]:
            strict_decrease = True
        else:
            return False
    return strict_increase and strict_decrease



print(validMountainArray([3,5,5]))