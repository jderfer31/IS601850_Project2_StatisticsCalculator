import random
import numpy as np


def generator_int_and_float(nums, sample_size):
    data = []
    random.seed(5)
    for row in range(0, sample_size):
        c = round(np.random.uniform(0, nums), 2)
        data.append(c)
    for i in range(0, sample_size):
        inte = random.randint(1, nums)
        data.append(inte)
    sample = random.choices(data, k=sample_size)
    return sample
