import numpy
cimport numpy
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def constant(double[:] param, double[:, :] input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = param[0]

    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def linear(double[:] param, double[:, :] input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = param[0]*input_arr[i, 0] + param[1]

    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def quadratic(double[:] param, double[:, :] input_arr):
    input_size = input_arr.shape[0]

    result = numpy.zeros(input_size, dtype=numpy.float64)

    for i in range(input_size):
        result[i] = param[0]*input_arr[i, 0]**2 + param[1]*input_arr[i, 0] + param[2]

    return result


# @cython.boundscheck(False)
# @cython.wraparound(False)
# cpdef double linear(double[:] param, double[:] x):
#     return param[0]*x[0] + param[1]

# @cython.boundscheck(False)
# @cython.wraparound(False)
# cpdef double quadratic(double[:] param, double[:] x):
#     return param[0]*x[0]**2 + param[1]*x[1] + param[2]

