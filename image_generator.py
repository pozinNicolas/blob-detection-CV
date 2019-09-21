# coding=utf-8
"""
image generator module : generate sysnthetic image for blob detector test prurpose
"""

import numpy as np
import random

# global parameter
IMAGE_SIZE = 2500
BLOB_AVERAGE_SIZE = 50
NUMBER_OF_BLOBS = 100
BLOB_DETECTION_SIZE = 400


def set_rectangle_block(img: 'np.ndarray') -> bool:
    """
    insert a rectangle in img at random position and with random dimensions
    :param img:
    :return:
    """

    # lower left corner of the rectangle
    x = random.randint(0, IMAGE_SIZE - 1)
    y = random.randint(0, IMAGE_SIZE - 1)
    # dimensions of the rectangle
    size_x = random.randint(1, BLOB_AVERAGE_SIZE)
    size_y = random.randint(1, BLOB_AVERAGE_SIZE)

    # upper right corner  of the rectangle - NB the rectangle fits in the image
    x_max = min(IMAGE_SIZE - 1, x + size_x)
    y_max = min(IMAGE_SIZE - 1, y + size_y)

    # the rectangle does not overlapp an existing rectangle
    if (np.max(img[x:x_max + 1, y:y_max + 1])) == 1:
        return False

    img[x:x_max + 1, y:y_max + 1] = 1
    blob_area = (x_max - x - 1) * (y_max - y - 1)  # remove borders for area of 4-connected blob
    print("blob generated area", blob_area)
    return blob_area >= BLOB_DETECTION_SIZE


def generate_image() -> 'np.ndarray':
    """

    :return:
    """
    img = np.zeros((IMAGE_SIZE, IMAGE_SIZE))
    nb_blobs_detectable = 0
    for i in range(NUMBER_OF_BLOBS):
        nb_blobs_detectable += set_rectangle_block(img)
    print("number of detectable blobs in the synthetic image", nb_blobs_detectable)
    return img
