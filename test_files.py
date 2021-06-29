from equations import *
from triangle import *
from point import *

# Distance Formula
# p1=point(3,0)
# p2=point(0,4)
# print(p1.distance(p2))


# Section Formula
#Internal division
# p1=point(4,4)
# p2=point(8,8)
# print(p1.section(p2,m=1,n=3))

# # External division
#
# print(p1.section(p2,m=1,n=3,external=True))


# Slope
# p1=point(1,1)
# p2=point(3,3)
# print(p1.slope(p2))


#####################################################################################################
# Triangles
# A=point(0,0)
# B=point(5,0)
# C=point(5*math.cos(math.pi/3),5*math.sin(math.pi/3))
# t1=Triangle(A,B,C)
# print(t1.area())
# print(t1.incenter())
# print(t1.centroid())
# print(t1.circumcenter())
# print(t1.orthocenter())


#####################################################################################################

# Lines
# Solve
# l1=equation_type2(a=3,b=4,c=-5)
# l2=equation_type2(a=3,b=-4,c=-7)
# print(l1.solve(l2))

# Angle between lines
# l1=equation_type5(point(1,1),point(2,2))
# l2=equation_type5(point(-1,1),point(-3,3))
# print(l1.slope)
# print(l2.slope)
# print(l1.angle(l2))
# print(l1.is_perpendicular(l2))
# print(l1.is_parallel(l2))


# Distance between point and line

# l1=equation_type4(point(0,0),0)
# pt=point(3,0)
# print(l1.distance(pt))

# Image of a point and foot of perpendicular in a line

# l1=equation_type4(point(0,0),1)
# pt=point(1,2)
# print(l1.foot_of_perpendicular(pt))
# print(l1.image_of_point(pt))

