# ============================================
# TWO SUM II - INPUT ARRAY IS SORTED
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# ============================================

# ---------------------------
# Approach 1: Brute Force
# Time: O(n²) | Space: O(1)
# ---------------------------
# This approach uses two nested loops to check every pair of numbers in the array.
# If the sum of any pair equals the target, their indices are returned.

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]
'''+ 1 because we need to return 1-based indices'''

# ---------------------------
# Approach 2: Two Pointers
# Time: O(n) | Space: O(1)
# ---------------------------
# This approach uses two pointers, one starting at the
# beginning of the array and the other at the end.
# If the sum of the numbers at the two pointers is less than the target,
# we move the left pointer to the right.
# If the sum is greater than the target, we move the right pointer to the left.
# If the sum equals the target, we return the indices of the two pointers.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1

# ----------------------------
# Approach 3: Binary Search
# Time: O(n log n) | Space: O(1)
# ----------------------------
# This approach iterates through the array and for each element,
# it uses binary search to find the complement (target - current element)
# in the remaining part of the array.
# If the complement is found, the indices of the current element
# and the complement are returned.

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             left = i + 1
#             right = len(numbers) - 1
#             complement = target - numbers[i]
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if numbers[mid] == complement:
#                     return [i + 1, mid + 1]
#                 elif numbers[mid] < complement:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

# What I learned:
# - The two-pointer approach is efficient for sorted arrays and can
# find the solution in O(n) time and O(1) space.
# - The binary search approach is also efficient but has a higher time complexity of
# O(n log n) due to the binary search for each element.

# Sorted arrays unlock smarter approaches than hash maps — Two Pointers
# works by moving left and right inward based on whether the sum is too
# big or too small, achieving O(n) time and O(1) space. Binary search
# also works but costs O(n log n) since you search for each element's
# complement individually.