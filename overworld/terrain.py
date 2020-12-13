# Color Chart
chart = {
    15 : (29, 65, 173), # Depths
    25 : (65, 105, 225), # Shallows
    40 : (238, 214, 175), # Sand
    70 : (34, 139, 34), # Grassland
    95 : (36, 110, 27), # Woodlands
    120 : (87, 83, 74), # Mountains
    160 : (36, 36, 36), # Mountain Peaks
    255 : (255, 250, 250) # Snow
}

def applyColor(value, chart=chart):
    for i in chart:
        if value < i:
            return chart[i]
