# LC - 31


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #LOGIC: basically we try to find the first pair of adjacent elements where the first element is smaller than the next
        
        # 1st pointer will be on the first decreasing element , starting traversing from the right to left
        # 2nd pointer will be the first element that is found to be greater than 1st pointer element , when teaversing backwards AGAIN
        #now we take the 2 pointers and swap the values
        
        n = len(nums)
        p1 = 0
        p2 = 0
        
        if n <= 1 :
            return 
        
        for i in range(n-2,-1,-1):
            
            if nums[i] < nums[i+1]:
                p1 = i
                break
        
        
        for k in range(n-1,-1,-1):

            if nums[k] > nums[p1]:
                p2 = k
                break
        
        #the below IF will get triggered when the whole array is in non increasing order (3,2,1)
        #then the answer would simply be the reverse of the array as the next permutation.
        if p2 == p1 :
            return (nums.reverse())
        
        #Swap the pointers if the above IF is not the case
        temp = nums[p2]
        nums[p2] = nums[p1]
        nums[p1] = temp
        

        #lastly , where the 1st pointer was , reverse all the elements that were to the right of that pointer
        left, right = p1+1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
    
    #Time Complexity :
            # 2 iteration from the back 2*O(n) + 1 reversal O(n) , so 3O(n) == O(n)
    #Space Complexity :
            # No extra space = O(1)
            
            
