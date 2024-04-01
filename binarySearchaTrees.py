class BinaryTreeNode:
    # Initialization of the binary tree node.
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def preorder(root):
    # Return an empty list if the tree is empty.
    if root is None:
        return []
    
    # Initialize a stack with the root node and an empty list for the output.
    stack, output = [root], []
    
    # Iterate until the stack is empty.
    while stack:
        # Pop the top item from the stack.
        node = stack.pop()
        # Append the node's value to the output list.
        output.append(node.val)
        # Push right child first so the left child is processed first.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return output

def reconstructBT(preorder, inorder):
    # Base case: if either list is empty, we're done.
    if not preorder or not inorder:
        return None
    
    # The root is always the first item in the preorder sequence.
    root_value = preorder[0]
    root = BinaryTreeNode(root_value)
    
    # Find the root in the inorder list to split the tree.
    split_index = inorder.index(root_value)
    
    # Recursively construct the left subtree from the left split.
    root.left = reconstructBT(preorder[1:1+split_index], inorder[:split_index])
    
    # Recursively construct the right subtree from the right split.
    root.right = reconstructBT(preorder[1+split_index:], inorder[split_index+1:])
    
    return root

def convertBSTtoGST(root):
    # This variable keeps track of the running sum of all nodes processed so far.
    sum_so_far = [0]  # Using a list to keep it mutable in the recursion.

    def reverse_inorder(node):
        # Base case: if the node is None, do nothing.
        if not node:
            return
        # Process the right subtree first.
        reverse_inorder(node.right)
        # Update the node's value with the sum of values greater than or equal to it.
        sum_so_far[0] += node.val
        node.val = sum_so_far[0]
        # Process the left subtree.
        reverse_inorder(node.left)
    
    # Start the modified in-order traversal from the root.
    reverse_inorder(root)
    return root