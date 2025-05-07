# SAM2 Video Segmentation for Gaussian Splats

This branch implements segmentation using Meta's SAM2 Video model to create high-quality masks for Gaussian splat source images, with specialized export functionality for Postshot.

## Overview

SAM2 Video enables the segmentation of image sequences by propagating selections across frames while allowing for interactive refinement. This approach is particularly effective for creating masks with complex boundaries and handling occlusion.

## Key Features

- **Interactive Refinement**: Correct specific frames where segmentation fails
- **High-Resolution Support**: Works well with 6000×9000px images
- **Object Consistency**: Rarely confuses unrelated objects or selects them randomly
- **Occlusion Handling**: Effectively tracks objects that are partially visible or cut off
- **Multi-Object Support**: Multiple object selections can be combined into a binary mask
  
## Dataset:
https://storage.googleapis.com/anmstorage/Master_class/Chair_splat_dataset.zip

## Sam2Video Example results:
![SAM2 Animation](https://storage.googleapis.com/anmstorage/Master_class/sam2.%5B0000-0090%5D.gif)

## Postshot Export System

This implementation features a specialised export system designed specifically for Postshot compatibility. The export process:

1. Automatically creates versioned output directories (v001, v002, etc.)
2. Combines multiple object masks into a single binary mask
3. Adds the binary mask as an alpha channel to the original image WITHOUT premultiplication
4. Exports as PNG files with the alpha channel in Postshot's required format

## Postshot Mask Processing

## POSTSHOT MASK EXPORTING

 1. COMBINE MASKS: Merge all object masks into one binary mask
   - WHITE (255) = Subject
   - BLACK (0) = Background

 2. ADD AS ALPHA CHANNEL: Attach mask to original image as alpha channel
    - Preserves full RGB data
    - No premultiplication
    - No actual transparency applied

 3. SAVE AS PNG: Contains original image with mask as alpha channel
    (Alpha is not premultiplied or set for transparency)
    - Standard format for Postshot
   
  ## POSTSHOT Results 

  
