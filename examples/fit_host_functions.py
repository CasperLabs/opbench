# from operation_benchmarking.operations import *
from operation_benchmarking.operations.host_functions import *
from operation_benchmarking.plotting import plot_argumentless_operation
import logging


import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

from operation_benchmarking.helper import parse_benchmark_result

# input_arr, runtime_arr = parse_benchmark_result("host-function-metrics/add_local.csv")
# plt.plot(input_arr[:,0], runtime_arr, 'o')
# plt.show()


# op1 = AddLocalOperation()
# op1_param = op1.fit_parameters(
#     "host-function-metrics/add_local.csv", 0.99, bounds=((0, 0), (np.inf, np.inf))
# )
# op1.plot_model_performance(
#     op1_param, "host-function-metrics/add_local.csv", "data_op1.jpg",
# )


op2 = CreatePurseOperation()
op2_param = op2.fit_parameters(
    "host-function-metrics/create_purse.csv",
    0.99,
    bounds=((0), (np.inf))
)
plot_argumentless_operation(
    op2, op2_param[0], "host-function-metrics/create_purse.csv", "data_create_purse.jpg",
)

import ipdb; ipdb.set_trace()

# plot_single_input_operation(
#     op2,
#     "host-function-metrics/add_local.csv",
#     op2_param,
#     "data_op2.jpg",
#     "SHA1",
#     "y = m*x + n",
#     ["m", "n"],
#     "Input size [byte]",
# )


# import ipdb; ipdb.set_trace()
