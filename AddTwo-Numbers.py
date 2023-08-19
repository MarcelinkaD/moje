# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        obecny = dummy
        przeniesienie = 0
        
        while l1 or l2 or przeniesienie:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            suma = val1 + val2 + przeniesienie
            
            przeniesienie = suma // 10
            cyfra = suma % 10
            
            obecny.next = ListNode(cyfra)
            obecny = obecny.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
        
        
        
        
        
        
        
