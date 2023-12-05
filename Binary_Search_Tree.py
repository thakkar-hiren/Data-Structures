class BST:
    """
    Binary Search Tree (BST) implementation in Python.

    This class represents a node in a binary search tree. Each node contains a data value, a reference to its
    left child (with a value less than the current node), and a reference to its right child (with a value greater
    than the current node).

    Methods:
    - __init__(self, data): Initializes a new BST node with the given data.
    - add_node(self, data): Adds a new node with the specified data to the BST.
    - inorder(self): Performs an inorder traversal of the BST, returning a list of elements in ascending order.

    Example usage:
    ```python
    numbers = [87, 67, 54, 68, 91, 100, 2, 1]
    tree = buildTree(numbers)
    print(tree.inorder())  # Output: [1, 2, 54, 67, 68, 87, 91, 100]
    ```

    Note: The `buildTree` function is used to construct a BST from a list of elements.

    Author: [Hiren Thakkar]
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        # Check if the data that we are going to insert is already available or not.
        if data == self.data:
            return
        # Check if the value of data is greater or less than the current data value
        # If value is less than current value then add it into left child else right child.
        if data < self.data:
            # Check if there exist any left child or not. If not then create one.
            if self.left:
                # Creating new node to the left child
                self.left.add_node(data)
            else:
                # Creating new left child
                self.left = BST(data)
        else:
            # Check if there exist any right child or not. If not then create one.
            if self.right:
                # Creating a new node to the right child
                self.right.add_node(data)
            else:
                # Creating new right child
                self.right = BST(data)

    def inorder(self):
        elements = []
        # Inorder follows Left -- Root -- Right pattern
        # Let's visit Left part first
        if self.left:
            elements += self.left.inorder()
        
        elements.append(self.data)

        # Now, visit Right part
        if self.right:
            elements += self.right.inorder()

        return elements 

def buildTree(elements):
    """
    Constructs a BST from a list of elements.

    Parameters:
    - elements (list): List of elements to be inserted into the BST.

    Returns:
    - BST: The root node of the constructed BST.
    """
    root_node = BST(elements[0])
    for i in range(1,len(elements)):
        root_node.add_node(elements[i])
    return root_node

if __name__ == "__main__":
    numbers = [87,67,54,68,91,100,2,1]
    tree = buildTree(numbers)
    print(tree.inorder())