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
        self.model_definition = None
        self.model_parameter_labels = None
        self.model_variable_descriptions = None
        self.model_variable_units = None
        self.name = None

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

    def set_name(self, name):
        self.name = name

    def set_model_definition(self, model_definition):
        self.model_definition = model_definition

    def set_model_parameter_labels(self, model_parameter_labels):
        self.model_parameter_labels = model_parameter_labels

    def set_model_variable_descriptions(self, model_variable_descriptions):
        self.model_variable_descriptions = model_variable_descriptions

    def set_model_variable_units(self, model_variable_units):
        self.model_variable_units = model_variable_units

    def get_name(self):
        if self.name is not None:
            return self.name
        else:
            raise Exception(
                "The variable should be set, or the method should be overridden"
            )

    def get_model_definition(self):
        if self.model_definition is not None:
            return self.model_definition
        else:
            raise Exception(
                "The variable should be set, or the method should be overridden"
            )

    def get_model_parameter_labels(self):
        if self.model_parameter_labels is not None:
            return self.model_parameter_labels
        else:
            raise Exception(
                "The variable should be set, or the method should be overridden"
            )

    def get_model_variable_descriptions(self):
        if self.model_variable_descriptions is not None:
            return self.model_variable_descriptions
        else:
            raise Exception(
                "The variable should be set, or the method should be overridden"
            )

    def get_model_variable_units(self):
        if self.model_variable_units is not None:
            return self.model_variable_units
        else:
            raise Exception(
                "The variable should be set, or the method should be overridden"
            )

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
        used_arg_indices=None,
    ):

        input_arr, runtime_arr = parse_benchmark_result(
            benchmark_data_file, row_limit=row_limit, used_arg_indices=used_arg_indices
        )

        n_model_param = self.get_n_model_param()
        model_input_size = self.get_model_input_size()

        if False in [len(i) == model_input_size for i in input_arr]:
            raise Exception(
                "Number of arguments in data file does not match operation definition"
            )

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

    def plot_model_performance(self, param, data_file, output_file, row_limit=None, used_arg_indices=None):
        if self.get_model_input_size() == 0:
            plot_argumentless_operation(
                self, param[0], data_file, output_file, row_limit=row_limit, used_arg_indices=used_arg_indices
            )
        elif self.get_model_input_size() == 1:
            plot_single_input_operation(
                self, param, data_file, output_file, row_limit=row_limit, used_arg_indices=used_arg_indices
            )
