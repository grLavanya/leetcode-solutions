# ============================================
# VALID PALINDROME
# Link: https://leetcode.com/problems/valid-palindrome/
# ============================================

# ---------------------------
# Approach 1: Brute Force
# Time: O(n) | Space: O(n)
# ---------------------------
# This approach creates a new string that contains only alphanumeric characters.
# Then, the string is converted to lowercase and
# compared with its reverse to check if it's a palindrome.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ""
#         for ch in s:
#             if ch.isalnum():
#                 cleaned += ch
#         return cleaned.lower()[::-1] == cleaned.lower()

# ---------------------------
# Approach 2: Two Pointers
# Time: O(n) | Space: O(1)
# ---------------------------
# This approach uses two pointers to compare characters from the start and end of the string.
# It skips non-alphanumeric characters and compares
# the remaining characters in a case-insensitive manner.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1   # skip non-alphanumeric from left
            while left < right and not s[right].isalnum():
                right -= 1  # skip non-alphanumeric from right
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
# What I learned:
# While the brute force method cleans the string and compares it at the end (O(n) space),
# the two pointer method does everything in one loop without building a new string,
# bringing space complexity down to O(1).