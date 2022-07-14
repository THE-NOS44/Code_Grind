#LC - 876

# APPROACH - Turtle Hare

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        slow = head 
        fast = head
        
        while fast and fast.next :
            
            fast = fast.next.next
            slow = slow.next
            
        return slow 
            
