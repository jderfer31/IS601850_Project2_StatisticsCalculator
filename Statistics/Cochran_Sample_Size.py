from Calculator.Division import division
from Calculator.Multipule import mul
from Calculator.Square import sq


def cochran(proportion, probability, precision):
    p = probability
    p1 = float(proportion / 100)
    q = float(1 - p1)
    me = float(precision)
    if p == 80:
        z = 1.282
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    elif p == 85:
        z = 1.440
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    elif p == 90:
        z = 1.645
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    elif p == 95:
        z = 1.960
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    elif p == 99:
        z = 2.576
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    elif p == 99.5:
        z = 2.807
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    elif p == 99.9:
        z = 3.291
        return round(division(sq(me), mul(mul(p1, q), sq(z) )), 5)
    else:
        print("please select one interval")


print(cochran(50, 95, 0.05))


def result_cochran(proportion, probability, precision):
    p = probability
    p1 = float(proportion / 100)
    q = float(1 - p1)
    me = precision
    if p == 80:
        z = 1.282
        return round(z ** 2 * p1 * q / me ** 2, 5)
    elif p == 85:
        z = 1.440
        return round(z ** 2 * p1 * q / me ** 2, 5)
    elif p == 90:
        z = 1.645
        return round(z ** 2 * p1 * q / me ** 2, 5)
    elif p == 95:
        z = 1.960
        return round(z ** 2 * p1 * q / me ** 2, 5)
    elif p == 99:
        z = 2.576
        return round(z ** 2 * p1 * q / me ** 2, 5)
    elif p == 99.5:
        z = 2.807
        return round(z ** 2 * p1 * q / me ** 2, 5)
    elif p == 99.9:
        z = 3.291
        return round(z ** 2 * p1 * q / me ** 2, 5)
    else:
        print("please select one interval")


print(cochran(50, 95, 0.05))
