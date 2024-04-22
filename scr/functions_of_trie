class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word = str):
        current_node = self.root
        for letter in word:
            current_node = current_node.children[letter]
        current_node.leaf = True

    def search_word(self, word: str):
        current_node = self.root
        for letter in word:
            current_node = current_node.children.get(letter)
            if current_node is None:
                return False
            
        return current_node.leaf and current_node

    def search_trie(self, prefix: str):
        current_node = self.root
        for letter in prefix:
            current_node = current_node.children.get(letter)
        if not current_node:
            return False
        return True
