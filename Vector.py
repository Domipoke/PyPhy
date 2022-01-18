import math
from time import sleep
import turtle


class Vector2D():
    # Create a Vector
    # +   <- Using this Carthesian plane. 
    #-0+  <- This is x
    # -      a is the angle between x and vector
    def __init__(self,x,a) -> None:
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

    def draw(self,c):
        t=turtle.Turtle() 
        s=1
        
        #Draw Plane
        t.penup()
        t.goto()
        t.screen.window_height()/2
        t.screen.window_width()/2
        

