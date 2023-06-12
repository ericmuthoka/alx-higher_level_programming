#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with 0 if smaller than 2 elements
    tuple_a += (0, 0)[:2 - len(tuple_a)]
    tuple_b += (0, 0)[:2 - len(tuple_b)]
    # Perform element-wise addition and return result as a tuple
    return tuple(map(sum, zip(tuple_a, tuple_b)))
