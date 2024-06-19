# Define the Node class to represent each node in the circular linked list
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

# Link the nodes together to form a circular linked list
node1.next = node2  # Link first node to second node
node2.next = node3  # Link second node to third node
node3.next = node4  # Link third node to fourth node
node4.next = node1  # Link fourth node back to first node, creating a circular structure

# Initialize currentNode to the head of the circular linked list (node1)
currentNode = node1
# Remember the startNode to detect when we complete the circle
startNode = node1

# Print the data of the first node
print(currentNode.data, end=" -> ")
# Move to the next node
currentNode = currentNode.next

# Traverse the circular linked list until we come back to the start node
while currentNode != startNode:
    # Print the data of the current node followed by " -> "
    print(currentNode.data, end=" -> ")
    # Move to the next node in the list
    currentNode = currentNode.next

# Print "..." to indicate the circular nature of the list
print("...")
