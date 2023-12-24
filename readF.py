import os
import math

ChunkSize = 0  # 2 bytes


def SetChunkSize(num_of_chunks, file_path):
    real_num_of_chunks = num_of_chunks - 2;  # header chunks
    file_size = os.path.getsize(file_path)
    global ChunkSize
    ChunkSize = math.ceil(file_size / real_num_of_chunks)


def GetChunkSize():
    return ChunkSize


def FileToIntList(file_path):
    global ChunkSize
    data = bytes()
    with open(file_path, 'rb') as file:
        data = file.read()
    num_of_bytes = len(data)
    num_of_last_bytes = num_of_bytes % ChunkSize
    additional_bytes_to_add = (ChunkSize - num_of_last_bytes) % ChunkSize

    endf = (0).to_bytes(additional_bytes_to_add, 'little', signed=False)
    header = additional_bytes_to_add.to_bytes(ChunkSize, 'little', signed=False)
    data = header + data + endf

    int_ls = []
    for i in range(num_of_bytes // ChunkSize):
        byte_chunk = data[i * ChunkSize:(i + 1) * ChunkSize]
        int_ls += [int.from_bytes(byte_chunk, 'little', signed=False)]
    print(int_ls)
    return int_ls


def IntListToFile(int_ls, file_path):
    global ChunkSize
    num_of_bytes = int_ls[0]
    additional_bytes = int_ls[1]

    int_ls = int_ls[2:]
    data = bytes()
    for i in range(len(int_ls)):
        b = int_ls[i]  # this is error
        b = b.to_bytes(ChunkSize, 'little', signed=False)
        data += b

    data = data[:len(data) - additional_bytes]

    with open(file_path, 'wb') as file:
        file.write(data)
