from pixelplotter import pixeldrawer

def drawCircle(drawer, r, h, k):
    p = 1 - r
    x = 0
    y = r

    while(x <= y):
        drawer.draw_pixel(x+h , y+k)
        drawer.draw_pixel(y+h , x+k)
        drawer.draw_pixel(-y+h, x+k)
        drawer.draw_pixel(-x+h, y+k)
        drawer.draw_pixel(-x+h, -y+k)
        drawer.draw_pixel(-y+h, -x+k)
        drawer.draw_pixel(y+h, -x+k)
        drawer.draw_pixel(x+h, -y+k)

        if(p < 0):
            p = p + 2*x + 3
            x = x+1
            y = y
        else:
            p = p + p*(x - y) + 5
            x = x + 1
            y = y - 1
app = pixeldrawer.PixelDrawer()
app.start()
drawCircle(app, 7, 10, 10,10)
app.execute()

        


