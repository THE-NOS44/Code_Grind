  # LC - 169
  
  # MANY APROACHES - you know you can do Hash maps , traversals with nested loop as brute force etc .
  # OPTIMAL SOLUTION - Moore Voting Algorithm 
  
  # Really cool and simple algo - we take a count = 0 and a Majority element . Now we start with the first element and make it as the Majority element
  # now as we move forward IF the current element is equal to the Majority element then counter ++ , if not equal to the Majority element , then counter -- 
  # AND IF the counter was 0 till now , then make this current element as the Majority element. 
  
  # MY Intution here was - there is a SEAT for MAJOR ELEMENT right now , if the seat is empty ( count = 0 ) then simply give it to the element with we treverse 
  # now if the further element is same as the Element on the SEAT right now , then the power of the seat increases... if they are different we reduce the power 
  # of the seat ... 
  # IF the power gets to zero the same thing repeats , the next element gets the seat and we increase / decrease the counter as explained above ... SINCE WE KNOW 
  # that a majority candidate EXISTs , which is more than half of all the elements in the array , it will survive in the SEAT of MAJOR ELEMENT. 
  # So whoever survives , will be out MAJORITY ELEMENT
   
  class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        curr_major = 0
        count = 0
        
        for i in nums :
            
            if count == 0 :
                curr_major = i
            if curr_major == i:
                count += 1
            else:
                count -= 1
        
        return curr_major
      
     # Time complexity - O(n)
     # Space complexit - O(1)
