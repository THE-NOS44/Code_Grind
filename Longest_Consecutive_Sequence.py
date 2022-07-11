# LC - 128 

#**SORTING - O(n Log n)**

	if not nums:
            return 0
        
        count = 1 
        max_counter = 1
        
        nums.sort()
        
        for i in range(1,len(nums)):
            
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    count += 1
                else:
                    max_counter = max(count,max_counter)
                    count = 1

        return max(max_counter,count)
      
      
      
# BRUTE FORCE with OPTIMIZATION 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
    
        # - Intution : We take a number and see if it follows a sequence , i.e. , if the number has continuous             
        #  numbers ahead , so we count them and store them in the current max counter. 
        #  if the sequence is broken , we reset the current counter to 1 and update the global counter 
        
        # -IMPORTANT PART - in the optimization part ,we have to check if the current number is a part of a               
        #  previous sequence or not FOR THAT we easily check if there is a previous number that exists for the             
        #  number in the array , if there is , then it is a part of some sequence , if not then it can be                 
        #  considered as a new sequence.
        
        mx_streak = 0
        num_set = set(nums) #Optimization part

        for i in num_set :
            if i-1 not in num_set: #Optimization part
                curr_num = i
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1

                mx_streak = max(mx_streak , curr_streak)

        return mx_streak
    
    
        # - TIME Complexity - In brute force it was O(n^3)
        #  but with optimization it goes down to O(n) coz we use set to check if the number is already a part of seq. 
        #  in only O(1) time
