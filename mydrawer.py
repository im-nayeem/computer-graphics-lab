def draw_line(drawer, x1, y1, x2, y2):
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


def draw_bresenhams_circle(drawer, r, h, k):
    d = 3 - 2 * r
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

        if(d < 0):
            d = d + 4*x + 6
            x = x+1
            y = y
        else:
            d = d + d*(x - y) + 10
            x = x + 1
            y = y - 1
            