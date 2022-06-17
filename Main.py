import math

import CuanticCalculator as cc
import VectorsMatrixComplex as vmc
import numpy as np


def main():

    # print(cc.sum_complex([3, -1], [1, 4]))
    # print(cc.product_complex([-3, -1], [1, -2]))
    # print(cc.sub_complex([3, -4], [1, -2]))
    # print(cc.div_complex([0, 3], [-1, -1]))
    # print(cc.mod_complex([4, 3]))
    # print(cc.conjugation_complex([4, -2]))
    # print(cc.conjugation_complex([27, 5]))
    # print(cc.polar_representation_convert([1, 1]))
    # print(cc.cartesian_representation_convert([3, math.pi / 3]))
    # print(cc.phase_complex_number([1, 1]))

    ex_sum_v = [[6, -4], [7, 3], [4.2, -8.1], [0, -3]]
    ex_sum_w = [[16, 2.3], [0, -7], [6, 0], [0, -4]]
    # vmc.print_vector(vmc.add_vectors(ex_sum_v, ex_sum_w))
    # vmc.print_vector(vmc.add_vectors(vmc.additive_inverse(ex_sum_v), ex_sum_v))

    ex_scalar = [3, 2]
    ex_ps_v = [[6, 3], [0, 0], [5, 1], [4, 0]]
    # vmc.print_vector(vmc.product_scalar_vector(ex_scalar, ex_ps_v))

    ex_add_matrix_v = [[[0, 5], [-3, 1], [2, 2], [0, 9]], [[3, -8], [8, 0], [1, 8], [1, -1]], [[0, 4], [1, 5], [-3, -4], [4, 2]], [[-7, -1], [0, -2], [0, 0], [6, 0]]]
    ex_add_matrix_w = [[[2, 0], [1, -1], [9, -2], [0, 0]], [[1, 1], [5, 0], [4, -6], [3, 2]], [[9, 2], [4, 6], [10, 0], [1, -7]], [[0, 0], [3, -2], [1, 7], [4, 0]]]
    # vmc.print_matrix(vmc.add_matrix_complex(ex_add_matrix_v, ex_add_matrix_w))
    # vmc.print_matrix(vmc.inverse_add_matrix(ex_add_matrix_w))
    # vmc.print_matrix(vmc.product_scalar_matrix(ex_scalar, ex_add_matrix_v))

    ex_transpose_matrix = [[1, 2, 3], [4, 5, 6]]
    # vmc.print_matrix(ex_transpose_matrix)
    # print('<- Matriz Transpuesta ->')
    # vmc.print_matrix(vmc.transpose_matrix(ex_transpose_matrix))

    # vmc.print_matrix(vmc.conjugate_matrix(ex_add_matrix_v))

    # vmc.print_matrix(vmc.dagger_matrix(ex_add_matrix_v))

    a = [[[3, 2], [0, 0], [5, -6]], [[1, 0], [4, 2], [0, 1]], [[4, -1], [0, 0], [4, 0]]]
    b = [[[5, 0], [2, -1], [6, -4]], [[0, 0], [4, 5], [2, 0]], [[7, -4], [2, 7], [0, 0]]]
    # vmc.print_matrix(vmc.mult_matrix(a, b))

    action_a = [[[-1, 0], [1, 1], [0, 0]], [[2, -1], [0, 0], [1, 0]], [[0, 0], [1, -1], [0, 1]]]
    action_v = [[1, 0], [1, 1], [0, 1]]
    # vmc.print_vector(vmc.action_matrix_vector(action_a, action_v))

    v = [[3, 0], [-6, 0], [2, 0]]
    # print(vmc.norm_vector(v))

    quiz = [[1, 0], [0, 1], [1, -3]]
    quiz1 = [[2, 1], [0, 1], [2, 0]]
    print(vmc.inner_product_vectors(quiz, quiz1))

    quiz2 = [[8.2, 5.3], [8.1, -8.0]]
    print(vmc.norm_vector(quiz2))

    u = [[2, 1], [0, 0], [4, -5]]
    v2 = [[1, 1], [2, 1], [0, 0]]
    # print(vmc.distance_vectors(u, v2))

    hermitian_matrix = [[[5, 0], [4, 5], [6, -16]], [[4, -5], [13, 0], [7, 0]], [[6, 16], [7, 0], [-2.1, 0]]]
    # vmc.hermitian_validate(hermitian_matrix)


if __name__ == '__main__':
    main()
