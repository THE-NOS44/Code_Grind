# LC - 74
# Video Link -  - https://www.youtube.com/watch?v=ZYpYur0znng&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=15&ab_channel=takeUforward

# 2 Approaches - BINARY Search Ususally - done below
#              - 1 more BETTER approach - Done after Binary Search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # BINARY SEARCH
        
        n = len(matrix)
        m = len(matrix [0])
        
        # we are taking the LOW and HIGH as if the whole matrix was a single continuous array.
        low = 0
        high = (m*n) - 1
        
        
        while low <= high :
            
            # below we find the MID with overflow prevention
            mid = low +(high -low) //2 
            
   #--->    # NOW this expression below actually takes mid value which is the MID if we took the matrix as an               
            # array , and converts it into an index value of the matrix in [i][j] form . 
            # Rest is simple BINARY SEARCH
      
            if ( matrix[mid//m][mid%m] == target ):
                return True
            elif (matrix[mid//m][mid%m] < target) :
                low = mid + 1
            else:
                high = mid -1        
        return False

    
    
    
    
    
#          - In this approach we take a the last element of the first row as Start point , now if the target is smaller than the CURRENT , we move to the RIGHT 
#          - and if the target is greater than the CURRENT , we move one step DOWN . 
#          - We keep doing this until we find our target or we go out of bounds

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 0 :
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        i = 0
        j = m-1
        
        #print (matrix[i][j])
        
        while (i < n and j >= 0) :
            
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] < target:
                i += 1
            
            else:
                j -= 1
        return False
    
    # Time Complexity - O(m+n)
    # Space Complexity = O(1)
