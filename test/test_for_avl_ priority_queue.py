import unittest
import os
from src.avl_priority_queue import PriorityQueue, Node

class TestAVLPriorityTree(unittest.TestCase):
    def test_delete_max_priority_function(self):
        tree = PriorityQueue()
        tree.insert(4, 5)
        tree.insert(1, 3)
        tree.insert(6, 1)
        tree.insert(13, 2)
        tree.insert(100, 7)
        tree.insert(17, 9)
        deleted_node = tree.delete_highest_priority_element()
        self.assertEqual((deleted_node.value, deleted_node.priority), (17, 9))

    def test_equal_priority_input_data(self):
        tree = PriorityQueue()
        tree.insert(1, 1)
        tree.insert(2, 1)
        tree.insert(3, 1)
        tree.insert(4, 1)
        tree.insert(5, 1)
        self.assertEqual(tree.root.left.value, 2)

    def test_increasing_priority_input_data(self):
        tree = PriorityQueue()
        tree.insert(1, 1)
        tree.insert(11, 2)
        tree.insert(111, 3)
        tree.insert(1111, 4)
        tree.insert(11111, 5)
        self.assertEqual(tree.root.left.value, 1111)


if __name__ == '__main__':
    unittest.main()
