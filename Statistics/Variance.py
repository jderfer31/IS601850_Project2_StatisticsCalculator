from Statistics.Mean import mean
# from Calculator.Division import division
# from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Square import sq
from Statistics.check_emptylist import check

def variance(data):
    data = check(data)
    average = mean(data)
    a = []
    for i in data:
        a.append(sq(subtraction(average, i)))
    return mean(a)
