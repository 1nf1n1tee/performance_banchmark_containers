# Docker — crc32 benchmark

## Build
```bash
docker build -t dedup-crc32 .
```

## Run
```bash
docker run --name dedup-crc32-run dedup-crc32
```

## Copy results out
```bash
docker cp dedup-crc32-run:/app/. ./results/
```

## Cleanup
```bash
docker rm dedup-crc32-run
```
