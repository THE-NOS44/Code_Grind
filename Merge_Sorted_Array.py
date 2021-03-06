        '''Video Link - https://www.youtube.com/watch?v=C4oBXLr3zos'''

        
        # - 2 Pointer Approach ( REMEMBER --> ALREADY SORTED ARRAYS)
  
        # - Question says that nums1 array is actually having 0s at the end , which is equal to the length of nums2
        # - So we run 2 pointers BACKWARDS (from m-1 & n-1) and compare the numbers , the larger number adds to           
        # the end of the 0 space in nums1 array 
        # - If all the numbers in nums2 array array are done , we STOP
        
        pointer1 = m-1
        pointer2 = n-1
        
        ult_pointer = m+n-1
        
        # -we have run this while loop till pointer2 >=0 (teaversing nums2 backwards), becoz we will run it until         
        # all the elements of nums2 endup in nums1.
        while pointer2 >= 0:  
            
            if pointer1 >= 0 and (nums1[pointer1] > nums2[pointer2]) :
                nums1[ult_pointer] = nums1[pointer1]
                ult_pointer -= 1
                pointer1 -= 1
            
            else:
                nums1[ult_pointer] = nums2[pointer2]
                ult_pointer -= 1
                pointer2 -= 1
        
        return nums1
                
        
        #SIDE CASES :
            
            # - if nums1 is = [] (empty) then the pointer1 initialized would be -1. so we check in the if                   
            # statement ,that pointer 1 is  >= 0 .
        
        #COMPLEXITY :
            
         
        
    
