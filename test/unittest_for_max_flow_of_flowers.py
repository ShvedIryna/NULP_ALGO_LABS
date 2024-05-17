import unittest
import os
from scr.max_flow_of_flowers import ford_fulkerson, max_flow, read_graph_from_inputfile

class TestMaxFlow(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'Source': {'A': 10, 'B': 5},
            'A': {'C': 15, 'D': 5},
            'B': {'C': 10, 'D': 20},
            'C': {'Sink': 10},
            'D': {'Sink': 15},
            'Sink': {}
        }

    def test_ford_fulkerson(self):
        max_flow_value = ford_fulkerson(self.graph, 'Source', 'Sink')
        self.assertEqual(max_flow_value, 15)

    def test_read_graph_from_inputfile(self):
        graph, farms, shops = read_graph_from_inputfile(r'C:\Users\Shved Iryna\PycharmProjects\NULP_ALGO_LABS_1\venv\src\roads.csv')
        self.assertIsInstance(graph, dict)
        self.assertIsInstance(farms, list)
        self.assertIsInstance(shops, list)

if __name__ == '__main__':
    unittest.main()
