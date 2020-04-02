import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, fmin, fsolve
import numpy as np
from operation_benchmarking.helper import parse_benchmark_result


def plot_single_input_operation(
    operation,
    data_file,
    param,
    output_file,
    operation_name,
    model_str,
    param_str,
    x_label,
):

    assert operation.get_model_input_size() == 1

    input_arr, runtime_arr = parse_benchmark_result(data_file)

    model = operation.get_runtime_model()

    model_runtime = model(param, input_arr)

    X = np.linspace(input_arr.min(), input_arr.max(), 1000)
    # Y = np.array([MODEL(param, i) for i in X])
    Y = model(param, X[:, np.newaxis])

    x_below = []
    x_above = []
    y_below = []
    y_above = []

    for i, j, k in zip(input_arr, model_runtime, runtime_arr):
        if j >= k:
            x_below.append(i)
            y_below.append(k)
        else:
            x_above.append(i)
            y_above.append(k)

    ratio = len(x_below) / (len(x_above) + len(x_below))

    plt.figure()

    plt.scatter(x_below, y_below, color="green", marker="x")
    plt.scatter(x_above, y_above, color="blue", marker="x")

    fit_label = "Fit " + model_str + " -> "
    fit_label += " ".join(["%s = %.3g" % (i, j) for i, j in zip(param_str, param)])

    plt.plot(X, Y, color="red", label=fit_label)

    plt.title(
        "%s implemented in pure Python\n\
    Points above: %d, Points below: %d, DoC: %.1f%%"
        % (operation_name, len(x_above), len(x_below), ratio * 100,)
    )
    plt.xlabel(x_label)
    plt.ylabel("Runtime [second]")

    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    # plt.show()
