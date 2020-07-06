import random

random.seed(3)
print("Random integer between 1 and 10 is ", random.randint(1, 10))

random.seed(6)
x = random.uniform(1.0, 10.0)
print("Random float number between range 1.0 to 10.0 is", x)
