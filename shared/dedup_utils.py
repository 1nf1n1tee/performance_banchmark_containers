# dedup_utils.py

import os
import psutil
import time


def benchmark_deduplication(file_path, hash_func, output_file, hash_name):

    start = time.process_time()
    start_time = time.time()
    process = psutil.Process(os.getpid())

    duplicates = []
    unique_lines = []
    hash_map = {}

    total_lines = 0
    collision = 0

    with open(file_path, 'rb') as f:
        lines = f.readlines()[1:]
        for line in lines:
            total_lines += 1
            h = hash_func(line)
            if h in hash_map.keys():
                duplicates.append(line)
                if hash_map[h] != line:
                    collision += 1
            else:
                hash_map[h] = line
                unique_lines.append(line)

    with open(output_file, 'wb') as out:
        out.writelines(unique_lines)

    end_time = time.time()
    end = time.process_time()

    mem_usage = process.memory_info().rss / (1024 * 1024)  # in MB
    cpu_time = end - start
    lines_per_sec = total_lines / (end_time - start_time)
    dedup_ratio = (total_lines - len(unique_lines)) / total_lines * 100

    print(f"\n {hash_name} Deduplication Report")
    print("-" * 45)
    print(f"Total records:          {total_lines}")
    print(f"Unique records:         {len(unique_lines)}")
    print(f"Duplicate records:      {len(duplicates)}")
    print(f"Deduplication ratio:    {dedup_ratio:.2f}%")
    print(f"Number of Collision:    {collision}")
    print(f"Collision rate:         {collision / total_lines}")
    print(f"Memory used:            {mem_usage:.2f} MB")
    print(f"CPU time used:          {cpu_time:.3f} sec")
    print(f"Throughput:             {lines_per_sec:.2f} lines/sec")

    with open(f"{hash_name} Deduplication Report {file_path[:-4]}.txt", 'a') as result:
        result.write(f"\n{hash_name} Deduplication Report\n")
        result.write("-" * 45 + "\n")
        result.write(f"Total records:          {total_lines}\n")
        result.write(f"Unique records:         {len(unique_lines)}\n")
        result.write(f"Duplicate records:      {len(duplicates)}\n")
        result.write(f"Deduplication ratio:    {dedup_ratio:.2f}%\n")
        result.write(f"Number of Collision:    {collision}\n")
        result.write(f"Collision rate:         {collision / total_lines:.8f}\n")
        result.write(f"Memory used:            {mem_usage:.2f} MB\n")
        result.write(f"CPU time used:          {cpu_time:.4f} sec\n")
        result.write(f"Throughput:             {lines_per_sec:.2f} lines/sec\n")
