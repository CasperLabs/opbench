import time
import logging

import numpy as np
import progressbar

from opbench.fit import fit, fit_constant
from opbench.helper import parse_benchmark_result, round_up, multiple_replace
from opbench.plotting import (
    plot_single_input_operation,
    plot_argumentless_operation,
)


class Operation:
    def __init__(self):
        self.inputs = []
        self.model_definition = None
        self.model_parameter_labels = None
        self.model_variable_descriptions = None
        self.model_variable_units = None
        self.name = None

        self.latest_param = None

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

        if isinstance(benchmark_data_file, str):
            input_arr, runtime_arr = parse_benchmark_result(
                benchmark_data_file,
                row_limit=row_limit,
                used_arg_indices=used_arg_indices,
            )
        elif isinstance(benchmark_data_file, list):
            if len(benchmark_data_file) == 0:
                raise Exception("Received empty list")

            input_arr_ = []
            runtime_arr_ = []

            for path in benchmark_data_file:
                input_arr, runtime_arr = parse_benchmark_result(
                    path, row_limit=row_limit, used_arg_indices=used_arg_indices
                )
                input_arr_.append(input_arr)
                runtime_arr_.append(runtime_arr)

            input_arr = np.concatenate(input_arr_)
            runtime_arr = np.concatenate(runtime_arr_)
        else:
            raise Exception("Invalid argument")

        n_model_param = self.get_n_model_param()
        model_input_size = self.get_model_input_size()

        if False in [len(i) == model_input_size for i in input_arr]:
            raise Exception(
                "Number of arguments in data file does not match operation definition: %s"
                % (self.name)
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

        self.latest_param = param

        return param

    def plot_model_performance(
        self,
        param,
        data_file,
        output_file,
        row_limit=None,
        used_arg_indices=None,
        bench_label=None,
    ):
        if self.get_model_input_size() == 0:
            plot_argumentless_operation(
                self,
                param[0],
                data_file,
                output_file,
                row_limit=row_limit,
                used_arg_indices=used_arg_indices,
                bench_label=bench_label,
            )
        elif self.get_model_input_size() == 1:
            plot_single_input_operation(
                self,
                param,
                data_file,
                output_file,
                row_limit=row_limit,
                used_arg_indices=used_arg_indices,
                bench_label=bench_label,
            )
        else:
            logging.warning(
                "Plotting for models with input size > 1 has not been implemented yet, skipping: %s"
                % (self.name)
            )

    def output_model_surface(
        self,
        param,
        data_file,
        basename,
        row_limit=None,
        used_arg_indices=None,
        bench_label=None,
        resolution=100,
    ):

        input_arr, runtime_arr = parse_benchmark_result(
            data_file, row_limit=row_limit, used_arg_indices=used_arg_indices
        )
        tmp = np.hstack((input_arr, runtime_arr[:, np.newaxis]))

        input_arr = np.squeeze(input_arr)

        if input_arr.ndim not in [1, 2] or input_arr.size == 0:
            logging.debug(
                "Model surface output supported only for models of 1 or 2 variables, skipping"
            )
            return None
        # assert input_arr.ndim <= 2
        write_csv_file(basename + "_orig.csv", tmp)

        ndim = input_arr.ndim

        if ndim == 1:
            bboxes = [(input_arr.min(), input_arr.max())]
        else:
            bboxes = [
                (i, j) for i, j in zip(input_arr.min(axis=0), input_arr.max(axis=0))
            ]

        # for i in range(input_arr.ndim):

        model = self.get_runtime_model()

        axis_values = []
        for i in bboxes:
            axis_values.append(np.linspace(*i, resolution))

        mesh_out = np.meshgrid(*axis_values, indexing="ij")

        mesh = np.array([i.flatten() for i in mesh_out]).T

        # X = np.linspace(input_arr.min(), input_arr.max(), 1000)
        Y = model(param, mesh)

        out_arr = np.hstack((mesh, Y[:, np.newaxis]))

        first_row_labels = ["arg_%d" % i for i in range(ndim)]
        first_row_labels += ["val"]

        write_csv_file(basename + "_model.csv", out_arr, chunk_size=resolution)

    def get_gas_cost_expr(self, n_significant_figures=2):
        if self.latest_param is None:
            return None

        model_def = self.get_model_definition()
        left, expr = model_def.split("=")

        vars_ = left[left.find("(") + 1 : left.find(")")]
        vars_ = vars_.split(",")
        vars_ = [i.strip() for i in vars_]

        expr = expr.strip()

        replace_dict = {}

        for param, label in zip(self.latest_param, self.get_model_parameter_labels()):
            replace_dict[label] = "{:_}".format(round_up(param, n_significant_figures))

        for var, desc in zip(vars_, self.get_model_variable_descriptions()):
            replace_dict[var] = desc

        expr = multiple_replace(replace_dict, expr)

        return expr


def write_csv_file(
    output_file, output_arr, chunk_size=None,
):
    ndim = output_arr.shape[1] - 1
    first_row_labels = ["arg_%d" % i for i in range(ndim)]
    first_row_labels += ["val"]

    with open(output_file, "w") as ofile:
        ofile.write(",".join(first_row_labels))
        ofile.write("\n")

        if ndim == 1 or chunk_size is None:
            chunks = [output_arr]
        else:
            chunks = np.array_split(output_arr, chunk_size * (ndim - 1), axis=0)

        # import ipdb; ipdb.set_trace()
        for chunk in chunks:
            for row in chunk:
                ofile.write(",".join(["%.8e" % i for i in row.tolist()]))
                ofile.write("\n")
            ofile.write("\n")
            # ofile.write("%s"%(str(chunk)))
