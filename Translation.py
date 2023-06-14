from pixelvisualizer import pixelplotter

def translate(plotter, coordinates, tx, ty):
    for item in coordinates:
        item['x'] = item['x'] + tx
        item['y'] = item['y'] + ty
        plotter.plot_pixel(item['x'], item['y'], plotter.RED)


     
def main():
    # List containing the coordinates
    coordinates = [{'x':1, 'y':4}, {'x':2, 'y':4}, 
                   {'x':3, 'y':4}, {'x':4, 'y':4},
                   {'x':5, 'y':4}, {'x':4, 'y':5},
                   {'x':2, 'y':5}, {'x':3, 'y':5}, {'x':3, 'y':6}]
    
    # translation vector [tx, ty]
    tx, ty = 5, 8 

    plotter = pixelplotter.PixelPlotter()
    plotter.start()

    # Before Translation
    for item in coordinates:
        plotter.plot_pixel(item['x'], item['y'])

    # After Translation
    translate(plotter, coordinates, tx, ty)
    
    plotter.execute()

main()
