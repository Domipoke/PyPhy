import math
from time import sleep
import pygeom.vector as v
from pygeom import Axes, Point
import pygeom.vector as v


class Vector2D():
    # Create a Vector
    # +   <- Using this Carthesian plane. 
    #-0+  <- This is x
    # -      a is the angle between x and vector
    def __init__(self,x,a) -> None:
        self.apx = 0
        self.apy = 0
        self.x = x
        self.a = a
        self.v = self.x * math.cos(math.radians(a))
        self.y = self.v * math.sin(math.radians(a))
        print(self.x)
        print(self.y)
        print(self.v)
        print(self.a)
        print(math.cos(math.radians(a)))
        print(math.sin(math.radians(a)))
    

    def reverse(self):
        self.x = self.x*(-1)
        self.y = self.y*(-1)
        self.v = self.v*(-1)

    def add(self, Vector):
        x = self.x + Vector.x
        y = self.y + Vector.y
        t = 0
        if (x>=0&y>=0):
            t = math.atan(abs(y)/abs(x))
        elif (x>=0&y<0):
            t = 360-math.atan(abs(y)/abs(x))
        elif (x<0&y>=0):
            t = 180-math.atan(abs(y)/abs(x))
        elif (x<0&y<0):
            t = 270-math.atan(abs(y)/abs(x))
        return Vector2D(x,t)

    def setAp(self,x,y):
        self.apx = x
        self.apy = y   
        

    def draw(self):
        self.p1 = Point(self.apx,self.apy,color="gray")
        self.p2 = Point(self.x,self.y,color="gray")

        
        return v.Vector(
                p1=self.p1,
                p2=self.p2,
                head_width  = 0.25,
                head_length = 0.3)
