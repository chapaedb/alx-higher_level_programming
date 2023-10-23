#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    c = tuple_b[0] if len(tuple_b) > 0 else 0
    d = tuple_b[1] if len(tuple_b) > 1 else 0
    sum_a = a + c
    sum_b = b + d
    return (sum_a, sum_b)
