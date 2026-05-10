# ============================================
# CONTAINS DUPLICATE
# Link: leetcode.com/problems/contains-duplicate/
# ============================================

'''
My Submissions:
1. Using nested loops to compare each element with every other element.
(Approach 1)
# Note: This got Time Limit Exceeded on LeetCode for large inputs!
---------------------------
2. Using a set to track seen numbers. If a number is already in the set, return True.
    Time: O(n) | Space: O(n)
# There is a possibility that this method can be fatser because it stops executing as soon as
# a duplicate is found, while the set conversion method always processes the entire list.
---------------------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
'''

# ---------------------------
# Approach 1: Brute Force
# Time: O(n²) | Space: O(1)
# ---------------------------
# For each element, check every other element after it
# and see if they are the same.

# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[j]==nums[i]:
#                     return True
#         return False

# ---------------------------
# Approach 2: Set Conversion
# Time: O(n) | Space: O(n)
# ---------------------------
# Convert the list to a set, which removes duplicates.
# If the set is smaller than the original list, there were duplicates.

# LONGER CODE
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         unique = set(nums)
#         if len(unique)!=len(nums):
#             return True
#         return False

# SHORTER CODE
class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)
    
# What I learned:
# - The 'no duplicates' rule in sets allows us to
# easily convert and compare the length in order to decide
# whether the given set contains duplicates or not.
# This is more clean and efficient compared to creating
# loops to check with each element individually until a match is detected.
# In other words:
# - Sets automatically remove duplicates.
# - So comparing lengths is a quick way to check for duplicates.