from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multipule import mul
from Calculator.Square_root import sqr
from Statistics.Standard_Deviation import stddev
from Statistics.NListWithSeed import generator_int_and_float
from Statistics.Mean import mean
import math
import statistics

sample = generator_int_and_float(10, 35)


def confidence_interval_bottom(probability, data):
    num = data
    num_values = len(num)
    sd = stddev(num)
    avg = mean(num)
    p = probability
    if p == 80:
        z = 1.282
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)

    elif p == 85:
        z = 1.440
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)
    elif p == 90:
        z = 1.645
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)
    elif p == 95:
        z = 1.960
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)
    elif p == 99:
        z = 2.576
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)
    elif p == 99.5:
        z = 2.807
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)
    elif p == 99.9:
        z = 3.291
        return round(subtraction(division(sqr(num_values), mul(z, sd)), avg), 5)
    else:
        print("please select one interval")


def result_confidence_interval_bottom(probability, data):
    num = data  # should be imported as Random sample generator
    num_values = len(num)
    sd = statistics.stdev(num)
    avg = statistics.mean(num)
    p = probability
    if p == 80:
        z = 1.282
        return round(avg - (z * sd / math.sqrt(num_values)), 5)

    elif p == 85:
        z = 1.440
        return round(avg - (z * sd / math.sqrt(num_values)), 5)
    elif p == 90:
        z = 1.645
        return round(avg - (z * sd / math.sqrt(num_values)), 5)
    elif p == 95:
        z = 1.960
        return round(avg - (z * sd / math.sqrt(num_values)), 5)
    elif p == 99:
        z = 2.576
        return round(avg - (z * sd / math.sqrt(num_values)), 5)
    elif p == 99.5:
        z = 2.807
        return round(avg - (z * sd / math.sqrt(num_values)), 5)
    elif p == 99.9:
        z = 3.291
        return round(avg - (z * sd / math.sqrt(num_values)), 5)
    else:
        print("please select one interval")
