from opensimplex import OpenSimplex
from PIL import Image, ImageDraw
import math

# World Dimensions
WIDTH, HEIGHT = 250, 250

def distance(x1, y1, x2, y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def adjustment(iterations, x, y, persistence, scale, low=0, high=255):
    amp, maxAmp = 1, 0
    noise = 0

    for i in range(iterations):
        noise += simplex.noise2d(x * scale, y * scale) * amp
        maxAmp += amp
        amp *= persistence
        scale *= 2

    # Average and normalize the output
    noise /= maxAmp
    return noise * (high - low) / 2 + (high + low) / 2

def terrainColors(value):
    depth = (29, 65, 173)
    shallows = (65, 105, 225)
    sand = (238, 214, 175)
    grass = (34, 139, 34)
    mountain = (87, 83, 74)
    peaks = (36, 36, 36) 
    snow = (255, 250, 250)
    if value < 15:
        return depth
    elif value < 25:
        return shallows
    elif value < 40:
        return sand
    elif value < 70:
        return grass
    elif value < 120:
        return mountain
    elif value < 180:
        return peaks
    return snow

def generate():
    image = Image.new('RGB', (WIDTH, HEIGHT))
    border = int(((WIDTH + HEIGHT) // 2) * 0.05)
    scale = 0.045 # Don't change this for now
    iterations = 2
    persistence = 0.05

    for x in range(WIDTH):
        for y in range(HEIGHT):
            value = adjustment(iterations, x, y, persistence, scale)

            distCenter = distance(x, y, WIDTH / 2, HEIGHT / 2)
            adjustedPosition = int(value * (1.0 - distCenter / (WIDTH / 1.9)))

            color = terrainColors(adjustedPosition)
            image.putpixel((x, y), color)

    label = ImageDraw.Draw(image)
    label.text((5,5), "Seed: " + str(seed), fill=(255,255,0))

    image.save('generated/Seed: ' + str(seed) + '.png')


# Main
seed = randint(0, 100) # 66, 95, 89
simplex = OpenSimplex(seed=seed)
generate()
