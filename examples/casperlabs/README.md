# Benchmarking and analysis of operations on the CasperLabs blockchain

This requires that the `operation_benchmarking` module is installed. If it's not already, follow the instructions on the [main README.md](../../README.md).


## Host functions

Benchmarks are run in the [main repository](https://github.com/CasperLabs/CasperLabs/tree/d07ba181503b03f80c4c4f37270dbc35b84b1e2c/execution-engine/engine-tests/src/profiling#host-function-metrics). The results are then copied over to the current repository for analysis.

This assumes that the benchmark data comes in a zip file. Change to the project directory and unzip `host-function-metrics.zip`:

```
cd examples/casperlabs/host-functions/
unzip host-function-metrics.zip
```

### Fitting

```
ob_batch_fit host-function-input.toml
ob_round_results host-function-results.csv -o host-function-results-rounded.csv
```

This will generate plots in the `out` directory and also create parsable output in `host-function-results.csv`.


## WASM Opcodes

CasperLabs uses Parity's [wasmi](https://github.com/paritytech/wasmi/), and the opcodes are implemented in [isa.rs](https://github.com/paritytech/wasmi/blob/1d580e308dc549cf8056166722ac93e7b73f858c/src/isa.rs#L140-L341).

Opcode instrumentation has been implemented in [this PR](https://github.com/CasperLabs/wasmi/pull/1).

Once the benchmarks are completed, results are copied over to the current directory:

```
cd examples/casperlabs/wasm-opcodes/
unzip opcode-metrics.zip
```

### Fitting

```
ob_batch_fit opcode-input.toml
ob_round_results opcode-results.csv -o opcode-results-rounded.csv
```

