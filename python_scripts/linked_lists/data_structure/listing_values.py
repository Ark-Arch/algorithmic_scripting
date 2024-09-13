
# Linked list values problem
# return an array containing all of the values within the nodes of that linked list,
# we should also do it in order

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



def linked_list_values(head):
    array = []
    current = head
    while(current != None):
        array.append(current.val)
        current = current.next        
    return array

def recursively_linked_list_values(head, array):
    # base case
    if head == None:
        return
    
    else:
        array.append(head.val)
        recursively_linked_list_values(head.next,array)

    return array

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
array = []
print(recursively_linked_list_values(head,array))