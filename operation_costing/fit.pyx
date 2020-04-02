import time
import numpy as np
import logging

cimport numpy
cimport cython

from scipy.optimize import least_squares, fmin, fsolve

def modify_residual(x, alpha):
    return max(x, 0) - alpha * max(-x, 0)

modify_residual_vectorized = np.vectorize(modify_residual)

def fit(runtime_model, n_input, n_param, input_arr, runtime_arr, degree_of_confidence):
    global total_elapsed
    total_elapsed = 0

    input_size = len(input_arr)

    if input_arr.dtype is not np.float64:
        input_arr = input_arr.astype(np.float64)

    if runtime_arr.dtype is not np.float64:
        runtime_arr = runtime_arr.astype(np.float64)

    X0 = np.ones(n_param, dtype=np.float64)

    @cython.boundscheck(False)
    @cython.wraparound(False)
    def g(double[:] x, return_params=False):
        alpha = x[0]

        @cython.boundscheck(False)
        @cython.wraparound(False)
        def f(double[:] param):
            # estimate = np.array([runtime_model(param, i) for i in input_arr])
            residual = runtime_model(param, input_arr)

            residual = residual - runtime_arr
            residual = modify_residual_vectorized(residual, alpha)

            return residual

        result = least_squares(f, X0)
        param = result.x

        if return_params:
            return param

        runtime_result = runtime_model(param, input_arr)

        below_arr = runtime_result >= runtime_arr
        below = np.count_nonzero(below_arr)
        above = len(below_arr) - below


        ratio = below / (above + below)

        outer_residual = ratio - degree_of_confidence

        logging.debug('Residual: %.10f'%(abs(outer_residual)))

        return outer_residual

    # result = fmin(g, [1])
    result = fsolve(g, [1.])
    param = g(result, return_params=True)

    print("Total elapsed time for least squares: %f"%total_elapsed)

    return param
