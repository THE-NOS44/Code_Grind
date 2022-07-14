# LC - 206


# Linked List - can be dont in 2 ways - Iterative (done below) and Recursive (also done just for reference)

# Intution - take 3 pointers  - One Prev as NULL - One Curr which points HEAD - One Nxt which is NULL at the beginning but in loop it saves the previous of head

# Now, Firstly Nxt = Current's next (heads's next) , then current's next is updated to previous the Logical objective of the question is done , now we repeat same 
# after updating the prev, curr, nxt pointers
# So Previous is now Current and Current is now Next.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev = None 
        curr = head
        nxt = None
        
        while curr != None :
            
            nxt = curr.next
            curr.next = prev
            
            prev = curr
            curr = nxt
        
        head = prev
        
        return head
      
#TC - O(n)
#SC - O(1)



# Recursive Solution :

def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
