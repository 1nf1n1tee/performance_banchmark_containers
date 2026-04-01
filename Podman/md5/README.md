# Podman — md5 benchmark

## Build
```bash
podman build -t dedup-md5 -f Containerfile .
```

## Run
```bash
podman run --name dedup-md5-run dedup-md5
```

## Copy results out
```bash
podman cp dedup-md5-run:/app/. ./results/
```

## Cleanup
```bash
podman rm dedup-md5-run
```
