import numpy


def constant(param, input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = param[0]

    return result


def linear(param, input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = param[0] * input_arr[i, 0] + param[1]

    return result


def quadratic(param, input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = (
            param[0] * input_arr[i, 0] ** 2 + param[1] * input_arr[i, 0] + param[2]
        )

    return result


def linear_two_arg(param, input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = param[0] * input_arr[i, 0] + param[1] * input_arr[i, 1] + param[2]

    return result
