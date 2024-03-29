import unittest
from lab1 import quick_sort, find_k_largest, find_k_position


class TestMyFunctions(unittest.TestCase):

    def test_swap(self):
        num = [15, 7, 22, 9, 36, 2, 42, 18]
        sorted_num = quick_sort(num)
        self.assertEqual(sorted_num, [2, 7, 9, 15, 18, 22, 36, 42])

    def test_find_k_largest(self):
        num = [15, 7, 22, 9, 36, 2, 42, 18]
        sorted_num = quick_sort(num)
        k_largest = find_k_largest(sorted_num, 3)
        self.assertEqual(k_largest, 22)

    def test_find_k_position(self):
        num = [15, 7, 22, 9, 36, 2, 42, 18]
        sorted_num = quick_sort(num)
        k_largest = find_k_largest(sorted_num, 3)
        position = find_k_position(sorted_num, 3)
        self.assertEqual(position, 5)

if __name__ == '__main__':
    unittest.main()
