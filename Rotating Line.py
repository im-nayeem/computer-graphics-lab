from pixelplotter import pixeldrawer
import mydrawer
import math


plotter = pixeldrawer.PixelDrawer()
PI = math.acos(-1.0)

def rotateLine(x, y, theta):
    theta = theta*PI/180
    x_new = x*math.cos(theta) - y*math.sin(theta)
    y_new = x*math.sin(theta) + y*math.cos(theta)
    return (round(x_new), round(y_new))


plotter.start()
x1, y1, x2, y2 = 0, 0, 10, 5
mydrawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)

x2, y2 = rotateLine(x2, y2, 30)

mydrawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)

plotter.execute()

    