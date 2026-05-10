# ============================================
# CONTAINS DUPLICATE
# Link: leetcode.com/problems/valid-anagram/
# ============================================

# ---------------------------
# Approach 1: Brute Force
# Time: O(n²) | Space: O(n)
# ---------------------------
# Convert t to a list to allow for character removal.
# First, check if the lengths of s and t are different. If they are, return False.
# Then, for each character in s, check if it exists in t. If it does,
# remove that character from t to prevent reuse.
# If any character in s is not found in t, return False.

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         t = list(t)
#         if len(s) != len(t):
#             return False
#         for ch in s:
#             if ch in t:
#                 t.remove(ch)
#             else:
#                 return False
#         return True

'''
---------------------------
My Submission: Using String Count Function
Time: O(n²) | Space: O(n)
---------------------------
# This approach is not efficient because the count function itself is O(n),
# and we are calling it for each element in the list, leading to O(n²) time complexity.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for ch in set(s):
                if t.count(ch) != s.count(ch):
                    return False
            return True
'''

# ---------------------------
# Approach 2: Sorting
# Time: O(n log n) | Space: O(n)
# ---------------------------
# Sort both strings and compare them. If they are the same, they are anagrams.

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# ---------------------------
# Approach 3: Hash Map (Using Counter from collections)
# Time: O(n) | Space: O(n)
# ---------------------------
# Here we import Counter from the collections module.
# This allows us to create a hash map that counts the frequency of each
# character in both strings. If the two Counters are equal, the strings are anagrams.

from collections import Counter
# The import statement is placed at the top of the file, as is standard practice in Python.
# It can be placed at the very top, i.e., even before the comments begin.
# PEP 8 (Python's style guide) recommends it for cleanliness
# and to avoid confusion about where imports are located.
# However, for the sake of readability and to keep the code organized, it is often placed
# after the initial comments and before the class definition.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# What I learned:
# - Although sorting is instinctively the method we first think of,
# using Counter is more efficient — it counts character frequencies
# in one single pass, reducing time complexity from O(n log n) to O(n).
# - In simple words:
# - Using Counter from collections is a clean and efficient way to solve this problem.