import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, fmin, fsolve
import numpy as np
from operation_benchmarking.helper import parse_benchmark_result

from operation_benchmarking.config import TIME_UNIT


def plot_single_input_operation(
    operation, param, data_file, output_file, row_limit=None, used_arg_indices=None
):

    assert operation.get_model_input_size() == 1

    input_arr, runtime_arr = parse_benchmark_result(data_file, row_limit=row_limit, used_arg_indices=used_arg_indices)

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

    fit_label = "Fit " + operation.get_model_definition() + " -> "
    fit_label += " ".join(
        [
            "%s = %.3g" % (i, j)
            for i, j in zip(operation.get_model_parameter_labels(), param)
        ]
    )

    plt.plot(X, Y, color="red", label=fit_label)

    plt.title(
        "Operation: %s \n\
    Points above: %d, Points below: %d, DoC: %.1f%%"
        % (operation.get_name(), len(x_above), len(x_below), ratio * 100,)
    )
    plt.xlabel(
        operation.get_model_variable_descriptions()[0]
        + " ["
        + operation.get_model_variable_units()[0]
        + "]"
    )
    plt.ylabel("Runtime [%s]" % TIME_UNIT)

    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    # plt.show()


def plot_argumentless_operation(
    operation, constant, data_file, output_file, row_limit=None, used_arg_indices=None
):

    assert operation.get_model_input_size() == 0

    input_arr, runtime_arr = parse_benchmark_result(data_file, row_limit=row_limit, used_arg_indices=used_arg_indices)

    mean = np.mean(runtime_arr)
    std = np.std(runtime_arr)

    y_left = []
    y_right = []

    for i in zip(runtime_arr):
        if constant >= i:
            y_left.append(i)
        else:
            y_right.append(i)

    ratio = len(y_left) / (len(y_right) + len(y_left))

    fig = plt.figure()
    plt.grid()

    plt.hist(runtime_arr, bins=64, range=(mean - 4 * std, mean + 4 * std), ec="k")

    plt.axvline(constant, color="r", linewidth=2, label="Threshold = %.4g" % constant)

    plt.title(
        "Operation: %s \n\
    Points left: %d, Points right: %d, DoC: %.1f%%"
        % (operation.get_name(), len(y_left), len(y_right), ratio * 100,)
    )
    plt.xlabel("Runtime [%s]" % TIME_UNIT)
    plt.ylabel("Number of points")

    plt.xlim([max(0, mean - 4 * std), max(mean + 4 * std, constant)])

    tick_vals = [
        mean - 3 * std,
        mean - 2 * std,
        mean - std,
        mean,
        mean + std,
        mean + 2 * std,
        mean + 3 * std,
    ]

    tick_labels = [
        "%.2g\n$\mu-3\sigma$" % tick_vals[0],
        "%.2g\n$\mu-2\sigma$" % tick_vals[1],
        "%.2g\n$\mu-\sigma$" % tick_vals[2],
        "%.2g\n$\mu$" % tick_vals[3],
        "%.2g\n$\mu+\sigma$" % tick_vals[4],
        "%.2g\n$\mu+2\sigma$" % tick_vals[5],
        "%.2g\n$\mu+3\sigma$" % tick_vals[6],
    ]

    negative = False
    while True:
        if len(tick_vals) == 0:
            break
        if tick_vals[0] > 0:
            break
        tick_vals.pop(0)
        tick_labels.pop(0)
        negative = True

    if negative:
        tick_vals.insert(0, 0)
        tick_labels.insert(0, "0")

    plt.xticks(
        tick_vals, tick_labels,
    )

    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)

    plt.close()
