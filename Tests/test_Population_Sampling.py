import unittest
from Calculator.Calculator import Calculator as cal  # import Calculator
from Statistics.Statistics import Statistics  # import Statistics funcions
from Statistics.NListWithSeed import generator_int_and_float
import math  # import Calculator
import statistics  # import Statistics funcions
import random
from Statistics.Confidence_interval import confidence_interval_bottom
from Statistics.Confidence_interval import result_confidence_interval_bottom_and_top


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        random.seed(5)
        self.confidence_interval_bottom_and_top = confidence_interval_bottom(80, 10, 30)
        self.result = result_confidence_interval_bottom_and_top(80, 10, 30)


    def test_confidence_interval_bottom_and_top(self):
        self.assertEqual(self.confidence_interval_bottom_and_top, self.result)
        pass

if __name__ == '__main__':
    unittest.main()
