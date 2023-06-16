from pixelvisualizer import pixelplotter

def drawCircle(plotter, r, h, k):
    p = 1 - r
    x = 0
    y = r

    while(x <= y):
        plotter.plot_pixel(x+h , y+k)
        plotter.plot_pixel(y+h , x+k)
        plotter.plot_pixel(-y+h, x+k)
        plotter.plot_pixel(-x+h, y+k)
        plotter.plot_pixel(-x+h, -y+k)
        plotter.plot_pixel(-y+h, -x+k)
        plotter.plot_pixel(y+h, -x+k)
        plotter.plot_pixel(x+h, -y+k)

        if(p < 0):
            p = p + 2*x + 3
            x = x+1
            y = y
        else:
            p = p + p*(x - y) + 5
            x = x + 1
            y = y - 1


def takeInput():
    h, k = map(int, input('Enter coordinate of center (h, k): ').split())
    r = int(input('Enter radius of circle, r: '))
    return (r, h, k)

# Main Section
r, h, k = takeInput()

plotter = pixelplotter.PixelPlotter()
plotter.start()

drawCircle(plotter, r, h, k)

plotter.execute()
        


