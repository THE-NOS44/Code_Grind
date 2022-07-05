# LC -229

# READ QUESTION - it is not gurantteed that a majority element exist.
# APROACH - BOYCE MOORE VOTING ALGO - WITH 2  MAJORRITY SEATS


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if not nums :
             return []
        # THE INITIAL Values can be anyting BUT DIFFERENT VALUES .. else it will trigger the edge cases
        # So take any 2 initial values
        
        major1 = 0
        major2 = 1
        
        count1 = 0 
        count2 = 0
        
        for i in nums :
            
            if i == major1:
                count1 += 1
            elif i == major2:
                count2 += 1 
                
            elif count1 == 0 :
                major1 = i
                count1 += 1
                
            elif count2 == 0 :
                major2 = i
                count2 += 1
                
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (major1, major2)
                if nums.count(n) > len(nums) // 3]
      
 
