from pixelvisualizer import pixelplotter
from pixelvisualizer import drawer as mydrawer

def drawFlag(drawer, length):
    # Assign minimum length
    if(length < 10):
        length = 10
        
    # Calculate measurements according to ratios
    width = round(length * (6/10))
    h = round(length * (4.5 / 10))
    k = round(width / 2)
    r = round(length / 5)

    mydrawer.draw_bresenhams_line(drawer, 0, 0, length, 0)
    mydrawer.draw_bresenhams_line(drawer, 0, width, length, width)
    mydrawer.draw_bresenhams_line(drawer, 0, 0, 0, width)
    mydrawer.draw_bresenhams_line(drawer, length, 0, length, width)
    mydrawer.draw_bresenhams_circle(drawer, r, h, k)


drawer = pixelplotter.PixelPlotter()
drawer.start()
drawFlag(drawer, 27)
drawer.execute()



    

