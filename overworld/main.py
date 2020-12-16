from opensimplex import OpenSimplex
from PIL import Image, ImageDraw
from random import randint
import math

from terrain import applyColor

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

def shaping(x, y, value):
    distCenter = distance(x, y, WIDTH / 2, HEIGHT / 2)
    adjustedPosition = int(value * (1.0 - distCenter / (WIDTH / 1.9)))
    return adjustedPosition

def generate():
    image = Image.new('RGB', (WIDTH, HEIGHT))
    border = int(((WIDTH + HEIGHT) // 2) * 0.05)
    scale = 0.035 # Don't change this for now
    iterations = 3
    persistence = 0.05

    for x in range(WIDTH):
        for y in range(HEIGHT):
            value = adjustment(iterations, x, y, persistence, scale)

            adjustedPosition = shaping(x, y, value)
            color = applyColor(adjustedPosition)
            image.putpixel((x, y), color)

    label = ImageDraw.Draw(image)
    label.text((5,5), "Seed: " + str(seed), fill=(255,255,0))

    # image.save('generated/Seed:' + str(seed) + '.png')
    image.save('generated/test.png')


# Main
# seed = randint(0, 100) # 66, 95, 89
seed = 71
simplex = OpenSimplex(seed=seed) # 71
generate()
