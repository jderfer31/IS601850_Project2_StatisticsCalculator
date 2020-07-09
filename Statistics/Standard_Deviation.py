from Statistics.Variance import variance
from Calculator.Square_root import sqr
from Statistics.check_emptylist import check

def stddev(data):
    data = check(data)
    var = variance(data)
    squareroot = sqr(var)
    return squareroot
