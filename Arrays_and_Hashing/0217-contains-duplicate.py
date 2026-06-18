class Solution(object):
    def containsDuplicate(self, nums):
        """
        Approach: Hash Set Length Comparison
        Time Complexity: O(n) - Converting the list to a set takes linear time.
        Space Complexity: O(n) - The set stores unique elements, taking up to linear space.
        
        :type nums: List[int]
        :rtype: bool
        """
        # A set removes duplicates. If the lengths differ, duplicates existed.
        return len(nums) != len(set(nums))
