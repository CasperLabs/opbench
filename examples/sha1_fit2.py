from operation_costing.operations import diophantine
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, fmin
import numpy as np

THRESHOLD = 1.


df = pd.read_csv("data_sha1.csv")

timevar_list = df["time_vars"].to_list()

timevar_list = [eval(i) for i in timevar_list]

n_timevars = len(timevar_list[0])

timevar_keys = []


for i in range(n_timevars):
    new_col = [j[i] for j in timevar_list]
    key = "time_var_%d"%i

    timevar_keys.append(key)

    df[key] = pd.DataFrame(new_col)


df["mean_time"] = df["elapsed_time"]/df["n_exec"]


def positive_part(x):
    return np.array([max(i, 0.) for i in x])

def negative_part(x):
    return np.array([max(-i, 0.) for i in x])

def g(x, return_params=False):
    coeff = x[0]

    def f(x):
        m, n = x

        residual = m*df["time_var_0"]+n-df["mean_time"]

        pos = positive_part(residual)
        neg = negative_part(residual)

        result = pos - coeff*neg
        return result

    result = least_squares(f, [1,1])
    m, n = result.x

    if return_params:
        return (m, n)

    above = 0
    below = 0
    for i, j in zip(df["time_var_0"], df["mean_time"]):
        if i*m + n >= j:
            below += 1
        else:
            above += 1

    ratio = below/(above+below)

    objective = abs(ratio-THRESHOLD)
    print(objective)

    return objective

result = fmin(g, [1])

m, n = g(result, return_params=True)

X = np.linspace(df["time_var_0"].min(), df["time_var_0"].max(), 1000)
Y = m*X + n

x_below = []
x_above = []
y_below = []
y_above = []



for i, j in zip(df["time_var_0"], df["mean_time"]):
    if i*m + n >= j:
        x_below.append(i)
        y_below.append(j)
    else:
        x_above.append(i)
        y_above.append(j)

ratio = len(x_below)/(len(x_above)+len(x_below))



plt.scatter(x_below, y_below, color="green", marker="x")
plt.scatter(x_above, y_above, color="blue", marker="x")
plt.plot(X, Y, color="red", label="Fit m*x+n -> m = %.3g n = %.3g"%(m, n))

plt.title("SHA1 implemented in pure Python\n\
Points above: %d, Points below: %d, Percent below: %.1f%%"%(len(x_above), len(x_below), ratio*100))
plt.xlabel("Input size [byte]")
plt.ylabel("Runtime [second]")

plt.grid()
plt.legend()
plt.savefig("sha1_fit.jpg", dpi=150)
# plt.show()

