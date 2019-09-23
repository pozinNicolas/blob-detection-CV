# biocarbon - technical test

Blob detection algorithm : detects four-connected blobs with given size and intensity on a single band tiff image.

* To perform blob detection (blobs with size **blob_size** and intensity **blob_intensity**) on an image stored at address **image_path**, launch the following command from the terminal:
```
python main.py -p image_path -bs blob_size -bi blob_intensity
```

* data : folder with tiff image for test


### TODO (some ideas)
- [ ] work on blob representation
- [ ] implement parallel blob detection for faster treatment


### illustration 

Input image            |  Image with kept detected blobs only
:-------------------------:|:-------------------------:
[image](data/blobs.tif) |  [image](data/blobs_detected.tif)


Nicolas Pozin (23/09/19)


