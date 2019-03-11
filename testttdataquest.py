import numpy as numpy
from numpy.random import randint, seed

equal_distances = 0

for i in range (9):
    print(i)
    seed = numpy.random.seed(i)
    distribution = numpy.random.randint(0,1001, size=10)
    print(distribution, "\n")
    mean = numpy.mean(distribution)
    sum_distance_below, sum_distance_above = 0, 0
    for j in distribution:
        if j < mean:
            sum_distance_below += (j-mean)
        elif j > mean:
            sum_distance_above += (mean-j)
    if sum_distance_above == sum_distance_below:
        equal_distances += 1

print(equal_distances)
# At the end equal_distances should have a value of 5000