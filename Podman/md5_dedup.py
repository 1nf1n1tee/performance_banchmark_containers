# md5_dedup.py

import hashlib
import time
from dedup_utils import benchmark_deduplication

start_ = time.time()

file_name = "entry_1mil"

def md5_hash(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

if __name__ == "__main__":
    benchmark_deduplication(
        file_path=(f"{file_name}.csv"),
        hash_func=md5_hash,
        output_file="unique_md5.csv",
        hash_name="MD5"
    )

end_ = time.time()
print(f"Total Response Time:    {end_ - start_:.3f} sec")

with open(f"MD5 Deduplication Report {file_name}.txt", 'a') as result:
    result.write(f"Total Response Time:    {end_ - start_:.3f} sec\n")