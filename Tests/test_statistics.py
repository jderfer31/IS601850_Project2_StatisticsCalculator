import unittest
import random
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
import pprint

from ItemsWithSeed import items_with_seed
from RandomlySelectSame import randomly_same


def items_Wout_seed():
    pass


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)

    def test_items_with_seed(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.seed(5)
        number_list = random.sample(nlist, self)
        self.assertEqual(items_with_seed(), num)

    def test_items_Wout_seed(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        number_list = random.sample(nlist, self)
        self.assertEqual(items_Wout_seed(), self)

    def test_randomly_same(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.seed(5)
        number_list = random.sample(nlist, self)
        self.assertEqual(randomly_same(1), self)









if __name__ == '__main__':
    unittest.main()
