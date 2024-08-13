class solution:
    def lengthOfLongestSubstring(self, s):
        """
        The method calculates the longest substring without repeating characters.

        Args: s {str}

        Returns: Max_length: maximum length of teh unique substring {int}
        """
        # variable to store the max length of the substring.
        max_length = 0

        #iterate through all the characters of the string
        for i in range(len(s)):
            # inner loop to create all possible substrings
            # starting from the current character (i) to the end of the substrings.
            for j in range(i, len(s)):
                # extract the substring from the current charcater i
                # To the current inner loop index(j) and
                # Store it in a substring varaible
                substring = s[i:j+1]

                #check if extracted substring has unique character
                if self.has_unique_characters(substring):
                    # if the substring has unique characters
                    # Update the max_length with maximum length found so far.
                    max_length = max(max_length, len(substring))
        return max_length


    def has_unique_characters(self, sub_string):
        """
        The method evaluates unique characters in a substring.

        Args: sub_string{str}

        Returns: Boolen {False} if repetative characters found else {True}
        """
        # Initialize an empty dictionary to keep 
        # track of current character sin the substring
        char_count = {}

        # Loop through each character in the string
        for char in sub_string:
            # Update the count of current character in the cahracter dictionary.
            char_count[char] = char_count.get(char, 0) + 1

            # if the character count is greater than 1
            # Then there is a repetative character.
            if char_count[char] > 1:
                return False
            
        return True
    
Solution = solution()
print(Solution.lengthOfLongestSubstring("abcbabc"))
print(Solution.lengthOfLongestSubstring("aaaa"))