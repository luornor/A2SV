"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
 The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
        """
    k = m+n-1
    num1_index = m-1
    num2_index = n-1
    while num1_index >=0 and num2_index>=0:
        if nums1[num1_index]>= nums2[num2_index]:
            nums1[k] = nums1[num1_index]
            num1_index-=1
        else:
            nums1[k] = nums2[num2_index]
            num2_index-=1
        k-=1
        

    
    



nums = [1,2,3,0,0,0]
# nums = [1]
# nums = [0]
merge(nums,3,[2,5,6],3)
# merge(nums,1,[],0)
# merge(nums,0,[1],1)
print(nums)