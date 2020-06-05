mkdir -p results

opbench_batch_fit host-functions/host-functions-input.toml
cp host-functions/host-functions-fee-schedule.md results/

opbench_batch_fit wasm-opcodes/wasm-opcodes-input.toml
cp wasm-opcodes/wasm-opcodes-fee-schedule.md results/

