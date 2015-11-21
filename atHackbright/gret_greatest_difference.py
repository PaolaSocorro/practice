def greatest_diff(nums):
    if len(nums)>2:
        return None
    max = nums[0]
    min = nums[0]
    for num in nums:
        if min > max:
            max=min
        if max <  min:
            min= max
    return max - min


