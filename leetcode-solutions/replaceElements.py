"""
Given an array arr, replace every element in that array with the greatest element 
among the elements to its right, and replace the last element with -1.
After doing so, return the array."""

def replaceElements(arr: list[int]) -> list[int]:
    max_right=-1
    n = len(arr)
    for i in range(n-1,-1,-1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(current,max_right)

    return arr


print(replaceElements([17,18,5,4,6,1]))