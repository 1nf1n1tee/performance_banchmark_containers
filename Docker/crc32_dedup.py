# crc32_dedup.py

import binascii
import time
from dedup_utils import benchmark_deduplication

start_ = time.time()

file_name = "entry_1mil"

def crc32_hash(data: bytes) -> str:
    return str(binascii.crc32(data) & 0xffffffff)

if __name__ == "__main__":
    benchmark_deduplication(
        file_path=(f"{file_name}.csv"),
        hash_func=crc32_hash,
        output_file="unique_crc32.csv",
        hash_name="CRC32"
    )

end_ = time.time()
print(f"Total Response Time:    {end_ - start_:.3f} sec")

with open(f"CRC32 Deduplication Report {file_name}.txt", 'a') as result:
    result.write(f"Total Response Time:    {end_ - start_:.3f} sec\n")