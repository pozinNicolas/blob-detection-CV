# biocarbon - technical test

Blob detection algorithm : detects four-connected blobs with given size and intensity on a single band tiff image.

**Modules** :
* main.py 
* blob_detector.py : contains custom functions for blob detection
* blob_detector_test.py : a test module
* image_generator.py : a simple synthetic image generator with blobs to test the algo
* data : folder with tiff image for test

**NB** :
* To perform blob detection (blobs with size **blob_size** and intensity **blob_intensity**) on an image stored at address **image_path**, launch the following command from the terminal:
```
python main.py -p image_path -bs blob_size -bi blob_intensity
```




### TODO (some ideas)
- [ ] work on blob representation
- [ ] implement parallel blob detection for faster treatment


### illustration 

Input image            |  Image with kept detected blobs only
:-------------------------:|:-------------------------:
[image](data/blobs.tif) |  [image](data/blobs_detected.tif)


### author 
Nicolas Pozin (23/09/19)


