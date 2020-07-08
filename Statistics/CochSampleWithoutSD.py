import math # import Calculator
import statistics # import Statistics funcions


def cochran(proportion, probability, precision):
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


print(cochran(41, 95, 0.06))