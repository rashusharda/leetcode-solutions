class Solution(object):
    def twoSum(self, nums, target):
        """
        Approach: Single-pass hash map (dictionary)
        Time complexity: O(n) - In the worst case, we iterate through the whole list. Dictionary lookups take O(1) time.
        Space complexity: O(n) - In the worst case, we store all elements in the dictionary.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Tracks numbers we have already evaluated: {number: index}
        seen = {}
      
        for i, n in enumerate(nums):
            # Calculate the required complement to reach the target sum
            diff = target - n

            # If the complement exists in our map, we found the pair
            if diff in seen:
                return [seen[diff], i]

            # Otherwise, store the current number and its index for future lookups
            seen[n] = i
