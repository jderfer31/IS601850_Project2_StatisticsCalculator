from Statistics.Variance import variance
from Calculator.Square_root import sqr


def stddev(data):
    var = variance(data)
    squareroot = sqr(var)
    return squareroot
