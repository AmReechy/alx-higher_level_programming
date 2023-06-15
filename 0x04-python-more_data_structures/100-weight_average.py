#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    point = [i * j for i, j in my_list]
    weight = [w for m, w in my_list]
    average = sum(point) / sum(weight)
    return average
