class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def merge(l,r):
    dummy = ListNode()
    new = dummy 

    while l and r:
        if l.val <= r.val:
            new.next = l 
            new = new.next 
            l = l.next
        else:
            new.next = r
            new = new.next
            r = r.next

    if l:
        new.next = l 

    if r:
        new.next =  r

    return dummy.next

def merge_sort(head):
    if not head or not head.next: return head

    slow = head
    fast = head.next 

    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    
    mid = slow 
    right_head = mid.next
    mid.next = None
    left = merge_sort(head)
    right = merge_sort(right_head)
    return merge(left, right)

def main(head):
    head = merge_sort(head)
    return head 

if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

    head = main(head)
    
    while head != None: # type: ignore
        print(head.val)
        head = head.next
