"""
You are given an array nums consisting of positive integers.
You have to take each integer in the array, reverse its digits,
and add it to the end of the array. You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array."""

def countDistinctIntegers(nums):
    s = set()
    for x in nums:
        s.add(x)
        s.add(int(str(x)[::-1]))
    return len(s)


print(countDistinctIntegers([1,13,10,12,31]))