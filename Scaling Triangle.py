from pixelplotter import pixeldrawer
import mydrawer


def scaleTriangle(x1, y1, x2, y2, x3, y3, Sx, Sy):
    x1, y1, x2, y2, x3, y3 = x1*Sx, y1*Sy, x2*Sx, y2*Sy, x3*Sx, y3*Sy
    return (x1, y1, x2, y2, x3, y3)

drawer = pixeldrawer.PixelDrawer()
drawer.start()

x1, y1, x2, y2, x3, y3 = 0, 0, 8, 0, 4, 4


mydrawer.draw_bresenhams_line(drawer, x1, y1, x2, y2)
mydrawer.draw_bresenhams_line(drawer, x3, y3, x2, y2)
mydrawer.draw_bresenhams_line(drawer, x1, y1, x3, y3)


x1, y1, x2, y2, x3, y3 = scaleTriangle(x1, y1, x2, y2, x3, y3, 3, 4)

mydrawer.draw_bresenhams_line(drawer, x1, y1, x2, y2)
mydrawer.draw_bresenhams_line(drawer, x3, y3, x2, y2)
mydrawer.draw_bresenhams_line(drawer, x1, y1, x3, y3)



drawer.execute()