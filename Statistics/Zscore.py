from Statistics.Mean import mean
from Statistics.Standard_Deviation import stddev
from Calculator.Subtraction import subtraction
from Calculator.Division import  division


def zscore(data, x):
    m = mean(data)
    sd = stddev(data)
    num = subtraction(m, x)
    result = division(sd, num)
    return result


