class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

# Time Complexity: O(n)

# Space Complexity: O(n)

# The time complexity is O(n) because we traverse the list containing n elements once. Each look-up and insertion operation in the set takes O(1) time on average, so the overall time complexity is O(n).

# The space complexity is O(n) because in the worst case, we could be storing all n elements in the set. Therefore, the space required grows linearly with the size of the input list.