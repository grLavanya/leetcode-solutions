class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        h = {}

        for i in range(len(nums)):

            h[nums[i]] = i

	 

        for i in range(len(nums)):

            y = target - nums[i]

	 

            if y in h and h[y] != i:

                return [i, h[y]]

# Time Complexity: O(n)

# Space Complexity: O(n)

# Two-pass Hash Table

# The time complexity is O(n) because we traverse the list containing n elements exactly twice. Since the hash table reduces the look-up time to O(1), the overall time complexity is O(n).

# The space complexity is O(n) because in the worst case, we could be storing all n elements in the hash table. Therefore, the space required grows linearly with the size of the input list.