# operation_benchmarking

Proof of Concept for assigning runtime models to operations (opcodes, functions, etc.) in distributed networks.
See [Metering resource usage in blockchains](https://hackmd.io/@onur/metering_resource_usage).

## Install

Requirements: Python 3.5+, NumPy, SciPy, Cython.

```
sudo python setup.py install
```

## Run examples

```
cd examples/
python generate_inputs.py
python fit_and_plot.pt
```
