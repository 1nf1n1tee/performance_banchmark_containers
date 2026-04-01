# Podman — sha256 benchmark

## Build
```bash
podman build -t dedup-sha256 -f Containerfile .
```

## Run
```bash
podman run --name dedup-sha256-run dedup-sha256
```

## Copy results out
```bash
podman cp dedup-sha256-run:/app/. ./results/
```

## Cleanup
```bash
podman rm dedup-sha256-run
```
