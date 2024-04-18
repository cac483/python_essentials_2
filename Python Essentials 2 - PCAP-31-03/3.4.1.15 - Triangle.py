import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return (math.hypot((self.__x - x),(self.__y - y)))

    def distance_from_point(self, point):
        return (math.hypot((self.__x - point.getx()),(self.__y - point.gety())))


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__v1 = vertice1
        self.__v2 = vertice2
        self.__v3 = vertice3

    def perimeter(self):
        return self.__v1.distance_from_point(self.__v2) + self.__v2.distance_from_point(self.__v3) + self.__v3.distance_from_point(self.__v1)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
