opbench_batch_fit host-functions/host-functions-input.toml
opbench_round_results host-functions/host-functions-results.csv -s 2 -o host-functions/host-functions-results-rounded.csv

opbench_batch_fit wasm-opcodes/wasm-opcodes-input.toml
opbench_round_results wasm-opcodes/wasm-opcodes-results.csv -s 2 -o wasm-opcodes/wasm-opcodes-results-rounded.csv

mkdir -p results/
cp host-functions/host-functions-results-rounded.csv results/
cp wasm-opcodes/wasm-opcodes-results-rounded.csv results/
