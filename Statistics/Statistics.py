from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.Standard_Deviation import stddev
from Statistics.Zscore import zscore
from Statistics.RandomNumberWithSeed import random_integer
from Statistics.ItemsWoutSeed import items_without_seed
from Statistics.ItemsWithSeed import items_with_seed
from Statistics.NListWithSeed import generator_int_and_float
from Statistics.RandomItem import random_item
from Statistics.RandomNumberWoutSeed import random_integer
from Statistics.RandomlySelectSame import randomly_same



class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result
    def median(self, data):
        self.result = median(data)
        return self.result
    def mode(self, data):
        self.result = mode(data)
        return self.result
    def variance(self, data):
        self.result = variance(data)
        return self.result
    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def zscore(self, data, x):
        self.result = zscore(data, x)
        return self.result

    def random_integer(self, data, x):
        self.result = random_integer(data, x)
        return self.result

    def items_without_seed(self, data, x):
        self.result = items_without_seed(data, x)
        return self.result

    def items_with_seed(self, data, x):
        self.result = items_with_seed(data, x)
        return self.result

    def generator_int_and_float(self, data, x):
        self.result = generator_int_and_float(data, x)
        return self.result

    def random_item(self, data, x):
        self.result = random_item(data, x)
        return self.result

    def randomly_same(self, data, x):
        self.result = randomly_same(data, x)
        return self.result


