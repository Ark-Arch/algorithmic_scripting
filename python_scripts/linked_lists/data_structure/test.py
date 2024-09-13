class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

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


def print_linked_list(head):
    current = head
    while(current != None):
        print(current.val)
        current = current.next

# writing this recursively
def recursively_print_linkedlist(current):
    # base case
    if current.next == None:
        return f'{current.val} -> None'
    else:
        return f'{current.val} -> ' + recursively_print_linkedlist(current.next)

head = node_a
print(recursively_print_linkedlist(head))