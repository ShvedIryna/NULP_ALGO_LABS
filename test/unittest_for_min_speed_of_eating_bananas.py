from min_speed_of_eating_bananas import min_speed_of_eating_bananas
import unittest


class TestMyFunction(unittest.TestCase):
    def test_min_speed_of_eating_bananas1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(min_speed_of_eating_bananas(piles, h), 4)

    def test_min_speed_of_eating_bananas2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(min_speed_of_eating_bananas(piles, h), 30)

    def test_min_speed_of_eating_bananas3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(min_speed_of_eating_bananas(piles, h), 23)


if __name__ == '__main__':
    unittest.main()
