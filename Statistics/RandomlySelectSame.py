import random


nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.seed(2)
number_list = random.sample(nlist, 4)
print("number list", number_list)

random.seed(2)
number_list = random.sample(nlist, 4)
print("number list", number_list)
