import numpy as np
import time

from blob_detector import Pixel, Blob, BlobDetector
from image_generator import generate_image

if __name__ == '__main__':

    # generate synthetic image
    # image = generate_image()

    from PIL import Image

    image = generate_image()
    img_tmp = Image.fromarray(np.uint8(image * 255), 'L')
    img_tmp.save('blobs.tif')

    # time measure
    to = time.time()

    blob_detector = BlobDetector(image_path='blobs.tif', blob_size=400, blob_intensity=255)
    list_detected_blobs = blob_detector.apply()

    print("blob detection process time", time.time() - to)

