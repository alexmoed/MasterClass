# SAM2 Video Segmentation for Gaussian Splats

## Overview
This branch implements segmentation using Meta's SAM2 Video model to create masks for Gaussian splat source images. It also has specialised export functionality for Postshot. SAM2 Video enables the segmentation of image sequences by propagating selections across frames while allowing for interactive refinement. This approach is particularly effective for creating masks with complex boundaries and handling occlusion.

## Key Features
- **Interactive Refinement**: Correct specific frames where segmentation fails
- **High-Resolution Support**: Works well with 6000×9000px images
- **Occlusion Handling**: Effectively tracks objects that are partially visible or cut off, with prediction capability for hidden object portions
- **Object Consistency**: Rarely confuses unrelated objects or selects them randomly
- **Multi-Object Support**: Multiple object selections can be combined into a binary mask
- **Effective with Panoramic Sequences**: Successfully tested across panoramic image sequences

## Implementation Details
The implementation uses SAM2's `propagate-in-video` function which maintains memory of previous frames. Users can place click markers to specify objects for segmentation, which can be configured with a numpy array specifying XY coordinates of markers and labels (1 for inclusion, 0 for exclusion).

## Usage Instructions
1. Prepare image sequences in a folder structure
2. Run the script with path to the image folder
3. Place markers on objects in the first frame
4. Process the sequence with automatic propagation
5. Review results and make manual corrections where needed
6. Export as alpha masks for Postshot

## Export Functionality
- Takes the generated segmentation masks and combines them with original images
- Properly embeds masks as unpremultiplied alpha channels in PNG format
- Places exported files in the input footage folder with a consistent naming convention
- Creates files that can be directly imported into PostShot for Gaussian splat generation
- Eliminates the need for manual compositing in external applications
  
## Limitations
- Consistency issues between multiple runs
- Some manual intervention required on problematic frames
- Occasional difficulties with thin elements like chair legs
- High RAM requirements (56.2GB)

## Demo
[![Chair Segmentation Demo](https://storage.googleapis.com/anmstorage/Master_class/Thumbnail_chair.PNG)](https://storage.googleapis.com/anmstorage/Master_class/chair_demo_video.mp4)

Click the image above to view a demo video showing the SAM2 Video segmentation and resulting Gaussian splat of a chair.

## POSTSHOT Results 
![3D Gaussian Splatting Chair Rendering](PostShot_3DGS_results/chair_3DGS.png)

3DGS created from matted SAM2Video image sequences using Postshot.

## Aknowlegements 
https://github.com/facebookresearch/sam2
