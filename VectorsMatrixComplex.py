#  Library for performing operations with vectors and complex matrices.
# Author: José Manuel Gamboa Gómez
import math

import CuanticCalculator as cc
import numpy as np


def print_vector(vector):
    """
    It prints the elements of a vector

    :param vector: the vector to print
    """
    for i in range(len(vector)):
        print('%s' % vector[i])


def print_matrix(matrix):
    """
    It prints the matrix

    :param matrix: a 2D array of numbers
    """
    for i in range(len(matrix)):
        print(matrix[i])


def add_vectors(v, w):
    """
    > For each element in the vector `v`, add it to the corresponding element in the vector `w` and append the result
    to the vector `vector_result`

    :param v: a vector of complex numbers
    :param w: a vector of complex numbers
    :return: A vector of complex numbers.
    """
    vector_result = []
    for j in range(len(v)):
        vector_result.append(cc.sum_complex(v[j], w[j]))
    return vector_result


def inverse_complex(complex):
    """
    This function takes a complex number as input and returns the inverse of that complex number

    :param complex: a list of two numbers, the real and imaginary parts of a complex number
    :return: The inverse of the complex number.
    """
    inv_comp = [complex[0]*-1, complex[1]*-1]
    return inv_comp


def additive_inverse(vector):
    """
    It takes a vector of complex numbers and returns a vector of complex numbers, where each complex number is the
    additive inverse of the corresponding complex number in the original vector

    :param vector: a list of complex numbers
    :return: The additive inverse of the vector.
    """
    inverse_vector = []
    for i in range(len(vector)):
        inverse_vector.append(inverse_complex(vector[i]))
    return inverse_vector


def product_scalar_vector(scalar, vector):
    """
    It multiplies a scalar by a vector

    :param scalar: a complex number
    :param vector: a list of complex numbers
    :return: A vector with the same length as the input vector, but with each element multiplied by the scalar.
    """
    vector_result = []
    for i in range(len(vector)):
        vector_result.append(cc.product_complex(scalar, vector[i]))
    return vector_result


def add_matrix_complex(m1, m2):
    """
    It takes two matrices and returns the sum of the two matrices

    :param m1: a matrix of complex numbers
    :param m2: a matrix of complex numbers
    :return: A matrix of the same size as the input matrices, with the corresponding elements added together.
    """
    matrix_result = []
    for i in range(len(m1)):
        matrix_result.append(add_vectors(m1[i], m2[i]))
    return matrix_result


def inverse_add_matrix(matrix):
    """
    It takes a matrix as input and returns the additive inverse of that matrix

    :param matrix: a matrix of numbers
    :return: A matrix with the additive inverse of each element in the original matrix.
    """
    matrix_inv = []
    for i in range(len(matrix)):
        matrix_inv.append(additive_inverse(matrix[i]))
    return matrix_inv


def product_scalar_matrix(scalar, matrix):
    """
    It takes a scalar and a matrix and returns the product of the scalar and the matrix

    :param scalar: of complex number
    :param matrix: a matrix of complex numbers
    :return: A matrix
    """
    matrix_product = []
    for j in range(len(matrix)):
        matrix_product.append(product_scalar_vector(scalar, matrix[j]))
    return matrix_product


def transpose_matrix(matrix):
    """
    For each row in the matrix, create a new row in the transpose by taking the corresponding column in the matrix

    :param matrix: a list of lists
    :return: A new matrix that is the transpose of the original matrix.
    """
    transpose = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in matrix:
            new_row.append(j[i])
        transpose.append(new_row)
    return transpose


def conjugate_vector(vector):
    """
    It takes a vector and returns the conjugate of that vector

    :param vector: a list of complex numbers
    :return: A vector with the conjugate of each element of the vector.
    """
    vector_result = []
    for i in range(len(vector)):
        vector_result.append(cc.conjugation_complex(vector[i]))
    return vector_result


def conjugate_matrix(matrix):
    """
    It takes a matrix and returns the conjugate of that matrix

    :param matrix: a list of lists of complex numbers
    :return: A matrix with the conjugate of each vector in the matrix.
    """
    conjugate = []
    for i in range(len(matrix)):
        conjugate.append(conjugate_vector(matrix[i]))
    return conjugate


def dagger_matrix(matrix):
    """
    > The dagger of a matrix is the conjugate transpose of the matrix

    :param matrix: The matrix to be transposed
    :return: The conjugate transpose of the matrix.
    """
    temp = transpose_matrix(matrix)
    matrix_result = conjugate_matrix(temp)
    return matrix_result


def mult_matrix(a, b):
    """
    For each element in the result matrix, multiply the corresponding row of the first matrix by the corresponding
    column of the second matrix and sum the results.

    :param a: The first matrix
    :param b: the matrix to be multiplied
    :return: A matrix with the result of the multiplication of the two matrices.
    """
    matrix_result = [[[0, 0] for y in range(len(b[0]))] for x in range(len(a))]
    for j in range(len(a)):
        for k in range(len(b[0])):
            for n in range(len(b)):
                matrix_result[j][k] = cc.sum_complex(matrix_result[j][k], cc.product_complex(a[j][n], b[n][k]))
    return matrix_result


def inner_product_vectors(v, w):
    """
    It takes two vectors and returns their inner product

    :param v: a list of complex numbers
    :param w: the vector to be multiplied
    :return: The inner product of two vectors.
    """
    result = [0, 0]
    for i in range(len(v)):
        result = cc.sum_complex(result, cc.product_complex(v[i], w[i]))
    return result


def action_matrix_vector(matrix, vector):
    """
    > For each row of the matrix, compute the inner product of that row with the vector

    :param matrix: a list of lists, each of which is a row of the matrix
    :param vector: a list of numbers
    :return: A vector
    """
    vector_result = []
    for j in range(len(matrix)):
        vector_result.append(inner_product_vectors(matrix[j], vector))
    return vector_result


def norm_vector(v):
    """
    It calculates the norm of a vector

    :param v: a list of complex numbers
    :return: The norm of the vector.
    """
    result = 0
    for i in range(len(v)):
        result += cc.mod_complex(cc.product_complex(v[i], v[i]))
    return math.sqrt(result)


def distance_vectors(u, v):
    """
    It takes two vectors and returns the distance between them

    :param u: a vector of complex numbers
    :param v: the vector we're trying to find the closest vector to
    :return: The distance between two vectors.
    """
    temp_vector = []
    for j in range(len(u)):
        temp_vector.append(cc.sub_complex(u[j], v[j]))
    return norm_vector(temp_vector)


def hermitian_validate(matrix):
    """
    It checks if the matrix is hermitian or not.

    :param matrix: The matrix to be validated
    :return: the hermitian matrix.
    """
    matrix_dagger = dagger_matrix(matrix)
    flag = True
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] != matrix_dagger[x][y]:
                flag = False
                break
    if flag:
        return print('It is a hermitian matrix')
    else:
        return print('Not a Hermitian matrix')
