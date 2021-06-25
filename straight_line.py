import math
import sys
def sgn(x:float):
    if x==0:
        return 0
    elif x<0:
        return -1
    else:
        return 1


class equation_type1:
    '''
    Slope and y intercept format
    '''
    def __init__(self,slope,y_intercept):
        self.slope=slope
        self.y_intercept=y_intercept
        self.a=-self.slope
        self.b=1
        self.c=-y_intercept


    def __eq__(self, other):

        if self.a==other.a or self.b==other.b or self.c==other.c:
            if self.a==other.a and self.b==other.b and self.c==other.c:
                return True
            else:
                return False

        if (self.a/other.a)==(self.b/other.b)==(self.c/other.c):
            return True
        else:
            return False


    def __str__(self):
        s=f' y = {self.slope} x + {self.y_intercept}'
        return s

    def is_parallel(self,other):
        if self.slope==other.slope:
            return True
        else:
            return False

    def is_perpendicular(self,other):
        if (self.slope*other.slope)==-1:
            return True
        else:
            return False

    def angle(self,other):
        if self.is_parallel(other):
            return 0
        elif self.is_perpendicular(other):
            return math.pi/2
        else:
            m1=self.slope
            m2=other.slope
            tan_angle=abs((m1-m2)/(1+(m1*m2)))
            angle=math.atan(tan_angle)
            return angle

######################################################################################

class equation_type2:
    '''
    General Format
    '''
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        if b!=0:
            self.slope=-a/b
            self.y_intercept=-c/b
        else:
            self.slope=math.inf
            self.y_intercept=math.inf

    def __eq__(self, other):

        if self.a == other.a or self.b == other.b or self.c == other.c:
            if self.a == other.a and self.b == other.b and self.c == other.c:
                return True
            else:
                return False

        if (self.a / other.a) == (self.b / other.b) == (self.c / other.c):
            return True
        else:
            return False



    def __str__(self):
        s=f'{self.a} x + {self.b} y + {self.c} = 0'
        return s

    def is_parallel(self,other):
        if self.slope==other.slope:
            return True
        else:
            return False

    def is_perpendicular(self,other):
        if (self.slope*other.slope)==-1:
            return True
        else:
            return False

    def angle(self,other):
        if self.is_parallel(other):
            return 0
        elif self.is_perpendicular(other):
            return math.pi/2
        else:
            m1=self.slope
            m2=other.slope
            tan_angle=abs((m1-m2)/(1+(m1*m2)))
            angle=math.atan(tan_angle)
            return angle

######################################################################################


class equation_type3:
    '''
    Intercept Format
    '''
    def __init__(self,x_intercept,y_intercept):
        self.a=y_intercept
        self.b=x_intercept
        self.c=-(x_intercept*y_intercept)
        self.y_intercept=y_intercept

        if self.b!=0:
            self.slope=-self.a/self.b
        else:
            self.slope=math.inf

    def __eq__(self, other):

        if self.a == other.a or self.b == other.b or self.c == other.c:
            if self.a == other.a and self.b == other.b and self.c == other.c:
                return True
            else:
                return False

        if (self.a / other.a) == (self.b / other.b) == (self.c / other.c):
            return True
        else:
            return False


    def __str__(self):
        s=f'{self.a} x + {self.b} y + {self.c} = 0'
        return s

    def is_parallel(self,other):
        if self.slope==other.slope:
            return True
        else:
            return False

    def is_perpendicular(self,other):
        if (self.slope*other.slope)==-1:
            return True
        else:
            return False

    def angle(self,other):
        if self.is_parallel(other):
            return 0
        elif self.is_perpendicular(other):
            return math.pi/2
        else:
            m1=self.slope
            m2=other.slope
            tan_angle=abs((m1-m2)/(1+(m1*m2)))
            angle=math.atan(tan_angle)
            return angle



######################################################################################

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False


    def distance(self,other):
        d=(((self.x-other.x)**2 )+((self.y-other.y)**2))**(0.5)
        return d

    def section(self,other,m,n,external=False):
        if m<0 or n<0:
            sys.stderr.write('Expected positive input of m and n')
            exit(1)

        if external==False:
            x=(m*other.x + n*self.x)/(m+n)
            y=(m*other.y + n*self.y)/(m+n)
            return point(x,y)
        else:
            if (m-n)==0:
                sys.stderr.write('External division not possible')
                exit(1)
            else:
                x=(m*other.x - n*self.x)/(m-n)
                y=(m*other.y - n*self.y)/(m-n)
            return point(x,y)


    def __str__(self):
        s=f'( {self.x} , {self.y} )'
        return s

    def area_of_triangle(self, p2, p3):
        area=0.5*abs((self.x*(p2.y-p3.y))+(p2.x*(p3.y-self.y))+(p3.x*(self.y-p2.y)))
        return area

    def centroid(self,p2,p3):
        x=(self.x+p2.x+p3.x)/(3.0)
        y=(self.y+p2.y+p3.y)/(3.0)
        return point(x,y)

    def incenter(self,B,C):
        a=B.distance(C)
        b=self.distance(C)
        c=self.distance(B)
        if a==0 or b==0 or c==0:
            sys.stderr.write('Can not find the in_center of a line')
            exit(1)
        Ix=(a*self.x + b*B.x + c*C.x)/(a+b+c)
        Iy=(a*self.y + b*B.y + c*C.y)/(a+b+c)
        return point(Ix,Iy)

    def slope(self,other):
        if self==other:
            sys.stderr.write('Can not find slope of a single point\n')
            exit(1)
        elif self.x==other.x:
            sys.stderr.write('Slope not defined')
            exit(1)
        else:
            dy=self.y-other.y
            dx=self.x-other.x
            return (dy/dx)


######################################################################################

class equation_type4:
    '''
    Point , Slope Format
    '''
    def __init__(self, pt:point,slope):
        m=slope
        self.a = -slope
        self.b = 1
        self.c = (m*pt.x - pt.y)
        self.slope=slope
        if self.b != 0:
            self.y_intercept = -self.c / self.b
        else:
            self.y_intercept = math.inf

    def __eq__(self, other):

        if self.a == other.a or self.b == other.b or self.c == other.c:
            if self.a == other.a and self.b == other.b and self.c == other.c:
                return True
            else:
                return False

        if (self.a / other.a) == (self.b / other.b) == (self.c / other.c):
            return True
        else:
            return False



    def __str__(self):
        s = f'{self.a} x + {self.b} y + {self.c} = 0'
        return s

    def is_parallel(self, other):
        if self.slope == other.slope:
            return True
        else:
            return False

    def is_perpendicular(self, other):
        if (self.slope * other.slope) == -1:
            return True
        else:
            return False

    def angle(self, other):
        if self.is_parallel(other):
            return 0
        elif self.is_perpendicular(other):
            return math.pi / 2
        else:
            m1 = self.slope
            m2 = other.slope
            tan_angle = abs((m1 - m2) / (1 + (m1 * m2)))
            angle = math.atan(tan_angle)
            return angle

######################################################################################
class equation_type5:
    '''
    Two Point Format
    '''
    def __init__(self, pt:point,pt2:point):
        m=slope=(pt2.y-pt.y)/(pt2.x-pt.x)

        self.a = -slope
        self.b = 1
        self.c = (m*pt.x - pt.y)
        self.slope=slope
        if self.b != 0:
            self.y_intercept = -self.c / self.b
        else:
            self.y_intercept = math.inf

    def __eq__(self, other):

        if self.a == other.a or self.b == other.b or self.c == other.c:
            if self.a == other.a and self.b == other.b and self.c == other.c:
                return True
            else:
                return False

        if (self.a / other.a) == (self.b / other.b) == (self.c / other.c):
            return True
        else:
            return False


    def __str__(self):
        s = f'{self.a} x + {self.b} y + {self.c} = 0'
        return s

    def is_parallel(self, other):
        if self.slope == other.slope:
            return True
        else:
            return False

    def is_perpendicular(self, other):
        if (self.slope * other.slope) == -1:
            return True
        else:
            return False

    def angle(self, other):
        if self.is_parallel(other):
            return 0
        elif self.is_perpendicular(other):
            return math.pi / 2
        else:
            m1 = self.slope
            m2 = other.slope
            tan_angle = abs((m1 - m2) / (1 + (m1 * m2)))
            angle = math.atan(tan_angle)
            return angle

######################################################################################


class Triangle:
    def __init__(self,A:point,B:point,C:point):
        self.A=A
        self.B=B
        self.C=C
        self.a = B.distance(C)
        self.b = A.distance(C)
        self.c = A.distance(B)

    def area(self):
        area=0.5*abs((self.A.x*(self.B.y-self.C.y))+(self.B.x*(self.C.y-self.A.y))+(self.C.x*(self.A.y-self.B.y)))
        return round(area,5)

    def centroid(self):
        x=(self.A.x+self.B.x+self.C.x)/(3.0)
        y=(self.A.y+self.B.y+self.C.y)/(3.0)
        return point(x,y)

    def incenter(self):
        # a=B.distance(C)
        # b=self.distance(C)
        # c=self.distance(B)
        if self.a==0 or self.b==0 or self.c==0:
            sys.stderr.write('Can not find the in_center of a line\n')
            exit(1)
        Ix=(self.a*self.A.x + self.b*self.B.x + self.c*self.C.x)/(self.a+self.b+self.c)
        Iy=(self.a*self.A.y + self.b*self.B.y + self.c*self.C.y)/(self.a+self.b+self.c)
        return point(Ix,Iy)










# Area
# p1=point(0,3)
# p2=point(4,0)
# p3=point(0,0)
# t1=Triangle(p1,p2,p3)
# print(t1.area())

# l1=equation_type5(point(0,-1),point(1,0))
# print(l1)
# l2=equation_type4(point(1,0),1)
# print(l2)
# print(l1==l2)
l1=equation_type4(point(1,1),1)
l2=equation_type5(point(3,3),point(4,4))
print(l1)
print(l2)
print(l1==l2)
# Success
'''
Able to calculate section , angle between lines,
equation by two point , slope and point , intercept form , general form , slope and intercept form

'''


