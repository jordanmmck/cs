from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# print(dot_product)

# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print(xyz)
# -> Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# print(xyz.Class)

# from collections import namedtuple
# N = int(input());student = namedtuple('student',input().strip().split())
# print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

N = int(input())
attributes = list(input().split())
ind = attributes.index('MARKS')
gradesum = 0

for i in range(N):
    l = list(input().split())
    gradesum += int(l[ind])
print(gradesum / N)
