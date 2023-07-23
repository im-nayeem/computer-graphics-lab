from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer

def reflectTriangleX(x1, y1, x2, y2, x3, y3):
    x1, y1, x2, y2, x3, y3 = x1, -y1, x2, -y2, x3, -y3
    drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2, plotter.RED)
    drawer.draw_bresenhams_line(plotter, x2, y2, x3, y3, plotter.RED)
    drawer.draw_bresenhams_line(plotter, x3, y3, x1, y1, plotter.RED)

def reflectTriangleY(x1, y1, x2, y2, x3, y3):
    x1, y1, x2, y2, x3, y3 = -x1, y1, -x2, y2, -x3, y3
    drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2, plotter.RED)
    drawer.draw_bresenhams_line(plotter, x2, y2, x3, y3, plotter.RED)
    drawer.draw_bresenhams_line(plotter, x3, y3, x1, y1, plotter.RED)
 
def takeInput():
    x1, y1 = map(int, input('Enter coordinate (x1, y1): ').split())
    x2, y2 = map(int, input('Enter coordinate (x2, y2): ').split())
    x3, y3 = map(int, input('Enter coordinate (x3, y3): ').split())
    return (x1, y1, x2, y2, x3, y3)


# Main Section
x1, y1, x2, y2, x3, y3 = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()
# Before Reflection
drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)
drawer.draw_bresenhams_line(plotter, x2, y2, x3, y3)
drawer.draw_bresenhams_line(plotter, x3, y3, x1, y1)

reflectTriangleX(x1, y1, x2, y2, x3, y3)
reflectTriangleY(x1, y1, x2, y2, x3, y3)




plotter.execute()