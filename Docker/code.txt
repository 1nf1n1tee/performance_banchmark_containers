docker build -t dedup-app -f container_file_name(example - crc_containerfile) . 
docker run --name anything(example - check) dedup-app
docker cp check:/app/ile_name(example - "CRC32 Deduplication Report ign.csv.txt") /home/al-is-working/Desktop/docker_results/run_data
docker rm name(example - check)
