class Solution(object):
    def isAnagram(self, s, t):
        """
        Approach: Character Frequency Hash Map
        Time Complexity: O(n) - Single pass to count frequencies.
        Space Complexity: O(1) - Dictionary size is capped at 26 characters.
        
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths do not match, they cannot be anagrams.
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # Build frequency maps for both strings simultaneously
        for i in range(len(s)):
             # .get() safely handles new characters by defaulting to 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Directly compare frequency dictionaries
        return countS == countT

