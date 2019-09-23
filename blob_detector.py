# coding=utf-8
"""
blob detector
"""

import numpy as np
import gdal
gdal.UseExceptions()
from PIL import Image
from typing import List

import sys

sys.setrecursionlimit(1000000)


class Pixel:
    """
    Pixel Class
    """

    def __init__(self,
                 x: int,
                 y: int,
                 image_array: 'np.ndarray'):
        self.x = x
        self.y = y
        self.image_array = image_array
        self.value = image_array[x, y]

    def __repr__(self):
        output = "pixel coordinates" + "\n"
        output += str(self.x) + " " + str(self.y)
        return output

    def is_on_image_border(self) -> bool:
        """
        returns True if self is on the image border, else False
        :return:
        """
        if self.x >= np.shape(self.image_array)[0] - 1:
            return True
        if self.x <= 0:
            return True
        if self.y >= np.shape(self.image_array)[1] - 1:
            return True
        if self.y <= 0:
            return True
        return False

    def is_four_connected(self) -> bool:
        """
        returns True if self is four-connected, else False
        :return: bool
        """
        if self.image_array[self.x - 1, self.y] == 0:
            return False
        if self.image_array[self.x + 1, self.y] == 0:
            return False
        if self.image_array[self.x, self.y + 1] == 0:
            return False
        if self.image_array[self.x, self.y - 1] == 0:
            return False
        return True

    def get_neighbor(self, direction: 'str'):
        """
        gets neighbor pixel in the image
        :param direction:
        :return:
        """
        if direction is 'left':
            return Pixel(self.x - 1, self.y, self.image_array)
        if direction is 'right':
            return Pixel(self.x + 1, self.y, self.image_array)
        if direction is 'down':
            return Pixel(self.x, self.y - 1, self.image_array)
        if direction is 'up':
            return Pixel(self.x, self.y + 1, self.image_array)
        return None


class Blob:
    """
    Blob Class
    """

    def __init__(self,
                 image_array: 'np.ndarray',
                 index: int,
                 seed_pixel: Pixel,
                 area: int = 0):
        self.image_array = image_array
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
            # zero intensity pixel or pixels already assigned to a blob
            return
        if pixel.is_on_image_border():
            return
        if pixel.is_four_connected():
            # NB : for the sake of recursion, pixels assigned to a blob have to be stored someway.
            # for each encountered pixel, we could check it belongs or not to an incremented list
            # of already assigned pixels
            # For efficiency purpose, we rather set the value of assigned pixels to a given
            # arbitrary number (here -1). Tests are thus made much faster.
            self.image_array[pixel.x, pixel.y] = -1
            self.pixels.append(pixel)
            self.area += 1  # a pixel has been added to the blob
            self.grow(pixel.get_neighbor('left'))
            self.grow(pixel.get_neighbor('right'))
            self.grow(pixel.get_neighbor('up'))
            self.grow(pixel.get_neighbor('down'))


class BlobDetector:
    """
    Blob Detector
    """

    def __init__(self,
                 image_path: 'str',
                 blob_size: int,
                 blob_intensity: int):
        self.image_path = image_path
        self.blob_size = blob_size
        self.blob_intensity = blob_intensity

    def load(self) -> 'np.ndarray' or None:
        """
        load a single band geotiff file and outputs a the associated image np array
        :return: 'np.ndarray'
        """
        img = gdal.Open(self.image_path)
        try:
            band = img.GetRasterBand(1)
            return np.array(band.ReadAsArray())
        except RuntimeError:
            print("band not found")
            return None

    def mask(self, image_array: 'np.ndarray') -> 'np.ndarray':
        """
        returns masks of the image array
        :param image_array:
        :return:
        """
        tmp = image_array == self.blob_intensity
        tmp = Image.fromarray(np.uint8(tmp), 'L')
        image_array_masked = np.asarray(tmp, dtype="int32")

        return image_array_masked

    def apply(self) -> List['Blob']:
        """
        generates list of all blobs in the image specified by self.image_path
        only blobs with size>=blob_size, intensity = blob_intensity are considered
        :return:
        """
        image_array = self.mask(self.load())
        list_blobs = []
        non_zeros = np.where(image_array == 1)
        if not non_zeros:
            print("no blob in the image")
            return list_blobs
        non_zero_pixels = list(
            zip(non_zeros[0], non_zeros[1]))  # list of tuples with non zeros pixel coords
        for p, pix in enumerate(non_zero_pixels):
            pixel = Pixel(x=pix[0], y=pix[1], image_array=image_array)
            if pixel.value != 1:
                continue
            blob = Blob(image_array, index=p + 1, seed_pixel=pixel, area=0)
            blob.grow(pixel)
            if blob.area > self.blob_size:
                list_blobs.append(blob)

        print(len(list_blobs), " have been detected in the image")

        return list_blobs


