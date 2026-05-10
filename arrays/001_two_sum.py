# ============================================
# TWO SUM
# Link: leetcode.com/problems/two-sum/
# ============================================

# ---------------------------
# Approach 1: Brute Force
# Time: O(n²) | Space: O(1)
# ---------------------------
# For each element, check every other element after it
# and see if they add up to target.

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]: 
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         # Return an empty list if no solution is found
#         return []

# ---------------------------
# Approach 2: Two-pass Hash Table
# Time: O(n) | Space: O(n)
'''This was my submission.'''
# ---------------------------
# Loop 1: store every number and its index in a dictionary.
# Loop 2: for each number, check if its complement exists in the dictionary.

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]]
#         # If no valid pair is found, return an empty list
#         return []

# ---------------------------
# Approach 3: One-pass Hash Table ✅
# Time: O(n) | Space: O(n)
# ---------------------------
# Single loop — check if complement already exists before adding current element.
# No risk of using the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

# What I learned:
# - Subtracting from target gives a definite value to search for
# - Dictionary lookups are O(1), which is what makes hash map faster than brute force
# - One-pass works by looking backwards — complement can only be something already stored