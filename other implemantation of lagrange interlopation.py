from MD import *
import readF


# Python3 program for implementation
# of Lagrange's Interpolation

# To represent a data point corresponding to x and y = f(x)
class Data:
    def __init__(self, x, y):
        self.x = MD(x)
        self.y = MD(y)
    def __repr__(self):
        return f"({self.x}, {self.y})"


# function to interpolate the given data points
# using Lagrange's formula
# xi -> corresponds to the new data point
# whose value is to be obtained
# n -> represents the number of known data points
def interpolate(f: list, xi: MD, n: MD) -> MD:
    # Initialize result
    result = MD(0)
    for i in range(n.value):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n.value):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)

        # Add current term to result
        result += term

    return result


# Driver Code
if __name__ == "__main__":

    f = list(enumerate(readF.FileToIntList(r"C:\Users\itama\PycharmProjects\pythonProject\Proj\myHit\A.txt")))
    num_of_points = f[0][1]//2
    F = list()
    for p in f:
        F.append(Data(p[0], p[1]))
    print(F)

    FF = []
    for i in range(num_of_points*2):
        FF.append(Data(i, interpolate(F, MD(i), MD(len(F))).value))

    newF = FF[::2]
    print(newF)

    f = []
    for i in range(num_of_points):
        f.append((i, interpolate(newF, MD(i), MD(len(newF))).value))
    print(f)


    lastf = []
    for a in f:
        lastf.append(a[1])

    readF.IntListToFile(lastf,r"C:\Users\itama\PycharmProjects\pythonProject\Proj\myHit\ads.txt" )



# This code is contributed by
# sanjeev2552
