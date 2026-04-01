# Podman — crc32 benchmark

## Build
```bash
podman build -t dedup-crc32 -f Containerfile .
```

## Run
```bash
podman run --name dedup-crc32-run dedup-crc32
```

## Copy results out
```bash
podman cp dedup-crc32-run:/app/. ./results/
```

## Cleanup
```bash
podman rm dedup-crc32-run
```
