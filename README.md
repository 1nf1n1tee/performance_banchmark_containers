# Performance Benchmark — Containers

Benchmarks MD5, SHA-256, and CRC32 deduplication across three container runtimes: **Docker**, **Podman**, and **LXC**.

## Repository structure

```
performance_benchmark_containers/
│
├── shared/                     # Single source of truth — all Python code lives here
│   ├── dedup_utils.py          # Core benchmarking engine (metrics, reporting)
│   ├── md5_dedup.py            # MD5 deduplication script
│   ├── sha256_dedup.py         # SHA-256 deduplication script
│   ├── crc32_dedup.py          # CRC32 deduplication script
│   └── epoch_runner.py         # Runs any dedup script 10 times
│
├── Docker/
│   ├── md5/Dockerfile          # Docker image for MD5
│   ├── sha256/Dockerfile       # Docker image for SHA-256
│   └── crc32/Dockerfile        # Docker image for CRC32
│
├── Podman/
│   ├── md5/Containerfile       # Podman image for MD5
│   ├── sha256/Containerfile    # Podman image for SHA-256
│   └── crc32/Containerfile     # Podman image for CRC32
│
├── Lxc/
│   └── README.md               # LXC setup and run instructions
│
└── Datasets_used/
    ├── generate_synthetic_data.py
    └── README.md               # Dataset source and generation guide
```

## Quick start

### 1. Get the dataset
Place `entry_1mil.csv` in each algorithm folder before building (e.g. `Docker/md5/`), or see `Datasets_used/README.md`.

### 2. Docker
```bash
cd Docker/md5
docker build -t dedup-md5 .
docker run --name dedup-md5-run dedup-md5
docker cp dedup-md5-run:/app/. ./results/
docker rm dedup-md5-run
```
Repeat for `sha256/` and `crc32/`.

### 3. Podman
```bash
cd Podman/sha256
podman build -t dedup-sha256 -f Containerfile .
podman run --name dedup-sha256-run dedup-sha256
podman cp dedup-sha256-run:/app/. ./results/
podman rm dedup-sha256-run
```

### 4. LXC
See `Lxc/README.md` — scripts from `shared/` are run directly inside the container.

## Metrics reported
Each run outputs a `.txt` report with: total/unique/duplicate records, deduplication ratio, collision count & rate, memory usage (MB), CPU time (sec), and throughput (lines/sec).
