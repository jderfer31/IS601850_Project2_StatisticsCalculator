import unittest
from Statistics.Confidence_interval import confidence_interval_bottom
from Statistics.Confidence_interval import result_confidence_interval_bottom_and_top
from Statistics.Sample_random_Sampling import population
from Statistics.NListWithSeed import generator_int_and_float
from Statistics.Margin_Error import margin_error2
from Statistics.Margin_Error import result_margin_error2
from Statistics.Cochran_Sample_Size import cochran
from Statistics.Cochran_Sample_Size import result_cochran
from Statistics.CochSampleWithoutSD import cochranwithNOsd
from Statistics.CochSampleWithoutSD import result_cochranwithNOsd


class MyTestCase(unittest.TestCase):
    def test_confidence_interval_bottom(self):
        self.assertEqual(confidence_interval_bottom(80, 10, 30), result_confidence_interval_bottom_and_top(80, 10, 30))

    def test_Sample_random_Sampling(self):
        self.assertNotEqual(population(10, 30), generator_int_and_float(10, 30))

    def test_margin_error(self):
        self.assertEqual(margin_error2(80, 10, 30), result_margin_error2(80, 10, 30))

    def test_Cochran_Sample_Size(self):
        self.assertEqual(cochran(50, 95, 0.05), result_cochran(50, 95, 0.05))

    def test_cochranwithNOsd(self):
        self.assertEqual(cochranwithNOsd(41, 59, 0.06), result_cochranwithNOsd(41, 59, 0.06))


if __name__ == '__main__':
    unittest.main()
