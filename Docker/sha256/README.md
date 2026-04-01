# Docker — sha256 benchmark

## Build
```bash
docker build -t dedup-sha256 .
```

## Run
```bash
docker run --name dedup-sha256-run dedup-sha256
```

## Copy results out
```bash
docker cp dedup-sha256-run:/app/. ./results/
```

## Cleanup
```bash
docker rm dedup-sha256-run
```
