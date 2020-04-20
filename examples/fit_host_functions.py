import os
import logging

from operation_benchmarking.plotting import plot_argumentless_operation
from operation_benchmarking.helper import parse_benchmark_result
from operation_benchmarking.operations.host_functions import *

import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)


DEGREE_OF_CONFIDENCE = 0.99
DATA_DIR = "host-function-metrics"
PLOT_DIR = "out"


operations = [
    AddAssociatedKeyOperation(),
    AddOperation(),
    CreatePurseOperation(),
    GetArgSizeOperation(),
    GetBalanceOperation(),
    GetBlocktimeOperation(),
    GetCallerOperation(),
    GetMainPurseOperation(),
    GetPhaseOperation(),
    GetSystemContractOperation(),
    IsValidUrefOperation(),
    ReadValueOperation(),
    RemoveAssociatedKeyOperation(),
    RevertOperation(),
    SetActionThresholdOperation(),
    TransferFromPurseToAccountOperation(),
    TransferFromPurseToPurseOperation(),
    TransferToAccountOperation(),
    UpdateAssociatedKeyOperation(),
]

if not os.path.exists(PLOT_DIR):
    os.makedirs(PLOT_DIR)

# op1 = AddLocalOperation()
# op1_param = op1.fit_parameters(
#     "host-function-metrics/add_local.csv", 0.99, bounds=((0, 0), (np.inf, np.inf))
# )
# op1.plot_model_performance(
#     op1_param, "host-function-metrics/add_local.csv", "data_op1.jpg",
# )

for op in operations:
    logging.info("Fitting model for operation: " + op.get_name())
    data_file_path = os.path.join(DATA_DIR, op.get_name() + ".csv")
    plot_path = os.path.join(PLOT_DIR, op.get_name() + ".jpg")

    op_param = op.fit_parameters(
        data_file_path, DEGREE_OF_CONFIDENCE, bounds=((0), (np.inf))
    )

    op.plot_model_performance(
        op_param, data_file_path, plot_path,
    )

    # input_arr, runtime_arr = parse_benchmark_result(data_file_path)
    # plt.hist(runtime_arr)
    # plt.show()

import ipdb

ipdb.set_trace()
