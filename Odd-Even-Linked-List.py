# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def list_to_listnode(self, lst):
        if not lst:
            return None
        
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head
    
    def oddEvenList(self, head):
        index = 0
        w = []
        parz = []
        
        current = head
        while current:
            if index % 2 != 0:
                parz.append(current.val)
            else:
                w.append(current.val)
            index += 1
            current = current.next
        
        for i in parz:
            w.append(i)
            
        return self.list_to_listnode(w)
        