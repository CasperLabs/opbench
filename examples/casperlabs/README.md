# Generating the Highway Fee Schedule

This requires that the `opbench` module is installed. If it's not already, follow the instructions on the [main README.md](../../README.md).


## Host functions

Benchmarks are run in the [main repository](https://github.com/CasperLabs/CasperLabs/tree/d07ba181503b03f80c4c4f37270dbc35b84b1e2c/execution-engine/engine-tests/src/profiling#host-function-metrics). The results are then copied over to the current repository for analysis.

## WASM Opcodes

CasperLabs uses Parity's [wasmi](https://github.com/paritytech/wasmi/), and the opcodes are implemented in [isa.rs](https://github.com/paritytech/wasmi/blob/1d580e308dc549cf8056166722ac93e7b73f858c/src/isa.rs#L140-L341).

Opcode instrumentation has been implemented in [this PR](https://github.com/CasperLabs/wasmi/pull/1).

## Running the Analysis

Most recent benchmarks are covered by the ticket OP-1366. Once you make sure that the result zip file `OP-1366.zip` is in the current directory, run

```
bash copy-OP-1366-results.csv
```

This will copy over the benchmark data files to their respective directories.

Then, perform the analysis by simply running

```
bash run-analysis.sh
```

Once the analysis completes, the final fee schedules are copied over to `results/`. Plots and other output files are not copied over. They can be found in `host-functions/` and `wasm-opcodes/` for debugging purposes.
