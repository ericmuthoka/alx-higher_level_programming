#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    result = []
    for item in my_list:
        if item == search:
            # If item matches the search element, replace it with new element
            result.append(replace)
        else:
            # Otherwise, keep the original item
            result.append(item)

    return result
