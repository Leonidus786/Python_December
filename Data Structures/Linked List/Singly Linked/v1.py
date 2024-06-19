# Define the Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        # Initialize the node with data and set the next pointer to None
        self.data = data
        self.next = None

# Create individual nodes with given data
node1 = Node(3)   # First node with data 3
node2 = Node(5)   # Second node with data 5
node3 = Node(13)  # Third node with data 13
node4 = Node(2)   # Fourth node with data 2

# Link the nodes together to form the linked list
node1.next = node2  # Link first node to second node
node2.next = node3  # Link second node to third node
node3.next = node4  # Link third node to fourth node

# Initialize currentNode to the head of the linked list (node1)
currentNode = node1

# Traverse the linked list and print each node's data
while currentNode:
    # Print the data of the current node followed by " -> "
    print(currentNode.data, end=" -> ")
    # Move to the next node in the list
    currentNode = currentNode.next

# Print "null" to indicate the end of the linked list
print("null")
