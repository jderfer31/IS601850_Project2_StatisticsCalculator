from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Multipule import mul
from Calculator.Subtraction import subtraction
from Calculator.Square import sq
from Calculator.Square_root import sqr


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def mul(self, a, b):
        self.result = mul(a, b)
        return self.result

    def sq(self, a):
        self.result = sq(a)
        return self.result

    def sqr(self, a):
        self.result = sqr(a)
        return self.result
