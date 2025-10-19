# Ref : https://leetcode.com/problems/longest-consecutive-sequence/


# Time and Space Complexity
# Time: O(n)
# Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # num_set = set(nums) provides fast O(1) lookups and removes duplicates
        num_set = set(nums)

        longest_streak = 0
        
        for num in num_set:

            # Start only if 'num' is the beginning of a sequence
            # num - 1 not in num_set ensures we only start counting from the first number in each consecutive sequence, avoiding duplicate work.
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count forward sequence
                # This loop counts consecutive numbers forward from the sequence start, building up the length until the sequence breaks.
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak


