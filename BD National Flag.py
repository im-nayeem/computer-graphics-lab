from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer

def drawFlag(plotter, length):
    # Assign minimum length
    if(length < 10):
        length = 10
        
    # Calculate measurements according to ratios
    width = round(length * (6/10))
    h = round(length * (4.5 / 10))
    k = round(width / 2)
    r = round(length / 5)

    drawer.draw_bresenhams_line(plotter, 0, 0, length, 0, plotter.GREEN)
    drawer.draw_bresenhams_line(plotter, 0, width, length, width, plotter.GREEN)
    drawer.draw_bresenhams_line(plotter, 0, 0, 0, width, plotter.GREEN)
    drawer.draw_bresenhams_line(plotter, length, 0, length, width, plotter.GREEN)
    drawer.draw_bresenhams_circle(plotter, r, h, k, plotter.RED)


# Main Section
l = int(input('Enter the length(greater than or equal to 10) of flag: '))
plotter = pixelplotter.PixelPlotter()
plotter.start()
drawFlag(plotter, l)
plotter.execute()