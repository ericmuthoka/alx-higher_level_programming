#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()  # Set to store unique integers
    sum = 0

    for num in my_list:
        if num not in unique_nums:
            # If the number isn't in the set, add it to the sum
            sum += num
            unique_nums.add(num)

    return sum
