# Docker — md5 benchmark

## Build
```bash
docker build -t dedup-md5 .
```

## Run
```bash
docker run --name dedup-md5-run dedup-md5
```

## Copy results out
```bash
docker cp dedup-md5-run:/app/. ./results/
```

## Cleanup
```bash
docker rm dedup-md5-run
```
