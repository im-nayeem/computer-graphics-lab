from pixelplotter import pixeldrawer
drawer = pixeldrawer.PixelDrawer()

def drawLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1

    while(x <= x2):
        drawer.draw_pixel(round(x), round(y))
        x = x + xinc
        y = y + yinc
        
        if(y > y2):
            break;


drawer.start()
drawLine(0, 0, 5, 6)
drawer.execute()


