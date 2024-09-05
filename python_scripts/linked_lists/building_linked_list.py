# Basic Structure
# two classes: 
#   Node - to represent a single node of the linked list
#   LinkedList - to manage the linked list and provide methods to insert, delete, and traverse the list.

# STEP 1: TO CREATE THE NODE CLASS
class Node:
    def __init__(self, data):
        self.data = data    # Data the node stores
        self.next = None    # Pointer to the next node (initially None)

# STEP 2: TO CREATE THE LINKEDLIST CLASS
class LinkedList:
    def __init__(self):
        self.head = None # Initially, the list is empty, so head points to none - nothing.

    # Method to insert a node at the beginning (prepend)
    def insert_at_head(self, data):
        new_node = Node(data) # Create a new node
        new_node.next = self.head # New node's next is the current head
        self.head = new_node # Update head to the new node
    
    # Method to insert a node at the end (append)
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None: # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next: # Traverse the list to find the last node
            last = last.next
        last.next = new_node # Make the last node's next point to the new node

    # Method to delete the first occurrence of a node with a specific value
    

