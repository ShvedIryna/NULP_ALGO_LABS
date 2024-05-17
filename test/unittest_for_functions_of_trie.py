import unittest
import os
from src.function_of_trie import TrieNode, Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.patterns = ["class", "app", "trie", "bonus", "note"]

    def test_insert_word(self):
        for pattern in self.patterns:
            self.trie.insert_word(pattern)
        self.assertTrue(self.trie.search_word("class"))
        self.assertTrue(self.trie.search_word("note"))

    def test_search_word(self):
        for pattern in self.patterns:
            self.trie.insert_word(pattern)

        self.assertTrue(self.trie.search_word("class"))
        self.assertTrue(self.trie.search_word("trie"))

    def test_search_trie(self):
        for pattern in self.patterns:
            self.trie.insert_word(pattern)

        self.assertTrue(self.trie.search_trie("ap"))
        self.assertTrue(self.trie.search_trie("n"))

        self.assertFalse(self.trie.search_trie("z"))
        self.assertFalse(self.trie.search_trie("abc"))


if __name__ == '__main__':
    unittest.main()
