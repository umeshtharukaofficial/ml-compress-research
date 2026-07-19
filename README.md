# ml-compress-research

Scientific datasets neural compression research using small pre-trained predictors.

## Target Metric Goals

| Metric | Baseline (ZSTD-19) | Our target |
| --- | --- | --- |
| Compression ratio | 1.0× | ≥ 1.4× better on domain data |
| Compress speed | 1.0× | ≥ same or faster on CPU |
| Decompress speed | 1.0× | ≥ 0.8× (acceptable) |
| RAM at runtime | 1.0× | ≤ 2× (must stay < 200 MB) |
| Model size | — | ≤ 5 MB quantized |

## 20-Bot Matrix

| Bot ID | Bot name | Owns |
| --- | --- | --- |
| 01 | `bot-literature` | Scrapes literature & papers |
| 02 | `bot-dataset` | Datasets collection |
| 03 | `bot-baseline` | Benchmarks baselines |
| 04 | `bot-tokenizer` | Domain tokenizers |
| 05 | `bot-rnn` | GRU Predictor |
| 06 | `bot-transformer` | Transformer Predictor |
| 07 | `bot-rwkv` | RWKV Predictor |
| 08 | `bot-ssm` | SSM/Mamba Predictor |
| 09 | `bot-arith-coder` | Arithmetic Coding |
| 10 | `bot-range-coder` | Range Coding |
| 11 | `bot-quant` | Model quantization |
| 12 | `bot-onnx` | ONNX pipeline |
| 13 | `bot-runtime` | C++/Rust inference kernels |
| 14 | `bot-bench` | Benchmarking system |
| 15 | `bot-genomic` | Genomic domain tuning |
| 16 | `bot-sensor` | IoT sensor tuning |
| 17 | `bot-csv` | CSV domain tuning |
| 18 | `bot-paper` | LaTeX paper generation |
| 19 | `bot-blog` | Blog generator |
| 20 | `bot-orchestrator` | Orchestrator of the multi-agent system |






























## Daily Update Summary
*   **Last Daily Run**: 2026-07-19 12:44:41 UTC
*   **Status**: Multi-scale datasets successfully generated & evaluated. RNN Markov trained on multiple variants.
**Latest Performance Stats (Conventional Baseline):**
* 2026-07-19 12:44:41,README.md,4754,2194,2.1668,0.2689
* 2026-07-19 12:44:41,LICENSE,6866,2760,2.4877,0.253
* 2026-07-19 12:44:41,requirements.txt,86,83,1.0361,0.0398

