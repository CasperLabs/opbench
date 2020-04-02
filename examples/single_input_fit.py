import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, fmin, fsolve
import numpy as np

DEGREE_OF_CONFIDENCE = 0.98

# OPERATION_NAME = "SHA1"
# DATA_FILE = "data_sha1.csv"
# MODEL_STR = "y = m*x + n"
# PARAM_STR = ["m", "n"]
# X_LABEL = "Input size [byte]"
# X0 = [1, 1]
# def MODEL(param, x):
#     return param[0]*x + param[1]

OPERATION_NAME = "Selection sort"
DATA_FILE = "data_selection_sort.csv"
MODEL_STR = "y = a*x^2 + b*x + c"
PARAM_STR = ["a", "b", "c"]
X_LABEL = "Number of elements"
X0 = [1, 1, 1]
def MODEL(param, x):
    return param[0] * x ** 2 + param[1] * x + param[2]


# OPERATION_NAME = "Selection sort"
# DATA_FILE = "data_selection_sort.csv"
# MODEL_STR = "y = a*x + b"
# PARAM_STR = ["a", "b"]
# X_LABEL = "Number of elements"
# X0 = [1, 1]
# def MODEL(param, x):
#     return param[0]*x + param[1]


# OPERATION_NAME = "Selection sort"
# DATA_FILE = "data_selection_sort.csv"
# MODEL_STR = "y = a*x^2 + b"
# PARAM_STR = ["a", "b"]
# X_LABEL = "Number of elements"
# X0 = [1, 1]
# def MODEL(param, x):
#     return param[0]*x**2 + param[1]


df = pd.read_csv(DATA_FILE)
timevar_list = df["time_vars"].to_list()
timevar_list = [eval(i) for i in timevar_list]
n_timevars = len(timevar_list[0])
timevar_keys = []

for i in range(n_timevars):
    new_col = [j[i] for j in timevar_list]
    key = "time_var_%d" % i

    timevar_keys.append(key)

    df[key] = pd.DataFrame(new_col)


df["mean_time"] = df["elapsed_time"] / df["n_exec"]



def g(x, return_params=False):
    coeff = x[0]

    def f(param):
        estimate = np.array([MODEL(param, i) for i in df["time_var_0"]])

        residual = estimate - df["mean_time"]

        pos = positive_part(residual)
        neg = negative_part(residual)

        result = pos - coeff * neg
        return result

    result = least_squares(f, X0)
    param = result.x

    if return_params:
        return param

    above = 0
    below = 0
    for i, j in zip(df["time_var_0"], df["mean_time"]):
        if MODEL(param, i) >= j:
            below += 1
        else:
            above += 1

    ratio = below / (above + below)

    # objective = abs(ratio-DEGREE_OF_CONFIDENCE)
    objective = ratio - DEGREE_OF_CONFIDENCE

    print(objective)

    return objective


# result = fmin(g, [1])
result = fsolve(g, [1])

param = g(result, return_params=True)

X = np.linspace(df["time_var_0"].min(), df["time_var_0"].max(), 1000)
Y = np.array([MODEL(param, i) for i in X])

x_below = []
x_above = []
y_below = []
y_above = []


for i, j in zip(df["time_var_0"], df["mean_time"]):
    if MODEL(param, i) >= j:
        x_below.append(i)
        y_below.append(j)
    else:
        x_above.append(i)
        y_above.append(j)

ratio = len(x_below) / (len(x_above) + len(x_below))

plt.scatter(x_below, y_below, color="green", marker="x")
plt.scatter(x_above, y_above, color="blue", marker="x")

fit_label = "Fit " + MODEL_STR + " -> "
fit_label += " ".join(["%s = %.3g" % (i, j) for i, j in zip(PARAM_STR, param)])

plt.plot(X, Y, color="red", label=fit_label)

plt.title(
    "%s implemented in pure Python\n\
Points above: %d, Points below: %d, \n\
Targeted DoC: %.1f%% Resulting DoC: %.1f%%"
    % (OPERATION_NAME, len(x_above), len(x_below), DEGREE_OF_CONFIDENCE * 100, ratio * 100)
)
plt.xlabel(X_LABEL)
plt.ylabel("Runtime [second]")

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("fit.jpg", dpi=150)
# plt.show()
