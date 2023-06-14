from pixelvisualizer import pixelplotter

def drawLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    b = y1 - m*x1

    if(dx < 0):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    
    while(True):
        plotter.plot_pixel(round(x), round(y))
        x = x+1
        y = m * x + b
        if(x > xend):
            break

x1 , y1 = map(int, input('Enter x1 and y1: ' ).split())
x2 , y2 = map(int, input('Enter x2 and y2: ' ).split())

plotter = pixelplotter.PixelPlotter()
plotter.start()
drawLine(x1, y1, x2, y2)
plotter.execute()