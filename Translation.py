from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer

def translate(x1, y1, x2, y2, tx, ty):
    return (x1+tx, y1+ty, x2+tx, y2+ty)


def takeInput():
    x1, y1 = map(int, input('Enter coordinate (x1, y1): ').split())
    x2, y2 = map(int, input('Enter coordinate (x2, y2): ').split())
    tx, ty = map(int, input('Enter translation vector (tx, ty): ').split())
    return (x1, y1, x2, y2, tx, ty)


# Main Section
x1, y1, x2, y2,tx, ty = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()

drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)

x1, y1, x2, y2 = translate(x1, y1, x2, y2, tx, ty)

drawer.draw_bresenhams_line(plotter, x1, y1, x2, y2)

plotter.execute()