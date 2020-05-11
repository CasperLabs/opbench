import os
import logging

import numpy as np

from operation_benchmarking.helper import parse_benchmark_result
# from operation_benchmarking.operations.host_functions import *
from operation_benchmarking.operations import wasm_opcodes as opcode_module
from operation_benchmarking.operation import Operation

import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)


DEGREE_OF_CONFIDENCE = 0.99
ROW_LIMIT = 10_000
DATA_DIR = "opcode-metrics"
PLOT_DIR = "out"
OUTPUT_PATH = "opcode-results.csv"
SKIPPED_PATH = "skipped.txt"

operations = []
for i in vars(opcode_module).values():
    if not isinstance(i, type):
        continue

    try:
        i().get_name()
    except:
        continue

    if issubclass(i, Operation):
        operations.append(i())

# import ipdb; ipdb.set_trace()

if not os.path.exists(PLOT_DIR):
    os.makedirs(PLOT_DIR)

max_param = max([op.get_n_model_param() for op in operations])

skipped_ofile = open(SKIPPED_PATH, "w")

ofile = open(OUTPUT_PATH, "w")
ofile.write("Name,Model,")
ofile.write(
    ",".join(
        ["Param_%d_label,Param_%d_value" % (i + 1, i + 1) for i in range(max_param)]
    )
)
ofile.write("\n")

for op in operations:
    logging.info("Fitting model for operation: " + op.get_name())
    data_file_name = op.get_name() + ".csv"
    data_file_path = os.path.join(DATA_DIR, data_file_name)
    plot_path = os.path.join(PLOT_DIR, op.get_name() + ".jpg")

    if not os.path.exists(data_file_path):
        logging.warning("Benchmark data file for %s does not exist in directory %s, skipping"%(op.get_name(), DATA_DIR))
        skipped_ofile.write("%s\n"%(op.get_name()))
        continue

    n_param = op.get_n_model_param()
    bounds = [[0 for i in range(n_param)], [np.inf for i in range(n_param)]]

    op_param = op.fit_parameters(
        data_file_path, DEGREE_OF_CONFIDENCE, row_limit=ROW_LIMIT, bounds=bounds, ignore_input_mismatch=True,
    )

    op.plot_model_performance(
        op_param, data_file_path, plot_path, row_limit=ROW_LIMIT,
    )

    ofile.write('"%s","%s",' % (op.get_name(), op.get_model_definition()))
    labels = op.get_model_parameter_labels()
    ofile.write(",".join(['"%s",%.6e' % (i, j) for i, j in zip(labels, op_param)]))
    ofile.write("\n")
    ofile.flush()

    # input_arr, runtime_arr = parse_benchmark_result(data_file_path, row_limit=ROW_LIMIT)
    # plt.figure()
    # plt.scatter(input_arr[:,0], runtime_arr, marker='x')
    # plt.grid()
    # # plt.hist(runtime_arr)
    # plt.show()
