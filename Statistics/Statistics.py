from Calculator.Calculator import Calculator
from Statistics.CochSampleWithoutSD import cochranwithNOsd
from Statistics.Cochran_Sample_Size import cochran
from Statistics.Confidence_interval import confidence_interval_bottom
from Statistics.Margin_Error import margin_error2
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Sample_random_Sampling import population
from Statistics.Standard_Deviation import stddev
from Statistics.Variance import variance
from Statistics.Zscore import zscore
from Statistics.RandomNumberWithSeed import random_integer
from Statistics.ItemsWoutSeed import items_without_seed
from Statistics.ItemsWithSeed import items_with_seed
from Statistics.NListWithSeed import generator_int_and_float
from Statistics.RandomItem import random_item
from Statistics.RandomNumberWoutSeed import random_integer
from Statistics.RandomlySelectSame import randomly_same
from Statistics.Confidence_interval import confidence_interval_bottom
from Statistics.Sample_random_Sampling import population
from Statistics.NListWithSeed import generator_int_and_float
from Statistics.Margin_Error import margin_error2
from Statistics.Cochran_Sample_Size import cochran
from Statistics.CochSampleWithoutSD import cochranwithNOsd



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
    
    def me(self,probability, data):
        self.result = margin_error2(probability,data)
        return self.result

    def cochran(self,proportion, probability, precision):
        self.result = cochran(proportion,probability,precision)
        return self.result

    def cochranwithNOsd(self,proportion, probability, precision):
        self.result = cochranwithNOsd(proportion,probability,precision)
        return self.result
    

    def sample_random_sampling(self,data, sample_size):
        self.result = population(data,sample_size)
        return self.result

    def c_interval_bottom(self,probability, data):
        self.result = confidence_interval_bottom(probability,data)
        return self.result


    def me(self,probability, data):
        self.result = margin_error2(probability,data)
        return self.result

    def cochran(self,proportion, probability, precision):
        self.result = cochran(proportion,probability,precision)
        return self.result

    def cochranwithNOsd(self,proportion, probability, precision):
        self.result = cochranwithNOsd(proportion,probability,precision)
        return self.result
