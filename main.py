import numpy as np

from blob_detector.py import Pixel, Blob
from image_generator.py import generate_image

if __name__ == '__main__':

    # generate synthetic image
    image = generate_image()

    # detect every blobs in the image
    non_zeros = np.where(im == 1)
    if not non_zeros:
        print("no blob")
    else:
        non_zero_pixels = list(
            zip(non_zeros[0], non_zeros[1]))  # list of tuples with non zeros pixel coords
        for pix in non_zero_pixels:
            pixel=Pixel()
            if image[pix[0], pix[1]] != 1:
                continue
            blob_grow(el[0], el[1], im, ind)
            nb_blobs += 1

    def image_loop(im):
        result = np.where(im == 1)
        ind = 2
        if not result:
            return ind - 2
        listOfCoordinates = list(zip(result[0], result[1]))
        nb_blobs = 0
        for el in listOfCoordinates:
            if im[el[0], el[1]] != 1:
                continue
            blob_grow(el[0], el[1], im, ind)
            nb_blobs += 1
        return nb_blobs
