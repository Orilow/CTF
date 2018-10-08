import os.path
import hashlib

sha_hashes = []
chunk_size = 32768
first_file_size = os.path.getsize("files/lena512color.tiff")


with open("files/torrent_sha1_hashes.txt", "rb") as hashes_file:
    cont = hashes_file.read()
    for i in range(0, len(cont) - 20, 20):
        sha_hashes.append(cont[i:i+20])

needed_chunk_number = int(first_file_size / chunk_size)
needed_chunk_hash = sha_hashes[needed_chunk_number]

first_file_bytes_count_in_needed_chunk = first_file_size - chunk_size * needed_chunk_number
second_file_bytes_count_in_needed_chunk = chunk_size - 4 - first_file_bytes_count_in_needed_chunk

with open("files/lena512color.tiff", 'rb') as tiff_file:
    tiff_cont = tiff_file.read()
    raw_first_file_part = tiff_cont[first_file_size - first_file_bytes_count_in_needed_chunk: first_file_size]

with open("files/lena512.mat", "rb") as mat_file:
    raw_second_file_part = mat_file.read(second_file_bytes_count_in_needed_chunk)

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                pass
                pin = (str(a) + str(b) + str(c) + str(d)).encode()
                test_chunk = raw_first_file_part + pin + raw_second_file_part
                test_chunk_hash = hashlib.sha1(test_chunk).digest()
                if test_chunk_hash == needed_chunk_hash:
                    print(int(pin))
