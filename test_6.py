from solution_6 import Point

point_1 = Point((10, -5))
print(point_1)
print(point_1.get_x())
print(point_1.get_y())
point_2 = Point()
print(point_2)
point_3 = Point((5, -4))
print(point_3)
print(point_1.distance(point_3))
point_4 = point_3.sum(point_1)
print(point_4)
b = [point_1]
print(b)
