# ============================================
# MAJORITY ELEMENT
# Link: leetcode.com/problems/majority-element/
# ============================================

# ---------------------------
# Approach 1: Brute Force
# Time: O(n²) | Space: O(1)
# ---------------------------
# This approach is not efficient because it counts the occurrences of each element in the
# list, leading to O(n²) time complexity.

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         for num in nums:
#             count = nums.count(num)
#             if count > (len(nums)/2):
#                 return num

# ---------------------------
# Approach 2: Hash Map using Counter from collections
# Time: O(n) | Space: O(n)
# ---------------------------
# This approach uses a hash map to count the occurrences of each element.
# The majority element is the one that appears more than ⌊n/2⌋ times.

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq > len(nums) // 2:
                return num
            
# Actually, this is how i wrote the code, but both are fine anyway.
# Just pasting here for reference:
# ---------------------------
# from collections import Counter:
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         for i in count:
#             if count[i] > (len(nums)/2):
#                 return i
# ----------------------------

'''
My Submission: Also uses hashmap but in a different method.
---------------------------
Submission: Similar to Approach 2 but with a different implementation
Time: O(n) | Space: O(n)
---------------------------
-> Line 5 — freq.get(i, 0) + 1
This is a safer way to count without Counter! .get(i, 0) means "get the value for key i,
but if it doesn't exist return 0 instead of an error."
Then +1 increments the count. Really clean! ✅
-> Line 6 — max(freq, key=freq.get)
This is the clever part!
It finds the key in the dictionary that has the highest value — meaning the element with
the highest frequency. The key=freq.get part tells max() to
compare by the dictionary values, not the keys. ✅

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        majority_element = max(freq, key = freq.get)
        return majority_element
'''

#--------------------------------------------------------------------------------------------

'''
IMPORTANT NOTE:
Notice the follow-up question on LeetCode — "solve it in O(n) time AND O(1) space!" 👀
That's a famous algorithm called Boyer-Moore Voting Algorithm — it's a bit
mind-bending but really clever.

BOYER-MOORE VOTING ALGORITHM:
1. Initialize two variables: `candidate` (to store the potential majority element) and
    `count` (to keep track of the count of the candidate).
2. Iterate through the list of numbers:
    - If `count` is 0, set the current number as the new `candidate` and reset `count` to 1.
    - If the current number is the same as the `candidate`, increment `count`.
    - If the current number is different from the `candidate`, decrement `count`.
3. After the loop, the `candidate` will be the majority element.
This algorithm works because the majority element will always have a count greater than
the sum of counts of all other elements combined. So, even if we decrement the count for
every different element, the majority element will still end up as the candidate at the end.
'''

# ---------------------------
# Approach 3: Boyer-Moore Voting Algorithm
# Time: O(n) | Space: O(1)
# ---------------------------
# This approach is efficient because it finds the majority element in a single pass
# through the list, using constant space.

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None
#         count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num  # new candidate!
#             if num == candidate:
#                 count += 1       # vote for candidate!
#             else:
#                 count -= 1       # cancel out!
#         return candidate         # majority element survives!

# What I learned:
# - The Boyer-Moore Voting Algorithm is a clever way to find the majority element
# in O(n) time and O(1) space.
# - It works by maintaining a candidate and a count, and effectively "cancelling out"
# non-majority elements against the majority candidate.