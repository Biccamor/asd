class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next

def insert(head: Node, add) -> Node:

    if head == None: 
        return add 

    if add.val < head.val:
        add.next= head
        return add
    prev = head
    curr = head.next

    while curr:

        if add.val < curr.val:    
            prev.next = add
            add.next = curr
            return head 
        else:
            prev = curr
            curr = curr.next


    prev.next = add
    add.next = None

    return head

def find_max(head: Node) -> int | None:

    if head == None:
        return None
    

    maximum: int = head.val 

    curr: Node = head.next

    while curr!=None:
        maximum = max(curr.val, maximum)
        curr = curr.next

    return maximum


def delete_maximum(head: Node, max_value: int | None) -> Node:

    if not head: return None
    if max_value == None: return head

    if max_value == head.val:
        return head.next
    
    prev = head
    curr = head.next

    while curr:
        
        if curr.val == max_value:
            prev.next = curr.next 
            curr = None 
            return head
        
        prev = curr
        curr = curr.next

    return head    
    
def insertion_sort(head:Node) -> Node:  
    
    sorted_head = None

    if head == None or head.next == None:
        return head

    curr = head
    
    while curr:

        next_node = curr.next
        curr.next = None
        
        sorted_head = insert(sorted_head, curr)
        curr = next_node
    
    return sorted_head


if __name__ == "__main__":
    a = Node(1,None)
    b = Node(23,a)
    c = Node(3, b)
    d = Node(32,c)
    e = Node(17, d)
    f = Node(345, e)

    print(f.val)
    sort_list = insertion_sort(f)
    print(sort_list.val)