from operation_benchmarking.operations import *
from operation_benchmarking.plotting import plot_single_input_operation
import logging

logging.basicConfig(level=logging.INFO)

sha1 = SHA1HashOperation()
sha1_param = sha1.fit_parameters("data_sha1.csv", 0.98)
plot_single_input_operation(
    sha1,
    "data_sha1.csv",
    sha1_param,
    "data_sha1.jpg",
    "SHA1",
    "y = m*x + n",
    ["m", "n"],
    "Input size [byte]",
)

selection_sort = SelectionSortOperation()
selection_sort_param = selection_sort.fit_parameters("data_selection_sort.csv", 0.98)
plot_single_input_operation(
    selection_sort,
    "data_selection_sort.csv",
    selection_sort_param,
    "data_selection_sort.jpg",
    "Selection sort",
    "y = a*x^2 + b*x + c",
    ["a", "b", "c"],
    "Number of elements",
)
