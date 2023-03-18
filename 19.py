# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
    def __repr__(self):
        return f"heading {head.val}"
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if n==0:
            return head
        n=n+1

        c=self.size(head)
        if c==0:
            return []
        k=c-n+1
        curr=head
        for i in range(c):
            if i==k:
                curr.next=curr.next.next
            curr=curr.next
        return  self.lia(head)
    def size(self, head):
        linker=head        
        c=0
        while linker.next!=None:
            c+=1
            linker=linker.next
        return c
    def size(self, head):
        linker=head        
        c=0
        while linker.next!=None:
            c+=1
            linker=linker.next
        return c
    def lia(self,linked):
        curr=linked
        while True:
            print(curr.val)
            curr=curr.next
            if curr==None:
                break
        return None


    





li=[1,2,3,4,5]
head=ListNode(li[0])
h1=ListNode(li[1])
h2=ListNode(li[2])
h3=ListNode(li[3])
h4=ListNode(li[4])

head.next=h1
h1.next=h2
h2.next=h3
h3.next=h4
c='val'

print(Solution().removeNthFromEnd(head,4))