from pixelvisualizer import pixelplotter

def drawCircle(plotter, r, h, k):
    d = 3 - 2 * r
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

        if(d < 0):
            d = d + 4*x + 6
            x = x+1
            y = y
        else:
            d = d + d*(x - y) + 10
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