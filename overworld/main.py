from opensimplex import OpenSimplex
from PIL import Image, ImageDraw
from random import randint
import math
from terrain import applyColor

class IslandGen():

    def __init__(self, width, height, seed, name="Map"):
        self.width, self.height = width, height
        self.seed = seed
        self.name = str(name)
        self.image = Image.new('RGB', (width, height))
        self.mapping = OpenSimplex(seed=seed)

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

    def noise(self, iterations, x, y, persistence, scale):
        low, high = 0, 255
        maxAmp, amp = 0, 1
        value = 0

        for i in range(iterations):
            value += self.mapping.noise2d(x * scale, y * scale) * amp
            maxAmp += amp
            amp *= persistence
            scale *= 2

        value /= maxAmp
        return value * (high - low) / 2 + (high + low) / 2

    def generate(self, iterations, scale, persistence, label=True):
        for x in range(self.width):
            for y in range(self.height):
                value = self.noise(iterations, x, y, persistence, scale)
                # Creates Island Shapes
                distCenter = self.distance(x, y, self.width / 2, self.height / 2)
                adjustedPos = value * (1.0 - distCenter/ (self.width / 1.9))
                # Terrain Coloring
                color = applyColor(adjustedPos)
                self.image.putpixel((x, y), color)
        # Seed Labels
        if label == True:
            label = ImageDraw.Draw(self.image)
            label.text((5,5), "Seed: " + str(self.seed), fill=(255,255,0))
        self.image.save(self.name + ".png")

island = IslandGen(250, 250, 71, "Island2")
island.generate(3, 0.035, 0.04, True)
