from pixelplotter import pixeldrawer

def bresenhamsLineDrawing(drawer, x1, y1, x2, y2):
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
        drawer.draw_pixel(x, y)
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
            



app = pixeldrawer.PixelDrawer()
app.start()
bresenhamsLineDrawing(app, -7, 10, 20, -4)
app.execute()
