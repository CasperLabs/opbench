import pandas as pd
import numpy as np

import argparse

import matplotlib.pyplot as plt

from operation_benchmarking.helper import parse_benchmark_result

parser = argparse.ArgumentParser(
    description="Given a benchmark data file, plot runtime against a single argument"
)

parser.add_argument("csv_file")
parser.add_argument(
    "-i", "--index", type=int, required=True, help="Index of the arg, e.g. 0, 1, 2, ..."
)

args = parser.parse_args()

input_arr, runtime_arr = parse_benchmark_result(args.csv_file)

plt.scatter(input_arr[:, args.index], runtime_arr, marker="x")

plt.xlabel("arg at index %d" % args.index)
plt.ylabel("runtime [picosecond]")

plt.grid()

plt.show()
