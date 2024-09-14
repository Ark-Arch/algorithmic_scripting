# write a linked_list_find function that takes the head of a linked list, and a target value.
# The function should return a boolean indicating whether or not the linked list contains the target.


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def linked_list_find(head, target):
    current = head
    while (current != None):
        if current.val == target:
            return True
        current = current.next
    return False

def recursive_linked_list_find(head, target):
    # base case
    if head.val == target:
        return True
    elif head.next == None:
        return False
    else:
        return recursive_linked_list_find(head.next, target)


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

print(recursive_linked_list_find(head, 'D'))
#print(linked_list_find(head, 'C'))