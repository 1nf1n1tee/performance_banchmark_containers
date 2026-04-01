# LXC benchmark

LXC containers share the host filesystem, so no image build step is needed.
Copy the `shared/` scripts and your dataset into the container, then run.

## Setup (as root on host)
```bash
lxc-start --name <container_name>
lxc-attach --name <container_name>
```

## Inside the container
```bash
cd /path/to/shared
pip install psutil

# Run a single algorithm (10 epochs)
python3 epoch_runner.py md5_dedup.py
python3 epoch_runner.py sha256_dedup.py
python3 epoch_runner.py crc32_dedup.py
```

## Teardown (as root on host)
```bash
lxc-stop --name <container_name>
exit
```
