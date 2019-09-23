# test module

import pytest
from blob_detector import BlobDetector


def blob_detector_test():
    """
    Test : blobs.tif shall contain 51 blobs of intensity = 255 and size >=400
    :return:
    """

    blob_detector = BlobDetector(image_path='blobs.tif', blob_size=400, blob_intensity=255)
    list_detected_blobs = blob_detector.apply()

    assert len(list_detected_blobs) == 51
