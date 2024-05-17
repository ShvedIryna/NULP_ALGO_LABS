from src.longest_chain import longest_chain, write_and_read_file
import unittest
import os

class TestLongestChain(unittest.TestCase):
    def test_write_and_read_file(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        self.input_file = os.path.join(directory, "..", "src", "wchain.in")
        self.output_file = os.path.join(directory, "..", "src", "wchain.out")
        write_and_read_file(self.input_file, self.output_file)

        with open(self.output_file, "r") as f:
            result = int(f.read().strip())

    def test_longest_chain_1(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(longest_chain(words), 4)

    def test_longest_chain_2(self):
        words = ["word", "anotherword", "abc", "yetanotherword"]
        self.assertEqual(longest_chain(words), 1)

    def test_longets_chain_3(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        self.assertEqual(longest_chain(words), 6)

if __name__ == "__main__":
    main()
