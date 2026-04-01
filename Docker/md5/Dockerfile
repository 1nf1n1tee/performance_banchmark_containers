FROM python:3.11-slim

WORKDIR /app

# Copy shared source code
COPY ../../shared/dedup_utils.py .
COPY ../../shared/md5_dedup.py .
COPY ../../shared/epoch_runner.py .

# Dataset — place entry_1mil.csv in this folder before building
COPY entry_1mil.csv .

RUN pip install --no-cache-dir psutil

CMD ["python3", "epoch_runner.py", "md5_dedup.py"]
