# Problem Description
# Remove all elements from a list that are equal to a given value.

# Ref Link : https://leetcode.com/problems/remove-element/

"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

"""




# nums = [0,1,2,2,3,0,4,2]
# val = 2
nums = [3,2,2,3]
val = 3


def removeElement(nums, val):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]  # move last into current
            n -= 1                 # shrink effective length
        else:
            i += 1
    # Optional visualization
    for j in range(n, len(nums)):
        nums[j] = '_'
    return n

# Example
nums =  [0,1,2,2,3,0,4,2]
k = removeElement(nums, 2)
print("Output:", k, nums)  # Output: 2, [2, 2, '_', '_']