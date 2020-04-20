import pandas as pd
import numpy as np


def parse_benchmark_result(csv_file_path):
    df = pd.read_csv(csv_file_path)
    input_arr = df["args"].to_list()
    input_arr = [eval(i) for i in input_arr]
    input_arr = np.array(input_arr)

    runtime_arr = (df["total_elapsed_time"] / df["n_exec"]).to_numpy()

    if input_arr.dtype is not np.float64:
        input_arr = input_arr.astype(np.float64)

    if runtime_arr.dtype is not np.float64:
        runtime_arr = runtime_arr.astype(np.float64)

    return input_arr, runtime_arr
