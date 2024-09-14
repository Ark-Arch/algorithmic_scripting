# given the head of a linked list, write a function that reverses te order or the nodes in the linked list in-place and return the new list of reverse linked list

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    stack = []
    current = head
    while(current != None):
        stack.append(current.val)
        current = current.next
    
    current = head
    while(current != None):
        current.val = stack.pop()
        current = current.next
    
    return head

def reverse_list_in_place(head):
    # 1 - 2 - 3 - 4 - 5 - 6

    pointer = None
    next_pointer = head

    while(next_pointer != None):
        temp = next_pointer.next
        next_pointer.next = pointer
        pointer = next_pointer
        next_pointer = temp
    return pointer

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')

# A -> B -> C -> D -> E -> NULL
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e

head = node_a

#new_head = reverse_list(head)
new_head = reverse_list_in_place(head)

current = new_head
while(current != None):
    print(current.val)
    current = current.next