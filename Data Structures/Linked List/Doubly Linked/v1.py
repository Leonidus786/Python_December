# Define the Node class to represent each node in the doubly linked list
class Node:
    def __init__(self, data):
        # Initialize the node with data and set the next and prev pointers to None
        self.data = data
        self.next = None
        self.prev = None

# Create individual nodes with given data
node1 = Node(3)   # First node with data 3
node2 = Node(5)   # Second node with data 5
node3 = Node(13)  # Third node with data 13
node4 = Node(2)   # Fourth node with data 2

# Link the nodes together to form the doubly linked list
node1.next = node2  # Link first node to second node

node2.prev = node1  # Link second node back to first node
node2.next = node3  # Link second node to third node

node3.prev = node2  # Link third node back to second node
node3.next = node4  # Link third node to fourth node

node4.prev = node3  # Link fourth node back to third node

# Traversing the doubly linked list forward
print("\nTraversing forward:")
currentNode = node1
while currentNode:
    # Print the data of the current node followed by " -> "
    print(currentNode.data, end=" -> ")
    # Move to the next node in the list
    currentNode = currentNode.next
# Print "null" to indicate the end of the list
print("null")

# Traversing the doubly linked list backward
print("\nTraversing backward:")
currentNode = node4
while currentNode:
    # Print the data of the current node followed by " -> "
    print(currentNode.data, end=" -> ")
    # Move to the previous node in the list
    currentNode = currentNode.prev
# Print "null" to indicate the start of the list
print("null")
