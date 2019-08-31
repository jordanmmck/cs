import numpy
import math

A = list(map(float, inumpyut().split()))
B = list(map(float, inumpyut().split()))
C = list(map(float, inumpyut().split()))
D = list(map(float, inumpyut().split()))

# A=[0, 4, 5]
# B=[1, 7, 6]
# C=[0, 5, 9]
# D=[1, 7, 2]

AB = numpy.subtract(B, A)
BC = numpy.subtract(C, B)
CD = numpy.subtract(D, C)

ABBC = numpy.cross(AB, BC)
BCCD = numpy.cross(BC, CD)

numer = numpy.dot(ABBC, BCCD)
denom = numpy.linalg.norm(ABBC) * numpy.linalg.norm(BCCD)
print(math.degrees(math.acos(numer / denom)))
# print("%.2f"%(math.degrees(math.acos(numer/denom))))
