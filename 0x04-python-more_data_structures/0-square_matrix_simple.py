#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()
    n = len(new_mat)
    for row in range(len(new_mat)):
        new_mat[row] = list(map(lambda x: x ** 2, new_mat[row]))
    return new_mat
