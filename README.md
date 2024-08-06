# Length of Longest Substring Without Repeating Characters
  This Python project contains a class Solution that provides a method to find the length of the longest substring without repeating characters in a given string.

# Class solution
# Method: lengthOfLongestSubstring(self, s: str) -> int
    The lengthOfLongestSubstring method calculates the length of the longest substring in the input string s that does not contain any repeating characters.
# Parameters
    s (str): The input string in which to find the longest substring   without repeating characters.

# Returns
    int: The length of the longest substring without repeating characters.

# How it works:
  * Initialization:
    A set charSet is used to track the unique characters in the current substring.
    Two pointers l (left) and r (right) are used to define the sliding window in the string.
    A variable res is used to keep track of the maximum length of the substring found.
  * Sliding Window:
    The right pointer r moves through each character in the string.
    If a duplicate character is found, the left pointer l is moved to shrink the window until the duplicate character is removed.
    The maximum length of the current window (r - l + 1) is calculated and stored in res.
  * Result:
    The method returns the maximum length of the substring without repeating characters.
    
# How to run:
  * To run locally use git clone and redirect to the folder and run the python file directly 
   ```bash
    python longestSubstring.py
  ```

  * To run in docker
   1. Please install docker desktop 
  ```
    https://www.docker.com/products/docker-desktop/
  ```

   2. checkout the Dockerfile provided in the projectdirectory for reference
   ```
    Dockerfile
   ```

   3. Build an image using the follwing command
   ```
    docker build -t python-docker-vscode . 
   ```

   4. Run the container using
   ```
    docker run python-docker-vscode
   ```
   
   5. Running on a pipeline: Please refer to
   ```
    docker-python.yml
   ```

# References
  * https://www.geeksforgeeks.org/window-sliding-technique/
  * https://realpython.com/python-sets/
  * https://docs.github.com/en/actions

# Contributions
    Feel free to contribute to the repository if interested, other approaches/languages appreciated.
    https://github.com/abirami91/Leetcode-challenges/tree/main.
