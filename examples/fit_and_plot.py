from operation_benchmarking.operations import *
import logging

logging.basicConfig(level=logging.INFO)

sha1 = SHA1HashOperation()
sha1_param = sha1.fit_parameters("data_sha1.csv", 0.98)
sha1.plot_model_performance(
    sha1_param, "data_sha1.csv", "data_sha1.jpg",
)

selection_sort = SelectionSortOperation()
selection_sort_param = selection_sort.fit_parameters("data_selection_sort.csv", 0.98)
selection_sort.plot_model_performance(
    selection_sort_param, "data_selection_sort.csv", "data_selection_sort.jpg",
)
