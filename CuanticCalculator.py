#  Library for performing algebraic operations between complex numbers
# Author: José Manuel Gamboa Gómez
import math


def sum_complex(c1, c2):
    """
    It takes two complex numbers, adds them together, and returns the result

    :param c1: A complex number in the form of a list
    :param c2: A complex number in the form of a list
    :return: The sum of the two complex numbers.
    """
    a = c1[0] + c2[0]
    b = c1[1] + c2[1]
    return [a, b]


def product_complex(c1, c2):
    """
    It takes two complex numbers, multiplies them, and returns the result

    :param c1: The first complex number
    :param c2: the complex number to be multiplied
    :return: The product of two complex numbers.
    """
    a = c1[0]*c2[0] - c1[1]*c2[1]
    b = c1[0]*c2[1] + c1[1]*c2[0]
    return [a, b]


def sub_complex(c1, c2):
    """
    Subtracts two complex numbers and returns the result as a string.

    :param c1: The first complex number
    :param c2: The second complex number
    :return: a string.
    """
    a = c1[0] - c2[0]
    b = c1[1] - c2[1]
    return [a, b]


def div_complex(c1, c2):
    """
    It takes two complex numbers, c1 and c2, and returns the quotient of c1 and c2

    :param c1: The first complex number
    :param c2: the complex number to divide by
    :return: A string
    """
    den = c2[0]**2 + c2[1]**2
    a = (c1[0]*c2[0] + c1[1]*c2[1])/den
    b = (c2[0]*c1[1] - c1[0]*c2[1])/den
    return [a, b]


def mod_complex(c):
    """
    It takes a complex number as input and returns its modulus

    :param c: a complex number
    :return: The modulus of the complex number.
    """
    mod = math.sqrt((c[0]**2 + c[1]**2))
    return mod


def conjugation_complex(c):
    """
    It takes a complex number, and returns the complex conjugate of that number

    :param c: a complex number in the form of a list, where c[0] is the real part and c[1] is the imaginary part
    :return: The conjugate of the complex number.
    """
    c[1] = c[1]*-1
    return [c[0], c[1]]


def polar_representation_convert(cartesian_repre):
    """
    It converts a complex number from cartesian to polar representation

    :param cartesian_repre: the cartesian representation of the complex number
    :return: The modulus and the angle of the complex number.
    """
    p = mod_complex(cartesian_repre)
    angle = math.degrees(math.atan(cartesian_repre[1]/cartesian_repre[0]))
    return [p, angle]


def cartesian_representation_convert(polar_repre):
    """
    It converts a polar representation of a complex number to a cartesian representation

    :param polar_repre: a list of two elements, the first element is the radius, the second element is the angle
    :return: The cartesian representation of the polar representation.
    """
    a = polar_repre[0]*math.cos(polar_repre[1])
    b = polar_repre[0]*math.sin(polar_repre[1])
    return [a, b]


def phase_complex_number(comp):
    """
    It takes a complex number and returns the phase of that complex number

    :param comp: a complex number
    :return: The phase of the complex number.
    """
    phase = math.degrees(math.atan(comp[1]/comp[0]))
    return phase


def main():
    # print(sum_complex([3, -1], [1, 4]))
    # print(product_complex([-3, -1], [1, -2]))
    # print(sub_complex([3, -4], [1, -2]))
    # print(div_complex([0, 3], [-1, -1]))
    # print(mod_complex([4, 3]))
    # print(conjugation_complex([4, -2]))
    # print(conjugation_complex([27, 5]))
    # print(polar_representation_convert([1, 1]))
    # print(cartesian_representation_convert([3, math.pi/3]))
    # print(phase_complex_number([1, 1]))
    print(mod_complex([1/(2**(1/2)), -7/(2**(1/2))])**2)


if __name__ == '__main__':
    main()
