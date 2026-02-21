# dedup_utils.py

import os
import psutil
import time
import math

def benchmark_deduplication(file_path, hash_func, output_file, hash_name):

    # if(hash_name == "SHA-256"):
    #     hashkey_size = 256
    # elif(hash_name == "MD5"):
    #     hashkey_size = 128
    # else:
    #     hashkey_size = 32

    start = time.process_time()
    start_time = time.time()
    process = psutil.Process(os.getpid())
    # io_start = process.io_counters()

    # seen = set()
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
                if(hash_map[h] != line):
                    collision += 1
            else:
                hash_map[h] = line
                unique_lines.append(line)

    # def collision_probability(n, m):
    #     H = 2 ** m  # total hash space

    #     # exact probability of no collision
    #     p_no_collision = math.exp(-(n * (n - 1)) / (2 * H))

    #     return (1 - p_no_collision) * 100
    
    with open(output_file, 'wb') as out:
        out.writelines(unique_lines)

    end_time = time.time()
    end = time.process_time()
    # io_end = process.io_counters()

    mem_usage = process.memory_info().rss / (1024 * 1024)  # in MB
    # cpu_time = time.process_time()
    cpu_time = end - start
    lines_per_sec = total_lines / (end_time - start_time)
    dedup_ratio = (total_lines - len(unique_lines)) / total_lines * 100
    # prob_of_collision = collision_probability(total_lines, hashkey_size)

    # read_bytes = io_end.read_bytes - io_start.read_bytes
    # write_bytes = io_end.write_bytes - io_start.write_bytes
    # read_count = io_end.read_count - io_start.read_count
    # write_count = io_end.write_count - io_start.write_count
    # if():
    #   

    print(f"\n {hash_name} Deduplication Report")
    print("-" * 45)
    print(f"Total records:          {total_lines}")
    print(f"Unique records:         {len(unique_lines)}")
    print(f"Duplicate records:      {len(duplicates)}")
    print(f"Deduplication ratio:    {dedup_ratio:.2f}%")
    # print(f"Prob. of collision:     {prob_of_collision:.8f}%")
    # print(f"Time taken:             {end_time - start_time:.3f} sec")
    print(f"Number of Collision:    {collision}")
    print(f"Collision rate:         {collision/total_lines}")
    print(f"Memory used:            {mem_usage:.2f} MB")
    print(f"CPU time used:          {cpu_time:.3f} sec")
    print(f"Throughput:             {lines_per_sec:.2f} lines/sec")

    # print(f"\n I/O Performance:")
    # print(f"Disk reads:             {read_count} times")
    # print(f"Disk writes:            {write_count} times")
    # print(f"Bytes read:             {read_bytes / 1024:.2f} KB")
    # print(f"Bytes written:          {write_bytes / 1024:.2f} KB")

    with open(f"{hash_name} Deduplication Report {file_path[:-4]}.txt", 'a') as result:
        result.write(f"\n{hash_name} Deduplication Report\n")
        result.write("-" * 45)
        result.write("\n")
        result.write(f"Total records:          {total_lines}\n")
        result.write(f"Unique records:         {len(unique_lines)}\n")
        result.write(f"Duplicate records:      {len(duplicates)}\n")
        result.write(f"Deduplication ratio:    {dedup_ratio:.2f}%\n")
        # result.write(f"Prob. of collision:     {prob_of_collision:.8f}%\n")
        result.write(f"Number of Collision:    {collision}\n")
        result.write(f"Collision rate:         {collision/total_lines:.8f}\n")
        result.write(f"Memory used:            {mem_usage:.2f} MB\n")
        result.write(f"CPU time used:          {cpu_time:.4f} sec\n")
        result.write(f"Throughput:             {lines_per_sec:.2f} lines/sec\n")
