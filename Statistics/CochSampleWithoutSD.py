from Calculator.Division import division
from Calculator.Multipule import mul
from Calculator.Square import sq


def cochranwithNOsd(proportion, probability, precision):
    p = probability
    p1 = float(proportion / 100)
    q = float(1 - p1)
    me = precision
    e = division(2, me)
    if p == 80:
        z = 1.282
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    elif p == 85:
        z = 1.440
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    elif p == 90:
        z = 1.645
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    elif p == 95:
        z = 1.960
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    elif p == 99:
        z = 2.576
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    elif p == 99.5:
        z = 2.807
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    elif p == 99.9:
        z = 3.291
        return round(mul(mul(q, p1), sq(division(e, z))), 5)
    else:
        print("please select one interval")


def result_cochranwithNOsd(proportion, probability, precision):
    p = probability
    print(p)
    p1 = float(proportion / 100)
    print(p1)
    q = float(1 - p1)
    print(q)
    me = precision
    e = me / 2
    print(e)
    if p == 80:
        z = 1.282
        return round(q * p1 * (z / e) ** 2, 5)  # 41%*
    elif p == 85:
        z = 1.440
        return round(q * p1 * (z / e) ** 2, 5)
    elif p == 90:
        z = 1.645
        return round(q * p1 * (z / e) ** 2, 5)
    elif p == 95:
        z = 1.960
        print((z / e) ** 2)
        return round(q * p1 * (z / e) ** 2, 5)  # 41%*
    elif p == 99:
        z = 2.576
        return round(q * p1 * (z / e) ** 2, 5)
    elif p == 99.5:
        z = 2.807
        return round(q * p1 * (z / e) ** 2, 5)
    elif p == 99.9:
        z = 3.291
        return round(q * p1 * (z / e) ** 2, 5)
    else:
        print("please select one interval")


print(cochranwithNOsd(41, 95, 0.06))
