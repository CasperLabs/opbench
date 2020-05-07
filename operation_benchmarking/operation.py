import time
import progressbar

import pandas as pd
import numpy as np

from math import ceil

from scipy.optimize import least_squares, fmin, fsolve

from operation_benchmarking.fit import fit, fit_constant
from operation_benchmarking.models import constant, linear, quadratic
from operation_benchmarking.plotting import (
    plot_single_input_operation,
    plot_argumentless_operation,
)
from operation_benchmarking.helper import parse_benchmark_result


class Operation:
    def __init__(self):
        self.inputs = []

    def generate_inputs(self, n_input):
        for i in range(n_input):
            self.inputs.append(self._generate_input())

    def execute(self, input_):
        raise Exception("This should be implemented")

    def _generate_input(self):
        raise Exception("This should be implemented")

    def map_input(self):
        raise Exception("This should be implemented")

    def get_n_model_param(self):
        raise Exception("This should be implemented")

    def get_constant_term_idx(self):
        raise Exception("This should be implemented")

    def get_model_input_size(self):
        raise Exception("This should be implemented")

    def get_runtime_model(self):
        raise Exception("This should be implemented")

    def get_name(self):
        raise Exception("This should be implemented")

    def get_model_definition(self):
        raise Exception("This should be implemented")

    def get_model_parameter_labels(self):
        raise Exception("This should be implemented")

    def get_model_variable_descriptions(self):
        raise Exception("This should be implemented")

    def get_model_variable_units(self):
        raise Exception("This should be implemented")

    def batch_execute(self, n_executions, input_):
        for i in range(n_executions):
            self.execute(input_)

    def run_test(self, n_executions, opath):

        ofile = open(opath, "w")

        bar = progressbar.ProgressBar(max_value=len(self.inputs))

        ofile.write("args,n_exec,total_elapsed_time\n")

        for n, input_ in enumerate(self.inputs):
            start = time.time()
            self.batch_execute(n_executions, input_)

            end = time.time()

            time_vars = self.map_input(input_)

            elapsed_time = end - start

            ofile.write(
                '"'
                + str(time_vars)
                + '",'
                + str(n_executions)
                + ",%.6e" % elapsed_time
                + "\n"
            )
            ofile.flush()
            bar.update(n)

            # print(time_vars, elapsed_time)
        ofile.close()

    def fit_parameters(
        self,
        benchmark_data_file,
        degree_of_confidence,
        row_limit=None,
        x0=None,
        bounds=None,
        ignore_input_mismatch=False,
    ):

        input_arr, runtime_arr = parse_benchmark_result(
            benchmark_data_file, row_limit=row_limit
        )

        n_model_param = self.get_n_model_param()
        model_input_size = self.get_model_input_size()

        if False in [len(i) == model_input_size for i in input_arr] and not ignore_input_mismatch:
            raise Exception("Number of arguments in data file does not match operation definition")

        if model_input_size == 0:
            param = (fit_constant(runtime_arr, degree_of_confidence),)
        else:
            param = fit(
                self,
                input_arr,
                runtime_arr,
                degree_of_confidence,
                x0=x0,
                bounds=bounds,
            )

        return param

    def plot_model_performance(self, param, data_file, output_file, row_limit=None):
        if self.get_model_input_size() == 0:
            plot_argumentless_operation(
                self, param[0], data_file, output_file, row_limit=row_limit
            )
        elif self.get_model_input_size() == 1:
            plot_single_input_operation(
                self, param, data_file, output_file, row_limit=row_limit
            )


class LinearOperation(Operation):
    def runtime_model(self, param, x):
        a, b = param
        x_ = x[0]

        return a * x_ + b

    def get_n_model_param(self):
        return 2

    def get_model_input_size(self):
        return 1

    def get_constant_term_idx(self):
        return 1

    def get_runtime_model(self):
        return linear

    def get_model_definition(self):
        return "f(x) = a*x + b"

    def get_model_parameter_labels(self):
        return ["a", "b"]


class QuadraticOperation(Operation):
    def runtime_model(self, param, x):
        a, b, c = param
        x_ = x[0]

        return a * x_ ** 2 + b * x_ + c

    def get_n_model_param(self):
        return 3

    def get_model_input_size(self):
        return 1

    def get_constant_term_idx(self):
        return 2

    def get_runtime_model(self):
        return quadratic

    def get_model_definition(self):
        return "f(x) = a*x^2 + b*x + c"

    def get_model_parameter_labels(self):
        return ["a", "b", "c"]


class ConstantOperation(Operation):
    def runtime_model(self, param, x):
        return x[0]

    def get_n_model_param(self):
        return 1

    def get_model_input_size(self):
        return 0

    def get_constant_term_idx(self):
        return 0

    def get_runtime_model(self):
        return constant

    def get_model_definition(self):
        return "f(x) = c"

    def get_model_parameter_labels(self):
        return ["c"]

    def get_model_variable_descriptions(self):
        return []

    def get_model_variable_units(self):
        return []
