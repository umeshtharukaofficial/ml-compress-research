# AGENTS.md

This file defines the roles and responsibilities for each of the 20 bot agents participating in this project.

## Bot Matrix & Specifications

### Bot 01: `bot-literature`
- **Role**: Literature scraper. Scrapes arXiv, bioRxiv, GitHub for new compression + AMR papers.
- **Output**: Writes to `docs/literature.md`.
- **Interval**: Runs every 6 hours.

### Bot 02: `bot-dataset`
- **Role**: Dataset downloader & versioner. Downloads & versions public FASTQ / sensor / CSV samples.
- **Output**: Updates dataset references / pointers.
- **Interval**: Runs every 12 hours.

### Bot 03: `bot-baseline`
- **Role**: Baselines benchmark runner. Runs GZIP, ZSTD, Brotli, Parquet + Snappy on active datasets.
- **Output**: Logs baseline results.
- **Interval**: Runs every 24 hours.

### Bot 04: `bot-tokenizer`
- **Role**: Tokenizer exporter. Exports byte-level + domain BPE tokenizers and vocabulary mappings.
- **Interval**: On demand.

### Bot 05: `bot-rnn`
- **Role**: RNN Model trainer. Trains tiny GRU next-byte predictors.
- **Interval**: 5 min heartbeat.

### Bot 06: `bot-transformer`
- **Role**: Transformer Model trainer. Trains 2-layer 128-dim transformer predictors.
- **Interval**: 5 min heartbeat.

### Bot 07: `bot-rwkv`
- **Role**: RWKV Model trainer. Trains tiny RWKV predictors.
- **Interval**: 5 min heartbeat.

### Bot 08: `bot-ssm`
- **Role**: SSM/Mamba Model trainer. Trains tiny SSM predictors.
- **Interval**: 5 min heartbeat.

### Bot 09: `bot-arith-coder`
- **Role**: Arithmetic coder implementation (Python & Rust).
- **Interval**: On demand.

### Bot 10: `bot-range-coder`
- **Role**: Range coder / rANS implementation.
- **Interval**: On demand.

### Bot 11: `bot-quant`
- **Role**: Model Quantizer. Quantizes models to INT8 / INT4.
- **Interval**: After each new model train.

### Bot 12: `bot-onnx`
- **Role**: ONNX Exporter. Exports PyTorch models to ONNX.
- **Interval**: After quantization.

### Bot 13: `bot-runtime`
- **Role**: Fast inference runtime. Highly optimized Rust/C++ inference kernel with SIMD & zero-alloc.
- **Interval**: Weekly.

### Bot 14: `bot-bench`
- **Role**: Full benchmark executor. Assesses compression ratio, speed, RAM, model size.
- **Interval**: Nightly.

### Bot 15: `bot-genomic`
- **Role**: Genomic domain expert tuner.
- **Interval**: Daily.

### Bot 16: `bot-sensor`
- **Role**: IoT sensor domain expert tuner.
- **Interval**: Daily.

### Bot 17: `bot-csv`
- **Role**: Scientific CSV domain expert tuner.
- **Interval**: Daily.

### Bot 18: `bot-paper`
- **Role**: LaTeX Paper Draft writer.
- **Interval**: Daily.

### Bot 19: `bot-blog`
- **Role**: Blog post writer (Medium / LinkedIn draft format).
- **Interval**: Weekly.

### Bot 20: `bot-orchestrator`
- **Role**: Master Orchestrator. Coordinates the work of Bots 01-19, plans next experiments, updates daily progress logs, and handles heartbeats.
- **Interval**: Runs every 5 minutes.
