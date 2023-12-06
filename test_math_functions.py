from math_functions import *


def test_calc_addition():
    output = add_numbers(2, 4)
    assert output == 6


def test_calc_subtraction():
    output = subtract_numbers(2, 4)
    assert output == -2


def test_calc_multiply():
    output = multiply_numbers(2, 4)
    assert output == 8


def test_calc_multiply_pass():
    output = multiply_numbers(4, 4)
    assert output == 16


def test_calc_divide():
    output = divide_numbers(10, 2)
    assert output == 5


def test_calc_sum():
    output = calc_sum(25, 20, 29)
    assert output == 74


def test_calc_product():
    output = calc_product(10, 20, 27)
    assert output == 5400
