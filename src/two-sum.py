# Ref : https://leetcode.com/problems/two-sum/description/


# ⏱️ Time & Space Complexity
# Time: O(n) — single pass through the list
# Space: O(n) — for the hash map

def twoSum(nums, target):
    seen = {}  # key: number, value: index

    # enumerate(nums) is a Python built-in function that returns both the index and value from an iterable (like a list) as you loop through it.
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        
        # Records each number and its index so we can quickly look up if its complement exists later.
        seen[num] = i
