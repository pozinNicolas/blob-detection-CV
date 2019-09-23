# coding=utf-8

"""
main module
"""

from blob_detector import BlobDetector
import time

if __name__ == '__main__':

    ######### parser #########
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--image_path", help="image path",
                        default='data/blobs.tif')
    parser.add_argument("-bs", "--blob_size", help="blob size",
                        default='400')
    parser.add_argument("-bi", "--blob_intensity", help="blob intensity",
                        default='255')
    args = parser.parse_args()

    image_path = str(args.image_path)
    blob_size = int(args.blob_size)
    blob_intensity = int(args.blob_intensity)

    ######### blob detection #########
    to = time.time()

    # detects all blobs with given size and intensity in a tif image
    blob_detector = BlobDetector(image_path=image_path, blob_size=blob_size,
                                 blob_intensity=blob_intensity)
    list_detected_blobs = blob_detector.apply()

    print("blob detection process time", time.time() - to)
