from pixelvisualizer import pixelplotter
plotter = pixelplotter.PixelPlotter()

# (c) Nayeem Hossain

def drawLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    x_flag = 1 if dx >= 0 else -1
    y_flag = 1 if dy >= 0 else -1

    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1

    while(x*x_flag <= x2*x_flag):
        plotter.plot_pixel(round(x), round(y))
        x = x + xinc
        y = y + yinc
        if(y*y_flag > y2*y_flag):
            break


plotter.start()
drawLine(0, 0, 0, 10)
plotter.execute()


