# coding=utf-8
"""
blob detector
"""

import numpy as np
import sys
sys.setrecursionlimit(1000000)

class Pixel:
    """
    Pixel Class
    """

    def __init__(self,
                 x: int,
                 y: int,
                 image: 'np.ndarray'):
        self.x = x
        self.y = y
        self.image = image
        self.value = image[x, y]

    def __repr__(self):
        output = "pixel coordinates" + "\n"
        output += str(self.x) + " " + str(self.y)
        return output

    def is_on_image_border(self) -> bool:
        """
        returns True if self is on the image border, else False
        :return:
        """
        if self.x >= np.shape(self.image)[0] - 1:
            return True
        if self.x <= 0:
            return True
        if self.y >= np.shape(self.image)[1] - 1:
            return True
        if self.y <= 0:
            return True
        return False

    def is_four_connected(self) -> bool:
        """
        returns True if self is four-connected, else False
        :return:
        """
        if self.image[self.x - 1, self.y] < 1:
            return False
        if self.image[self.x + 1, self.y] < 1:
            return False
        if self.image[self.x, self.y + 1] < 1:
            return False
        if self.image[self.x, self.y - 1] < 1:
            return False
        return True

    def get_neighbor(self, direction: 'str'):
        if direction is 'left':
            return Pixel(self.x - 1, self.y, self.image)
        if direction is 'right':
            return Pixel(self.x + 1, self.y, self.image)
        if direction is 'down':
            return Pixel(self.x, self.y - 1, self.image)
        if direction is 'up':
            return Pixel(self.x, self.y + 1, self.image)
        return None


class Blob:
    """
    Blob Class
    """

    def __init__(self,
                 image: 'np.ndarray',
                 index: int,
                 seed_pixel: Pixel,
                 area: int = 0):
        self.image = image
        self.index = index
        self.area = area
        self.seed_pixel = seed_pixel
        self.pixels = []

    def __repr__(self):
        output = "blob :" + "\n"
        output += "area " + str(self.area) + "\n"
        output += "seed_" + self.seed_pixel.__repr__() + "\n"
        return output

    def grow(self, pixel: Pixel):
        """
        grows the blob
        :param pixel:
        :return:
        """
        if pixel.value != 1:
            # zero intensity region or already explored pixel
            return
        if pixel.is_on_image_border():
            return
        if pixel.is_four_connected():
            self.image[pixel.x, pixel.y] = self.index
            self.pixels.append(pixel)
            self.area += 1  # a pixel has been added to the blob
            self.grow(pixel.get_neighbor('left'))
            self.grow(pixel.get_neighbor('right'))
            self.grow(pixel.get_neighbor('up'))
            self.grow(pixel.get_neighbor('down'))
