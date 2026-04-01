# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        cur=head
        mystack=[]

        
        while cur:
            mystack.append(cur)
            cur=cur.next
        if mystack:
            res=mystack.pop()
        else:
            res=[]
        myres=res
        while mystack:
            cur=mystack.pop()
            res.next=cur
            res=res.next
        res.next=None
        return myres


