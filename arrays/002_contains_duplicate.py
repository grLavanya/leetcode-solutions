# ============================================
# CONTAINS DUPLICATE
# Link: leetcode.com/problems/contains-duplicate/
# ============================================

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
