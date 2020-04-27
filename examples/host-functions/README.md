# Benchmarking and analysis of host functions on the CasperLabs blockchain

## Fitting

Benchmark results are obtained by running them in the [main repository](https://github.com/CasperLabs/CasperLabs/tree/d07ba181503b03f80c4c4f37270dbc35b84b1e2c/execution-engine/engine-tests/src/profiling#host-function-metrics). The results are then copied over to the current repository for further analysis.

This requires that the `operation_benchmarking` module is installed. If it's not already, follow the instructions on the [main README.md](../../README.md).

This assumes that the benchmark data comes in a zip file. Change to the project directory and unzip `host-function-metrics.zip`:

```
cd examples/host-functions/
unzip host-function-metrics.zip
```

Then, run

```
python fit_host_functions.py
```
