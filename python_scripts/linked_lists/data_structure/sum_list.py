# a singly linked list containing numbers as nodes.
# return the total sum of the nodes in the linked list

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def sum_list(head):
    total_sum = 0
    current = head

    while(current != None):
        total_sum += current.val
        current = current.next
    
    return total_sum

def recursive_sum_list(head, total_sum=0):
    # base case
    if head == None:
        return 0
    else:
        total_sum = head.val + recursive_sum_list(head.next)

    return total_sum


node_a = Node(2)
node_b = Node(8)
node_c = Node(3)
node_d = Node(7)

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

head = node_a

print(recursive_sum_list(head))