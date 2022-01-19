import matplotlib.pyplot as plt
from Vector import Vector2D
import numpy as np
from pygeom import Axes, Point
import pygeom.vector as v



class CarthesianPlane():
    def __init__(self,xlim,ylim,figsize) -> None:
        self.axes = Axes(xlim=xlim, ylim=ylim, figsize=figsize)
        

    def draw(self):
        self.axes.draw()
    
    def pos(self,vector:Vector2D):
        
        
        self.axes.add(vector)
        self.axes.addMany([vector.p1,vector.p2])
