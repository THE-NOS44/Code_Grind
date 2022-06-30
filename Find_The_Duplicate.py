class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # - Can be solved by a lot of methods 
        # - PATTERN : Linked List Cycle, Binary Search
        
        # - Below we have used the - mark the index traversed with -1 multiple ... 
        # and if we get to some number already negative then the index which led us to 
        # this number is the repeating one
        
        for i in range(len(nums)) : 
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] *= -1
        
        # - COMPLEXITY : 
             # Time - O(n)
             # Space - O(1)
