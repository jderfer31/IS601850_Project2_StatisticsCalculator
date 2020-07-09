from Statistics.Mean import mean
from Statistics.Standard_Deviation import stddev
from Calculator.Subtraction import subtraction
from Calculator.Division import  division
from Statistics.check_emptylist import check

def zscore(data, x):
    data = check(data)
    m = mean(data)
    sd = stddev(data)
    num = subtraction(m, x)
    result = division(sd, num)
    return result


