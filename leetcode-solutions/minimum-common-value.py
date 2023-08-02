def getCommon(nums1,nums2):
    l = 0
    r = 0
    # com_min = -1
    while l<len(nums1) and r<len(nums2):
        if nums1[l]==nums2[r]:
            return nums1[l]
            r+=1
            l+=1
        elif nums1[l]<nums2[r]:
            l+=1
        else:
            r+=1

    return -1