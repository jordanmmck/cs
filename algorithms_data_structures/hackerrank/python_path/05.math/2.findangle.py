# -*- coding: utf-8 -*-
import math

AB = float(input())
BC = float(input())
AC = math.sqrt(AB**2 + BC**2)
MC = AC / 2

# print(AB,BC,AC,MC)

A = math.acos((AC**2 + AB**2 - BC**2) / (2 * AB * AC))
B = math.pi / 2
C = math.pi - A - B
BM = math.sqrt((MC**2) + (BC**2) - (2 * MC * BC * math.cos(C)))

# print(A,B,C)

if MC < BC:
    theta = math.asin(MC * math.sin(C) / BM)
else:
    zeta = math.asin(BC * math.sin(C) / BM)
    theta = math.pi - C - zeta

print(str(int(round(math.degrees(theta)))) + '°')
