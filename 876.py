# Definition for singly-linked list.
#Done
class ListNode:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next
    def __repr-_(self):
        return f"head={head.val} next={head.next.val} next={head.next.next.val}..."
class Solution:
    def middleNode(self, head):
        return self.size(head,101,False)

        

    def size(self,li,fornode,valu):
        
        c=0
        curr=li
        while_b=False
        while c<fornode and while_b==False:
            if valu==True:
                print(f"val True c={c}")

            if curr.next==None:
                print(f"c={c}")
                while_b=True
            
            c+=1
            curr=curr.next
        if valu==True:
            return curr.val
        
        print(f"c+1/2 {(c)//2}")
        return self.size(li,(c)//2,True)
li=[1,2,3,4,5,6,7]
head=ListNode(li[0])
h1=ListNode(li[1])
h2=ListNode(li[2])
h3=ListNode(li[3])
h4=ListNode(li[4])
h5=ListNode(li[5])
h6=ListNode(li[6])
head.next=h1
h1.next=h2
h2.next=h3
h3.next=h4
# h4.next=h5
# h5.next=h6

curr=head
while curr!=None:
    print(f"linked {curr.val}")
    curr=curr.next
print(Solution().middleNode(head))
    

