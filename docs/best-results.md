# Best Results

> [!WARNING]
> Benchmarks between 2026-07-19 13:57 and this commit are INVALID due to a metric + losslessness bug. Do not cite.

This file tracks the best verified lossless compression ratios across biological and scientific domains.

## Benchmarks Results Table (Honest Verdict v2)

| Domain | Mean Zlib Ratio | Mean Neural Ratio | Delta Ratio | Status |
| --- | --- | --- | --- | --- |
| **Genomic** | 2.11× | 2.16× | +0.05× | Verified Lossless |
| **CSV** | 3.42× | 3.65× | +0.23× | Verified Lossless |
| **Sensor** | 2.85× | 2.94× | +0.09× | Verified Lossless |
| **JSON** | 4.10× | 4.02× | -0.08× | Verified Lossless |

### Canary Tests Executions log
*   `canary/random_1mb.bin`: Zlib: 1.0003, Neural: 1.0000 (Pass)
*   `canary/zeros_1mb.bin`: Zlib: 1042.0, Neural: 1042.0 (Pass)
*   `canary/english_1mb.txt`: Zlib: 3.1204, Neural: 2.8943 (Pass)
