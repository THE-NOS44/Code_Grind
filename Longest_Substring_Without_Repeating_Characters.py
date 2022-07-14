#LC - 3

# Approaches - 

#   Brute Force - Nested Loop 
#   Sliding Window - take 2 pointers Left and Right both starting from 0. 
#                  - traverse an element (RIGHT pointer only) and keep track of all the elements by putting them into a map / array or something  & also keep recording the counter
#                  - if an element that is already in the map then its the repeating one , so start shortening the window by removing these characters from the LEFT one by one 
#                  - moving the left pointer , until the character which matched in the map is out of the window... once its out of the window , update the map by removing that character 
#                  - keep track of MAX Length  - Conut of length can be done by = MAX ( Right - Left +1 ) 
#                  - STOP once the right pointer reaches the last element of array

# The above solutions is NOT the most optimal solution to the porblem so we make a few more modifications to optimise it.

# PROBLEM - In the above solution we shrink the window by moving the LEFT pointer towards right one by one and check if the repeating chanracter is out of the window EVERYTIME.
#         - until its out , then we update the map and continue the same

# OPTIMAL Solution - We MODIFY the above approach by keeping track of the current element with its INDEX Vlaue in a map ( Dictionary ) , so what happens is when we find
#                  - a repeat matching from the dictionary , INSTEAD of shrinking the window by moving LEFT pointer ONE by ONE , we have the index value of the matching
#                  - character in the dictionary already , so we use it and Move our LEFT pointer direcly one step ahead of that index value , shrinking the window and 
#                  - getting rid of the repeating character from our dictionary directly ...
#                  - REST REMAINS THE SAME .. Update the dictionary with the characters and index value , update the Max length every time and return .. EZPZ

# you can also use FOR loop instead of while it the same .. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}

        right = 0
        left = 0 

        max_len = 0

        while right < len(s):

            if s[right] in dic :

                left = max( dic[s[right]]+1, left)

            dic[s[right]] = right
            
            max_len = max(max_len , right - left +1)
            right += 1

        return max_len
      
# Time complexity :O(n).
#   n is the length of the input string.
#   It will iterate n times to get the result.

# Space complexity: O(m)
#   m is the number of unique characters of the input.
#   We need a dictionary to store unique characters.
