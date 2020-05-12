# WASM Opcodes

CasperLabs uses Parity's [wasmi](https://github.com/paritytech/wasmi/), and the opcodes are implemented in [isa.rs](https://github.com/paritytech/wasmi/blob/1d580e308dc549cf8056166722ac93e7b73f858c/src/isa.rs#L140-L341).

Opcode instrumentation has been implemented in [this PR](https://github.com/CasperLabs/wasmi/pull/1).

Once the benchmarks are completed, results are copied over to the current directory:

```
cd examples/casperlabs/wasm-opcodes/
unzip opcode-metrics.zip
```

## Fitting

```
ob_batch_fit opcode-input.toml
```

