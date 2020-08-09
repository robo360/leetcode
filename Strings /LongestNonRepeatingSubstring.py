"""
Level: Medium 

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 1):
            return 1
    
        last_seen_position = dict()
        long_sub = ""
        current_sub = ""
        i = 0 
        j = 0 
        while j < len(s):
            current_alphabet = s[j]
            if(current_alphabet in last_seen_position):
                if(last_seen_position[current_alphabet] < i):
                    last_seen_position[current_alphabet] = j
                else:
                    i = last_seen_position[current_alphabet] + 1 
                    last_seen_position[current_alphabet] = j
            else:
                last_seen_position[current_alphabet] = j
                
            j += 1
            current_sub = s[i:j]
            if(len(current_sub) >= len(long_sub)):
                        long_sub = current_sub[:]
        
        return len(long_sub)