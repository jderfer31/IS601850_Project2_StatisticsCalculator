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
