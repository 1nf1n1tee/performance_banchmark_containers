podman build -t dedup-app -f container_file_name(example - crc_containerfile)
podman run --name anything(example - check) dedup-app
podman cp check:/app/file_name(example - "CRC32 Deduplication Report ign.csv.txt") /home/al-is-working/Desktop/Podman_results/run_data
podman rm name(example - check)

