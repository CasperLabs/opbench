import numpy as np
from operation_benchmarking import Operation
from .helper import randrange_logarithmic
import random

from operation_benchmarking.models import quadratic


LOWER_LIMIT = 10
UPPER_LIMIT = 1000


def selection_sort(collection):
    """Pure implementation of the selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    return collection


class SelectionSortOperation(Operation):
    def execute(self, input_arr):
        return selection_sort(input_arr[0])

    def _generate_input(self):
        array_size = random.randrange(LOWER_LIMIT, UPPER_LIMIT)
        # array_size = randrange_logarithmic(LOWER_LIMIT, UPPER_LIMIT)
        result = list(range(array_size))
        random.shuffle(result)

        # import ipdb; ipdb.set_trace()
        return (result,)

    def map_input(self, input_arr):
        a = input_arr[0]

        return (len(a),)

    def runtime_model(self, param, x):
        a, b, c = param
        x_ = x[0]

        return a * x_ ** 2 + b * x_ + c

    def get_n_model_param(self):
        return 3

    def get_model_input_size(self):
        return 1

    def get_runtime_model(self):
        return quadratic
