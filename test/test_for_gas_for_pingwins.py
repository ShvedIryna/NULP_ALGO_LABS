import unittest
import os
from src.gas_for_pingwins import dfs, find_unreachable_storage

class TestGasPipeline(unittest.TestCase):
    def test_all_storages_reachable(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Сховище_1'], ['Стрий', 'Сховище_2']]
        self.assertEqual(find_unreachable_storage(cities, storages, pipelines), ['Сховище_2'])

    def test_unreachable_storage(self):
        cities = ['Долина', 'Коваль']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Долина', 'Сховище_1']]
        self.assertEqual(find_unreachable_storage(cities, storages, pipelines), ['Сховище_2'])

    def test_transit_cities(self):
        cities = ['Львів', 'Долина', 'Стрий']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Стрий'], ['Стрий', 'Долина'], ['Долина', 'Сховище_1'], ['Долина', 'Сховище_2']]
        self.assertEqual(find_unreachable_storage(cities, storages, pipelines), [])


if __name__ == '__main__':
    unittest.main()
