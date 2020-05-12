import pandas as pd
import numpy as np
import sys

import matplotlib.pyplot as plt

from operation_benchmarking.helper import parse_benchmark_result

input_arr, runtime_arr = parse_benchmark_result(sys.argv[1])

indices_0 = [i for i in range(input_arr.shape[0]) if input_arr[i, 1] == 0]
indices_1 = [i for i in range(input_arr.shape[0]) if input_arr[i, 1] == 1]

# import ipdb; ipdb.set_trace()

plt.scatter(
    input_arr[indices_0, 0],
    runtime_arr[indices_0],
    marker="x",
    color="red",
    label="index = 0",
)
plt.scatter(
    input_arr[indices_1, 0],
    runtime_arr[indices_1],
    marker="x",
    color="blue",
    label="index = 1",
)

plt.xlabel("dest_size [byte]")
plt.ylabel("runtime [picosecond]")

plt.grid()
plt.legend()

plt.show()
