import time
import progressbar

import pandas as pd
import numpy as np

from scipy.optimize import least_squares, fmin, fsolve

from operation_benchmarking.fit import fit


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

    def get_model_input_size(self):
        raise Exception("This should be implemented")

    def get_runtime_model(self):
        raise Exception("This should be implemented")

    def batch_execute(self, n_executions, input_):
        for i in range(n_executions):
            self.execute(input_)

    def run_test(self, n_executions, opath):

        ofile = open(opath, "w")

        bar = progressbar.ProgressBar(max_value=len(self.inputs))

        ofile.write("time_vars,n_exec,elapsed_time\n")

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

    def fit_parameters(self, benchmark_data_file, degree_of_confidence):

        df = pd.read_csv(benchmark_data_file)
        input_arr = df["time_vars"].to_list()
        input_arr = [eval(i) for i in input_arr]

        n_model_param = self.get_n_model_param()
        model_input_size = self.get_model_input_size()

        assert False not in [len(i) == model_input_size for i in input_arr]

        input_arr = np.array(input_arr)

        runtime_arr = (df["elapsed_time"] / df["n_exec"]).to_numpy()

        param = fit(
            self.get_runtime_model(),
            model_input_size,
            n_model_param,
            input_arr,
            runtime_arr,
            degree_of_confidence,
        )

        return param
