from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer

def scaleTriangle(x1, y1, x2, y2, x3, y3, Sx, Sy):
    x1, y1, x2, y2, x3, y3 = x1*Sx, y1*Sy, x2*Sx, y2*Sy, x3*Sx, y3*Sy
    return (x1, y1, x2, y2, x3, y3)

def takeInput():
    x1, y1 = map(int, input('Enter coordinate (x1,y1): ').split())
    x2, y2 = map(int, input('Enter coordinate (x2,y2): ').split())
    x3, y3 = map(int, input('Enter coordinate (x3,y3): ').split())
    Sx, Sy = map(int, input('Enter scaling factor (Sx,Sy): ').split())
    return (x1, y1, x2, y2, x3, y3, Sx, Sy)


# Main Section
x1, y1, x2, y2, x3, y3, Sx, Sy = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()

drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)
drawer.draw_bresenhams_line(plotter, x3, y3, x2, y2)
drawer.draw_bresenhams_line(plotter, x1, y1, x3, y3)

x1, y1, x2, y2, x3, y3 = scaleTriangle(x1, y1, x2, y2, x3, y3, Sx, Sy)

drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2, plotter.GREEN)
drawer.draw_bresenhams_line(plotter, x3, y3, x2, y2, plotter.GREEN)
drawer.draw_bresenhams_line(plotter, x1, y1, x3, y3, plotter.GREEN)

plotter.execute()