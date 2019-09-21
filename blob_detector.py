# coding=utf-8
"""
blob detector
"""


class Pixel:
    """
    Pixel Class
    """

    def __init__(self,
                 x: int,
                 y: int,
                 image: 'numpy.ndarray'):
        self.x = x
        self.y = y
        self.image = image

    def __repr__(self):
        output = "pixel coordinates" + "\n"
        output += (self.x, self.y)
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

    def get_neighbor(self, direction: 'str') -> Pixel:
        if direction is 'left':
            return Pixel(self.x - 1, self.y, self.image)
        if direction is 'right':
            return Pixel(self.x + 1, self.y, self.image)
        if direction is 'down':
            return Pixel(self.x - 1, self.y, self.image)
        if direction is 'up':
            return Pixel(self.x + 1, self.y, self.image)
        return None


class Blob:
    """
    Blob Class
    """

    def __init__(self,
                 image: 'numpy.ndarray',
                 index: int,
                 area: int = 0):
        self.image = image
        self.index = index
        self.area = area

    def grow(self, pixel: Pixel):
        """
        grows the blob
        :param pixel:
        :return:
        """
        if self.image[pixel.x, pixel.y] != 1:
            # zero intensity region or already explored pixel
            return
        if is_border(x, y, im):
            return
        if four_connected(x, y, im):
            self.image[pixel.x, pixel.y] = self.index
            self.area += 1  # a pixel has been added to the blob
            grow(pixel.get_neighbor('left'))
            grow(pixel.get_neighbor('right'))
            grow(pixel.get_neighbor('up'))
            grow(pixel.get_neighbor('down'))
        return


