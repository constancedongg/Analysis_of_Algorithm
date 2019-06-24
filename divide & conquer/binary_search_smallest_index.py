


# Given sorted array nums, return the smallest index k which satisifies
# for all i >= k : nums[i] >= target
def binary_search_smallest(nums , target):
    l = 0 
    r = len(nums) - 1 
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

nums = [10, 20, 34, 45, 60 , 60 , 70]
target = 60
print(binary_search_smallest(nums , target))