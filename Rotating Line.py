from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer
import math


plotter = pixelplotter.PixelPlotter()
PI = math.acos(-1.0)

def rotateLine(x, y, theta):
    theta = theta*PI/180
    x_new = x*math.cos(theta) - y*math.sin(theta)
    y_new = x*math.sin(theta) + y*math.cos(theta)
    return (round(x_new), round(y_new))


plotter.start()
x1, y1, x2, y2 = 0, 0, 0, 15
drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)

x2, y2 = rotateLine(x2, y2, 30)

drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2, plotter.RED)

plotter.execute()

    