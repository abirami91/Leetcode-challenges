class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize the set to keep track of unique characters
        charSet = set()
        # Initialize the left pointer
        l = 0
        # Initialize the result variable to store the maximum length
        res = 0

        # Iterate through the string using the right pointer `r`
        for r in range(len(s)):
            # If the character at `r` is already in the set, it means there is a duplicate
            while s[r] in charSet:
                # Remove the character at `l` from the set and move the left pointer `l`
                charSet.remove(s[l])
                l += 1
            # Add the character at `r` to the set
            charSet.add(s[r])
            # Update the result with the maximum length of the current window
            res = max(res, r - l + 1)
            
        # Return the length of the longest substring without repeating characters
        print("result: length of substring", s)
        return res
    
    # Example usage and tests.
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(solution.lengthOfLongestSubstring("")) 
