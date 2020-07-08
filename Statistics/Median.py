from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.check_emptylist import check

def median(data):
    data = check(data)
    if len(data) % 2 == 0:
        data.sort()
        middleindex1 = int(division(2, len(data)))
        middleindex2 = int(subtraction(1, middleindex1))
        middleval1 = data[middleindex1]
        middleval2 = data[middleindex2]
        result = mean([middleval1, middleval2])
        return result
    else:
        data.sort()
        middleindex = int(division(2, len(data)))
        middleval = data[middleindex]
        return middleval







