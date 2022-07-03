#LC - 75


# TRICK TO FOLLOW :   - when Mid pointer is on 1 do nothing , just move MID and LOW pointer one step ahead.
#                     - when MID pointer is on 0 Swap the values of MID and LOW pointer and move BOTH one step ahead.
#                     - whn MID pointer in on 2 Swap the values of MID and HIGH pointer and move OBLY the HIGH pointer towards left by one step.




class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        
        # DUTCH PARTITIONING PROBLEM (Wikipedia)

        
        # Take 3 pointers , The Low Pointer , Mid Pointer , High Pointer .
        #
        # WHAT WE HAVE TO ACHIEVE  : 0s will stay on the left of the Low Pointer
        #                            2s will stay on the right of the High Pointer
        # USE SWITCH CASE FOR THIS PROBLEM
        # WORKING : Low pointer , Mid pointer start from 0 index towards right and High Pointer starts from the
        #           last index moving towards the left.
        #
        #       1* Starting from 0 index check if the current element is 0 , if yes swap values Low pointer and           
        #          Mid Pointer  ( both pointer remains the same place if the the value of 0th index is 0, and is           
        #          swapped ) , then increment both by 1 . 
        #          
        #       2* If the current element under Mid pointer is 1 , then do nothing and move just Mid pointer by           
        #          1 step.
        #
        #       3* If the current element is 2 then swap the values of Mid Pointer and High Pointer , then ONLY           
        #          move the High Pointer to the right by 1 step. ( dont move the mid pointer for this )
        
        # DO THIS UNTIL mid pointer crosses (not even equal to, CROSSES ) the high pointer
        
        
        low = 0
        high = len(nums)-1
        mid = 0
        
        
        while mid <= high :
                    
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp 
                mid += 1
                low += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            elif nums[mid] == 2:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high -= 1
                
                
                
       # Time Complexity - O(N)
      # Space Complexity - O(N)
