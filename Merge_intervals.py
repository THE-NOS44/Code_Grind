# LC - 56

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # create a new array for output         
        merged = []
        
        # sort the intervals
        intervals.sort()
        #print(intervals)
        
        # traverse the interval pairs
        for i in intervals :
            
            
            # if the list of merged intervals is empty 
	          # or if the current interval does not overlap with the previous,
		        # simply append it.
            if not merged or merged[-1][1] < i[0] :
                merged.append(i)
            
            # otherwise, there is overlap,
			      # so we merge the current and previous by taking the higher of the both the right side elements 
            # of both pairs
            else :
                 merged[-1][1] = max(merged[-1][1],i[1])
        
        return merged
    
    
#Time complexity:
        # In python, use sort method to a list costs O(nlogn), where n is the length of the list.
        # The for-loop used to merge intervals, costs O(n).
        # O(nlogn)+O(n) = O(nlogn)
        # So the total time complexity is O(nlogn).

#Space complexity:
        # The algorithm used a merged list and a variable i.
        # In the worst case, the merged list is equal to the length of the input intervals list. So the space           
        # complexity is O(n), where n is the length of the input list.
        
        
        
        
        
