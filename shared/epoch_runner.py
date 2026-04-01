# epoch_runner.py
# Generic runner — calls the given script 10 times (one epoch per run).
# Usage: python3 epoch_runner.py md5_dedup.py

import sys
from subprocess import call

def run_epochs(script, n=10):
    for _ in range(n):
        call(["python3", script])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 epoch_runner.py <script_name>")
        sys.exit(1)
    run_epochs(sys.argv[1])
