# SAM2 + MatAnyone
This pipeline creates a seamless integration between SAM2 mask prediction and MatAnyone for mask propagation across video frames. The system automatically passes masks and paths between components for efficient video object segmentation.
Pipeline Overview

SAM2 generates an initial segmentation mask for the first frame
Frames are resized to 2048×1080 due to VRAM limitations while maintaining quality
MatAnyone propagates the initial mask through all subsequent frames
Output is saved with consistent naming and organisation in the source folder 

This integration eliminates manual steps between mask generation and propagation, creating a streamlined workflow for video segmentation tasks. At the time of starting this method, it was not available and it was suggested to use a SAM2 demo online, download the files, and upload to MatAnyone. I streamlined this process.


# Dataset:
https://storage.googleapis.com/anmstorage/Master_class/Chair_splat_dataset.zip
