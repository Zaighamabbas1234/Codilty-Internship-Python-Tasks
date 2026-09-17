# Problem Statement:
# Solve a Real-world Algorithm Problem.

# Description:
# Write a function "longest_substring(s)" that finds the length of the longest substring without repeating characters in a given string "s".

# Solution:
# A common and efficient solution is the Sliding Window algorithm. It keeps track of the current substring without duplicate characters and expands or shrinks the window as needed.

# Sliding Window algorithm:
# The Sliding Window Algorithm is an efficient technique used to solve problems involving arrays and strings. It works by maintaining a window (a continuous portion of the data) that moves across the input. Instead of repeatedly checking every possible subarray or substring, the algorithm expands or shrinks the window as needed, reducing unnecessary computations and improving performance.

# Longest_Substring_Sliding_Window Code:

#Defines a function named longest_substring() that takes one parameter, s, representing the input string.
def longest_substring(s):
    char_index = {} # Stores the last index of each character. Creates an empty dictionary.
    left = 0 # Left boundary of the sliding window. Initially, the window starts at index 0.
    max_length = 0 # Stores the length of the longest substring found so far. Initially it is 0.

# Loop through the string:

    for right in range(len(s)): # Right moves from the beginning to the end of the string. It represents the ending index of the current window.
        if s[right] in char_index and char_index[s[right]] >= left: # Checks whether the current character has appeared before. Checks whether the previous occurrence is inside the current window.
            left = char_index[s[right]] + 1 # If a duplicate is found, move left one position after the previous occurrence.
            
        # Update the last seen index of the character:
        char_index[s[right]] = right
        # Update the maximum length:
        max_length = max(max_length, right - left + 1)
    return max_length # Returns the length of the longest substring without repeating characters.

# Example usage:

# Test Case 1: All characters are unique:
print("Length of the longest substring is:", longest_substring("abcdefghijklmnopqrstuvwxyz"))

# Test Case 2: All characters are the same:
print("Length of the longest substring is:", longest_substring("bbbb"))

# Test Case 3: String contains repeating characters:
print("Length of the longest substring is:", longest_substring("aabbbccccdddddeeeeee"))

# Test Case 4: Empty string:
print("Length of the longest substring is:", longest_substring(""))

# Complexities:
# Time Complexity: O(n) (each character is processed at most twice).
# Space Complexity: O(min(n,m)), where m is the number of unique characters.

# Submitted By: Zaigham Abbas.
# Submitted to: HR Codility.
# Dated: 08/06/2026.