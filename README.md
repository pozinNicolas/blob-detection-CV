# biocarbon

Blob detection algorithm : detects four connected blobs with given size and intensity on a single band tiff image

* data analysis test
* To perform blob detection (blobs with size **blob_size** and blob intensity **blob_intensity**) on an image stored at address **file_path** launch this command from the terminal:
```
python main.py -f file_path -bs blob_size -bi blob_intensity 
```

### TODO (some ideas)
- [ ] work on blob representation
- [ ] implement parallel blob detection for faster treatment


### illustration 

Input image            |  Image with kept detected blobs only
:-------------------------:|:-------------------------:
[Input image](data/blobs.tif) |  [Image with kept detected blobs only](data/blobs_detected.tif)


