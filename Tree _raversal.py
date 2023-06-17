#  Here's an example of a Python program that demonstrates three common tree traversal algorithms: Preorder, Inorder, and Postorder.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is None:
        return

    print(node.value, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node is None:
        return

    inorder_traversal(node.left)
    print(node.value, end=" ")
    inorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end=" ")

# Example usage
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform tree traversals
print("Preorder Traversal: ", end="")
preorder_traversal(root)  # Output: 1 2 4 5 3

print("\nInorder Traversal: ", end="")
inorder_traversal(root)  # Output: 4 2 5 1 3

print("\nPostorder Traversal: ", end="")
postorder_traversal(root)  # Output: 4 5 2 3 1
