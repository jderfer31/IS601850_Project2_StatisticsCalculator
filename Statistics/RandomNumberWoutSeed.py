import numpy as np
import random

data = []

for row in range(0,10):
    c = round(np.random.uniform(100,10),2)
    data.append(c)
print(data)

X = random.randint(1,100)
print(X)

for i in range(0,10):
    Inte = random.randint(1,100)
    data.append(Inte)
print(data)

sample = random.choices(data, k=10)
print(sample)
