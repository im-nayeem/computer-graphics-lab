from pixelvisualizer import pixelplotter

def bresenhamsLineDrawing(plotter, x1, y1, x2, y2):
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1

    m = dy/dx
 
    if(m < 1):
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        p = c1 - dy
    else:
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        p = c1 - dy

    while(x <= x2):
        plotter.plot_pixel(x, y)
        if(m < 1):
            if(p < 0):
                p = p + c1
                x = x + 1
                y = y
            else:
                p = p + c2
                x = x + 1
                y = y + 1
        else:
            if(p < 0):
                p = p + c1
                x = x 
                y = y + 1
            else:
                p = p + c2
                x = x + 1
                y = y + 1

def takeInput():
    x1, y1 = map(int, input('Enter coordinate (x1, y1): ').split())
    x2, y2 = map(int, input('Enter coordinate (x2, y2): ').split())
    return (x1, y1, x2, y2)


# Main Section
x1, y1, x2, y2 = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()

bresenhamsLineDrawing(plotter, x1, y1, x2, y2)
plotter.execute()