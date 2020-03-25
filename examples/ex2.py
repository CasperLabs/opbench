from operation_pricing.operations import diophantine
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

df = pd.read_csv("test.csv")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

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

ax.scatter(df["time_var_0"]+df["time_var_1"], df["time_var_2"], df["mean_time"], marker="x")
plt.show()

import ipdb; ipdb.set_trace()
