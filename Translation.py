from pixelplotter import pixeldrawer


def translate(drawer, coordinates, tx, ty):
    for item in coordinates:
        item['x'] = item['x'] + tx
        item['y'] = item['y'] + ty
        drawer.draw_pixel(item['x'], item['y'])


     
def main():

    coordinates = [{'x':1, 'y':4}, {'x':2, 'y':4}, 
                   {'x':3, 'y':4}, {'x':4, 'y':4},
                   {'x':5, 'y':4}, {'x':4, 'y':5},
                   {'x':2, 'y':5}, {'x':3, 'y':5}, {'x':3, 'y':6}]

    tx, ty = 5, 8 

    drawer = pixeldrawer.PixelDrawer()
    drawer.start()
    for item in coordinates:
        drawer.draw_pixel(item['x'], item['y'])

    translate(drawer, coordinates, tx, ty)
    
    drawer.execute()

main()
