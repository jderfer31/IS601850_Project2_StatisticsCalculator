import random

my_randoms=[]
random.seed(5)

for i in range (10):
    my_randoms.append(random.randrange(1,10))

print("Printing list of 10 random integers")
print (my_randoms)


randomFloatList = []
random.seed(5)

for i in range(0, 10):
    x = round(random.uniform(1.0, 10.0), 2)
    randomFloatList.append(x)

print("Printing list of 10 random float numbers")
print(randomFloatList)
