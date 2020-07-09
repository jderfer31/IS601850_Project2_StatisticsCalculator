from Calculator.Division import division
from Calculator.Multipule import mul
from Calculator.Square_root import sqr
from Statistics.Standard_Deviation import stddev
from Statistics.NListWithSeed import generator_int_and_float
import math  # import Calculator
import statistics  # import Statistics funcions


def margin_error2(probability, range_s, numb):
    num = generator_int_and_float(range_s, numb)  # should be imported as Random sample generator
    num_values = len(num)
    sd = stddev(num)
    p = probability
    if p == 80:
        z = 1.282
        return round(division(sqr(num_values), mul(z, sd)), 5)
    elif p == 85:
        z = 1.440
        return round(division(sqr(num_values), mul(z, sd)), 5)
    elif p == 90:
        z = 1.645
        return round(division(sqr(num_values), mul(z, sd)), 5)
    elif p == 95:
        z = 1.960
        return round(division(sqr(num_values), mul(z, sd)), 5)
    elif p == 99:
        z = 2.576
        return round(division(sqr(num_values), mul(z, sd)), 5)
    elif p == 99.5:
        z = 2.807
        return round(division(sqr(num_values), mul(z, sd)), 5)
    elif p == 99.9:
        z = 3.291
        return round(division(sqr(num_values), mul(z, sd)), 5)
    else:
        print("please select one interval")


print(margin_error2(99.9, 10, 35))


def result_margin_error2(probability, range_s, numb):
    num = generator_int_and_float(range_s, numb)  # should be imported as Random sample generator
    num_values = len(num)
    sd = statistics.stdev(num)
    p = probability
    if p == 80:
        z = 1.282
        return round(z * sd / math.sqrt(num_values), 5)
    elif p == 85:
        z = 1.440
        return round(z * sd / math.sqrt(num_values), 5)
    elif p == 90:
        z = 1.645
        return round(z * sd / math.sqrt(num_values), 5)
    elif p == 95:
        z = 1.960
        return round(z * sd / math.sqrt(num_values), 5)
    elif p == 99:
        z = 2.576
        return round(z * sd / math.sqrt(num_values), 5)
    elif p == 99.5:
        z = 2.807
        return round(z * sd / math.sqrt(num_values), 5)
    elif p == 99.9:
        z = 3.291
        return round(z * sd / math.sqrt(num_values), 5)
    else:
        print("please select one interval")


print(margin_error2(99.9, 10, 35))
