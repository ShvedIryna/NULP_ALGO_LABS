from lab3 import BinaryTree, binary_tree_diameter
import unittest

class TestBinaryTreeDiameter(unittest.TestCase):
    def test_binary_tree_diameter(self):
        root1 = BinaryTree(1)
        root1.left = BinaryTree(2)
        root1.right = BinaryTree(3)
        root1.left.left = BinaryTree(4)
        root1.left.right = BinaryTree(5)
        self.assertEqual(root.binary_tree_diameter(root1), 3)

        root2 = BinaryTree(1)
        root2.left = BinaryTree(2)
        root2.right = BinaryTree(3)
        root2.right.left = BinaryTree(4)
        root2.right.right = BinaryTree(5)
        self.assertEqual(binary_tree_diameter(root2), 3)

        root3 = BinaryTree(3)
        root3.left = BinaryTree(9)
        root3.right = BinaryTree(20)
        self.assertEqual(binary_tree_diameter(root3), 3)


if __name__ == '__main__':
    unittest.main()
