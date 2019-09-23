# biocarbon

Blob detection algorithm : detects four connected blobs with given size and intensity on a single band tiff image

* To perform blob detection (blobs with size **blob_size** and blob intensity **blob_intensity**) on an image stored at address **image_path**, launch this command from the terminal:
```
python main.py -p image_path -bs blob_size -bi blob_intensity
```

*data : tiff image for test


### TODO (some ideas)
- [ ] work on blob representation
- [ ] implement parallel blob detection for faster treatment


### illustration 

Input image            |  Image with kept detected blobs only
:-------------------------:|:-------------------------:
[image](data/blobs.tif) |  [image](data/blobs_detected.tif)


