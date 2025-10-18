# 🧠 Problem Summary:
# You're given:
# nums1: an array of size m + n, with the first m elements sorted and valid, and the last n elements as placeholders (0s).
# nums2: an array of size n, sorted.

# 🎯 Goal:
# Merge nums2 into nums1 in-place, so that nums1 becomes a fully sorted array of size m + n.


# Time Complexity : O(m + n)
# Space Complexity : O(1)


def merge(nums1, m, nums2, n):
    # Set up pointers for nums1, nums2, and the merged array (from the end)
    p1 = m - 1  # Last valid element in nums1
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in nums1

    # Traverse backwards and fill nums1 from the back
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If any elements left in nums2, copy them
    nums1[:p2 + 1] = nums2[:p2 + 1]


# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


print("Before merging:", nums1, nums2, sep="\n")
merge(nums1, m, nums2, n)
print("After merging:", end=" ")
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]