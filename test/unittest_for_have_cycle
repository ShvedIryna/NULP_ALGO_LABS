import unittest
from have_cycle import have_cycle_in_graph, read_graph_from_inputfile


class TestHaveCycle(unittest.TestCase):

    def test_have_cycle(self):
        graph_with_cycle = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
        self.assertTrue(have_cycle_in_graph(graph_with_cycle))

    def test_graph_without_cycle(self):
        graph_without_cycle = {1: [2, 3], 2: [1], 3: [1]}
        self.assertFalse(have_cycle_in_graph(graph_without_cycle))

    def test_graph_empty(self):
        empty_graph = {}
        self.assertFalse(have_cycle_in_graph(empty_graph))


if __name__ == '__main__':
    unittest.main()
