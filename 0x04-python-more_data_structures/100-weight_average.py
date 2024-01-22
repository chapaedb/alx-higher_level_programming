#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        product_sum = sum( x * y for x, y in my_list)
        weight_sum = sum( y for x, y in my_list)
        average = product_sum / weight_sum
    return average
