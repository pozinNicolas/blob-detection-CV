import numpy as np
import time

from blob_detector import Pixel, Blob
from image_generator import generate_image

if __name__ == '__main__':

    # generate synthetic image
    image = generate_image()

    # time measure
    to = time.time()

    # detect every blobs in the image
    list_blobs = []
    non_zeros = np.where(image == 1)
    if not non_zeros:
        print("no blob")
    else:
        non_zero_pixels = list(
            zip(non_zeros[0], non_zeros[1]))  # list of tuples with non zeros pixel coords
        for p, pix in enumerate(non_zero_pixels):
            pixel = Pixel(x=pix[0], y=pix[1], image=image)
            if pixel.value != 1:
                continue
            blob = Blob(image, index=p + 2, seed_pixel=pixel, area=0)
            blob.grow(pixel)
            if blob.area > 400:
                list_blobs.append(blob)

    print("number of blobs detected ", len(list_blobs))
    print("process time", time.time() - to)
