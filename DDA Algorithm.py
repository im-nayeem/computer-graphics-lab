from pixelvisualizer import pixelplotter

def drawLine(plotter, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Declare flag to cope with negative value of dx or dy
    x_flag = 1 if dx >= 0 else -1
    y_flag = 1 if dy >= 0 else -1

    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1

    while(x * x_flag <= x2 * x_flag):
        plotter.plot_pixel(round(x), round(y))
        x = x + xinc
        y = y + yinc
        if(y * y_flag > y2 * y_flag):
            break

def takeInput():
    x1, y1 = map(int, input('Enter coordinate (x1, y1): ').split())
    x2, y2 = map(int, input('Enter coordinate (x2, y2): ').split())
    return (x1, y1, x2, y2)

# Main Section
x1, y1, x2, y2 = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()

drawLine(plotter, x1, y1, x2, y2)
plotter.execute()

