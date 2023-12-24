from MD import *
import readF
from lagrange_interlopation import *
from sympy import nextprime
import time

READ_FILE_PATH = r"C:\Users\itama\PycharmProjects\pythonProject\Proj\myHit\A.txt"
WRITE_FILE_PATH = r"C:\Users\itama\PycharmProjects\pythonProject\Proj\myHit\ads.txt"


def RunOfLagrangeInterpolatein(ChunkSize):
    readF.SetChunkSize(ChunkSize)

    byte_chunks_from_file = readF.FileToIntList(READ_FILE_PATH)
    size = byte_chunks_from_file[2] # FOR TIME TEST

    MD.modulus = nextprime(size * 10)


    print(byte_chunks_from_file)
    #input()  ###

    indexed_bytes = list(enumerate(byte_chunks_from_file))
    #print(indexed_bytes)
    #input()  ###

    num_of_points = byte_chunks_from_file[0] // 2
    p_list = list()
    for p in indexed_bytes:
        p_list.append(Data(p[0], p[1]))

    #print(p_list)
    #input()  ###

    new_points_list = list()
    for i in range(num_of_points * 2):
        # print(f"{num_of_points*2 - i}..", end="")
        new_points_list.append(Data(i, interpolate(p_list, MD(i), MD(len(p_list))).value))
    #print(new_points_list)
    #input()  ###

    half_of_points = new_points_list[::2]
    #print(half_of_points)
    #input()  ###

    original_list = []
    for i in range(num_of_points):
        # print(f"{num_of_points - i}..", end="")
        original_list.append((i, interpolate(half_of_points, MD(i), MD(len(half_of_points))).value))
    #print(original_list)
    #input()  ###

    original_bytes = []
    for a in original_list:
        original_bytes.append(a[1])
    #print(original_bytes)
    #input()  ###

    readF.IntListToFile(original_bytes, WRITE_FILE_PATH)


if __name__ == "__main__":
    ls = []
    RunOfLagrangeInterpolatein(1)
"""
    for i in range(2, 15):
        print(i)
        start_time = time.time()
        RunOfLagrangeInterpolatein(i)
        end_time = time.time()
        lenght = end_time - start_time

        l = (i, lenght)

        ls.append(l)
        print("DONEEE!")
        print(ls)
"""