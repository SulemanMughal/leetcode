# Ref : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

# ⏱️ Complexity
# Time: O(n)
# Space: O(1) extra

def removeDuplicates(nums):
    k = 0  
    for x in nums:
        # k < 2 guarantees the first two elements are always included, which is necessary to allow up to two duplicates as required by the problem.
        # x > nums[k - 2] prevents writing a third (or more) duplicate of the same number, enforcing the “at most two” rule.
        # nums[k - 2] lets us compare with the element two places back to detect if we’re about to add a third duplicate, which we want to skip. This enforces the “at most two” rule.
        # They build the result in-place at the start of nums, ensuring only the allowed elements are kept, and k always points to the next position to write.
        if k < 2 or x > nums[k - 2]:
            nums[k] = x
            k += 1
    return k, nums


nums = [1,1,1,2,2,3]
print("Input : ", nums)
print("Output : ", removeDuplicates(nums))