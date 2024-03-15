class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_diameter(self, tree: BinaryTree = None) -> int:
    self.max_diameter = 0
    def depth(node):
        if not node:
            return 0
        #Recursive call for left and right child
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1
    depth(root)
    return self.max_diameter

