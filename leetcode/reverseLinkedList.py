class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        sys.setrecursionlimit(1000000) 
        curr=copy.deepcopy(head)
        prev=None
        while curr!=None:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        while prev!=None and head!=None:
            if prev.val!=head.val: return False
            prev=prev.next
            head=head.next
        return True
