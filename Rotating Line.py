from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer
import math

def rotateLine(x, y, theta):
    PI = math.acos(-1.0)
    theta = theta*PI/180
    x_new = x*math.cos(theta) - y*math.sin(theta)
    y_new = x*math.sin(theta) + y*math.cos(theta)
    return (round(x_new), round(y_new))

def takeInput():
    x1, y1 = map(int, input('Enter coordinate (x1, y1): ').split())
    x2, y2 = map(int, input('Enter coordinate (x2, y2): ').split())
    theta = int(input('Enter angle of rotation in degree: '))
    return (x1, y1, x2, y2, theta)


# Main Section
x1, y1, x2, y2, theta = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()
# Before Rotation
drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)
# Rotate
x2, y2 = rotateLine(x2, y2, theta)
# After Rotation
drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2, plotter.RED)
plotter.execute()