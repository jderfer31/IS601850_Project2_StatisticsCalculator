import random
from Statistics.NListWithSeed import generator_int_and_float


def population(data, sample_size):
    pp = random.choices(generator_int_and_float(data, sample_size), k=sample_size)
    return pp
