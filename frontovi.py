from pyautocad import Autocad, APoint,aDouble
import numpy as np
import array
import math
from math import *

# Creating Autocad drawing
acad = Autocad(create_if_not_exists=True)


# Iterate through objects in Autocad drawing
for obj in acad.iter_objects(dont_cast=True):

    lis = obj.Coordinates

it = iter(lis)

tacke = []
# Iterate through each coordinate in the list creating points.
for x in it:
    tacke.append([x,next(it)])


def crtaj():

    # Iterate through points
    for currentPoint in range(len(tacke)):



        next = currentPoint + 1




        point1 = tacke[currentPoint]
        point2 = tacke[next]

        X1 = point1[0]
        Y1 = point1[1]
        X2 = point2[0]
        Y2 = point2[1]




        # The correct equation for measuring the distance between 2 points.
        distance = format(math.sqrt((X1-X2)**2 + (Y1-Y2)**2),f".{int(2)}f")


        dy = X2-X1
        dx = Y2-Y1

        # Finding correct rotation of the line
        if dy > 0 and dx > 0:

            dd = round(degrees(atan(dy/dx)),2)

        if dy > 0 and dx < 0:

            dd = round(degrees(atan(dy/dx)),2)+180

        if dy < 0 and dx < 0:

            dd = round(degrees(atan(dy/dx)),2)+180

        if dy < 0 and dx > 0:

            dd = round(degrees(atan(dy/dx)),2)+360


        Xn = X1+dy/2
        Yn = Y1+dx/2

        # Writing text on the drawing
        point = APoint(Xn,Yn)

        name1 = acad.model.AddText(distance,point,1)
        name1.Rotate(point,radians(90-dd))





        # print(dd)
        # print(distance)

crtaj()
