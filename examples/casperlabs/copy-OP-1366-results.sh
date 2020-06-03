unzip OP-1366.zip
cd OP-1366

tar zxvf host-function-metrics.tar.gz
mv host-function-metrics/ bench1/
cp -r bench1 ../host-functions/
rm -rf bench1

tar zxvf target_metrics_1thr.tar.gz
mv target/metrics bench_1thr
cp -r bench_1thr/ ../wasm-opcodes/
rm -rf target

tar zxvf target_metrics_2thr.tar.gz
mv target/metrics bench_2thr
cp -r bench_2thr/ ../wasm-opcodes/
rm -rf target

tar zxvf target_metrics_4thr.tar.gz
mv target/metrics bench_4thr
cp -r bench_4thr/ ../wasm-opcodes/
rm -rf target

tar zxvf target_metrics_8thr.tar.gz
mv target/metrics bench_8thr
cp -r bench_8thr/ ../wasm-opcodes/
rm -rf target

cd ../

rm OP-1366 -rf



