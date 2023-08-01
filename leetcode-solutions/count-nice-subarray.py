def numberOfSubarrays(nums,k):
    # Convert the original array to the modified array
    modified = [1 if num % 2 != 0 else 0 for num in nums]
    #  Create the prefix sum array
    prefix_sum = [0] * (len(modified) + 1)
    for i in range(len(modified)):
        prefix_sum[i + 1] = prefix_sum[i] + modified[i]

    # Find the number of nice subarrays using prefix sum
    niceCount = 0
    # Initialize the count of prefix sum value 0 with 1
    count_dict = {0: 1} 

    for i in range(1, len(prefix_sum)):
        niceCount += count_dict.get(prefix_sum[i] - k, 0)
        count_dict[prefix_sum[i]] = count_dict.get(prefix_sum[i], 0) + 1


    return niceCount

