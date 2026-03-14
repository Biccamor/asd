class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def merge(list1, list2):
    
    ans_list = Node(None)
    ans_head = ans_list

    while list1.next!=None and list2.next!=None:
        
        if list1.val < list2.val:
            ans_head.next = list1
            list1 = list1.next
        else:
            ans_head.next = list2
            list2 = list2.next
        
        ans_head = ans_head.next

    if list1.next!=None:
    
        ans_head.next = list1
        list1 = list1.next
        #ans_head = ans_head.next

    
    if list2.next!=None:
    
        ans_head.next = list2
        list2 = list2.next
        #ans_head = ans_head.next

    return ans_list.next

if __name__ == "__main__":
    p1 = Node(5)
    p2 = Node(7)
    p3 = Node(1)
    p4 = Node(10)
    p1.next = p2
    p2.next = p3
    p3.next = p4

    q1 = Node(4)
    q2 = Node(10)
    q3 = Node(11)
    q4 = Node(3)
    q1.next = q2
    q2.next = q3
    q3.next = q4

    merge(p1,q1)

    