# Host functions

Benchmarks are run in the [main repository](https://github.com/CasperLabs/CasperLabs/tree/d07ba181503b03f80c4c4f37270dbc35b84b1e2c/execution-engine/engine-tests/src/profiling#host-function-metrics). The results are then copied over to the current repository for analysis.

This assumes that the benchmark data comes in a zip file. Change to the project directory and unzip `host-function-metrics.zip`:

```
cd examples/casperlabs/host-functions/
unzip host-function-metrics.zip
```

## Fitting

```
ob_batch_fit host-function-input.toml
```

This will generate plots in the `out` directory and also create parsable output in `host-function-results.csv`.
