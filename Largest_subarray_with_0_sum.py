
# GFG - Largest subarray with 0 sum 

# IT IS ASKED  FOR SUBARRAY NOT SUBSEQUENCE , SO Nested Loop will be used for the brute for solution 

# The TRICK - 
# Suppose 3 index X,Y,Z are there , such that X < Y < Z ok
# If we take the sum of all the numbers from X to Y ... and X to Z separately  AND if the SUM MATCHES ... WHAT DOES IT MEAN .. (IMAGINE An array for better understanding)
# SO if   X to Y Sum == X to Z Sum   where Y < Z  THEN THAT MEANS the number between Y and Z will sum up to 0 RIGHT .

# So we Keep a hash map / dict that keeps all the records of the current index with its sum upto this index in pair in that dict.

# Now when we traverse we keep the track of this sum (prefix sum) and check if the same sum has been saved anytime before in the dictionary (  X to Y Sum == X to Z Sum )
# if there is any SUM that matches , then it means the number between the current index and the index we saved in dict (for with the sum got matched) , are 0
# SINCE we need the LENGTH of the subarray , we just subtract that index with the one matching sum in the dict. 

# This difference is the length of a subarray that we keep saved in a MAXI Variable , which is updated globally for the maximum length gotten till now 

# NOW , if the sum doesnt match with anythin in the dict , that means its a new sum value which might match with something later so we save it in the dict as Sum index pair

# ***IMPORTANT***  - when we are traversing the array normally the sum can also get to 0 , so we dont need to match it with anything in the dict BECOZ  we ARE SEARCHING
# FOR 0 SUM ONLY... so if we reach 0 sum then it means this is the maximum length of the subarray with 0 sum ... and we update the current global max with current index value + 1.

class Solution:
  
    # n is the length of the input array , arr is the array
    def maxLen(self, n, arr):
        #Code here
        mapp = {} 
        adder = 0
        maxi = 0
        
        for i in range(n):
            adder += arr[i]
            
            #print(adder)
            
            if(adder == 0) :
                maxi = i + 1
                
            else:
                if adder in mapp :
                #print(mapp[adder])
                    maxi = max(maxi,i - mapp[adder])
            
                else:
                    mapp[adder] = i
            #print(mapp)
            #print(maxi)
        return maxi
