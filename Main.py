from lagrange_interlopation import *
import readF
from sympy import nextprime
import math
from MD import MD

READ_FILE_PATH = r"C:\Users\itama\PycharmProjects\pythonProject\Proj\myHit\fileFrom.txt"
WRITE_FILE_PATH = r"C:\Users\itama\PycharmProjects\pythonProject\Proj\myHit\FileTo.txt"

if __name__ == "__main__":
    NUM_OF_COMPUTERS = 5
    readF.SetChunkSize(NUM_OF_COMPUTERS, READ_FILE_PATH)
    largest_number_possible = int(math.pow(2, (readF.GetChunkSize() * 8)) - 1)
    m = int(nextprime(largest_number_possible))
    print(m)
    MD.modulus = m


    byte_chunks_from_file = readF.FileToIntList(READ_FILE_PATH)

    print(byte_chunks_from_file)
    input()  ###

    indexed_bytes = list(enumerate(byte_chunks_from_file))
    print(indexed_bytes)
    input()  ###

    num_of_points = byte_chunks_from_file[0]
    p_list = list()
    for p in indexed_bytes:
        p_list.append(Data(p[0], p[1]))

    print(p_list)
    input()  ###

    new_points_list = list()
    for i in range(num_of_points * 2):
        new_points_list.append(Data(i, interpolate(p_list, MD(i), MD(len(p_list))).value))
    print(new_points_list)
    input()  ###

    half_of_points = new_points_list[::2]
    print(half_of_points)
    input()  ###

    original_list = []
    for i in range(num_of_points):
        # print(f"{num_of_points - i}..", end="")
        original_list.append((i, interpolate(half_of_points, MD(i), MD(len(half_of_points))).value))
    print(original_list)
    input()  ###

    original_bytes = []
    for a in original_list:
        original_bytes.append(a[1])
    print(original_bytes)
    input()  ###

    readF.IntListToFile(original_bytes, WRITE_FILE_PATH)

# Lagrange code is contributed by
# sanjeev2552
# thx!
