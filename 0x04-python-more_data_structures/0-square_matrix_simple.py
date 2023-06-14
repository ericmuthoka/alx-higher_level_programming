#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    result = []
    for row in matrix:
        new_row = []
        for num in row:
            # Square each number and append it to the new row
            new_row.append(num ** 2)
        # Append the new row to the result matrix
        result.append(new_row)

    return result
