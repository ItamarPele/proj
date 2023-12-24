ChunkSize = 2  # 2 bytes

def SetChunkSize(Chunk):
    global ChunkSize
    ChunkSize = Chunk


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

    new_num_of_bytes = len(data) + ChunkSize  # plus one for additional header
    len_header = new_num_of_bytes.to_bytes(ChunkSize, 'little', signed=False)
    data = len_header + data

    int_ls = []
    for i in range(new_num_of_bytes // ChunkSize):
        byte_chunk = data[i * ChunkSize:(i + 1) * ChunkSize]
        int_ls += [int.from_bytes(byte_chunk, 'little', signed=False)]
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
