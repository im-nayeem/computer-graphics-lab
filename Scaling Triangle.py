from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer

def scaleTriangle(x1, y1, x2, y2, x3, y3, Sx, Sy):
    x1, y1, x2, y2, x3, y3 = x1*Sx, y1*Sy, x2*Sx, y2*Sy, x3*Sx, y3*Sy
    return (x1, y1, x2, y2, x3, y3)

plotter = pixelplotter.PixelPlotter()
plotter.start()

x1, y1, x2, y2, x3, y3 = 0, 0, 8, 0, 4, 4


drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)
drawer.draw_bresenhams_line(plotter, x3, y3, x2, y2)
drawer.draw_bresenhams_line(plotter, x1, y1, x3, y3)


x1, y1, x2, y2, x3, y3 = scaleTriangle(x1, y1, x2, y2, x3, y3, 3, 4)

drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2, plotter.GREEN)
drawer.draw_bresenhams_line(plotter, x3, y3, x2, y2, plotter.GREEN)
drawer.draw_bresenhams_line(plotter, x1, y1, x3, y3, plotter.GREEN)

plotter.execute()