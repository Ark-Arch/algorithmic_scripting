# given head and index, return the value of the node on index 2

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def get_node_value(head, index):
    count = 0
    current = head
    while(current != None):
        if count == index:
            return current.val
        count+=1
        current = current.next
    return 'Error: index limit reached'

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

print(get_node_value(head, 5))