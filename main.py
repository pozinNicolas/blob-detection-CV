# coding=utf-8

"""
main module
"""

from blob_detector import BlobDetector
import time

if __name__ == '__main__':
    to = time.time()

    blob_detector = BlobDetector(image_path='data/blobs.tif', blob_size=400, blob_intensity=255)
    list_detected_blobs = blob_detector.apply()

    print("blob detection process time", time.time() - to)
