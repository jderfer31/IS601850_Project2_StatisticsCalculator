from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.ItemsWithSeed import ItemsWithSeed
from Statistics.ItemsWoutSeed import ItemsWoutSeed
from Statistics.NListWithSeed import NListWithSeed
from Statistics.RandomItem import RandomItem
from Statistics.RandomlySelectSame import RandomlySelectSame
from Statistics.RandomNumberWithSeed import RandomNumberWithSeed
from Statistics.RandomNumberWoutSeed import RandomNumberWoutSeed

class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def itemswithseed(self, data):
        self.result = self.itemswithseed(data)
        return self.result

    def itemswoutseed(self, data):
        self.result = self.itemswoutseed(data)
        return self.result

    def nlistwithseed(self, data):
        self.result = self.nlistwithseed(data)
        return self.result

    def randomitem(self, data):
        self.result = self.randomitem(data)
        return self.result

    def randomlyselectsame(self, data):
        self.result = self.randomlyselectsame(data)
        return self.result

    def randomnumberwithseed(self, data):
        self.result = self.randomnumberwithseed(data)
        return self.result

    def randomnumberwoutseed(self, data):
        self.result = self.randomnumberwoutseed(data)
        return self.result


