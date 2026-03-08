"""
Obracnie linked listy
"""

class Node:
    def __init__(self, val: int, next=None):
        self.next = next
        self.val = val

def reverse(head: Node) -> Node:

    if head == None or head.next == None:
        return head
    
    prev = None
    curr = head
    
    while curr != None:

        next_node = curr.next # trzymamy wskaznik do nexta
        curr.next = prev # odwracamy strzalke na prev
        
        prev = curr # idziemy prev do przodu
        curr = next_node # idziemy curr do przodu

    return prev


        