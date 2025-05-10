## SAM2-MatAnyone Integration Pipeline

This pipeline creates an integration between SAM2 mask prediction and MatAnyone for mask propagation across video frames. The system automatically passes masks and paths between components for video object segmentation. At the time of starting this method, it was not available and it was suggested to use a SAM2 demo online, download the files, and upload to MatAnyone. I streamlined this process.

### Pipeline Overview

1. SAM2 generates an initial segmentation mask for the first frame
2. Frames are resized to 2048×1080 due to VRAM limitations while maintaining quality
3. MatAnyone propagates the initial mask through all subsequent frames
4. Output is saved with consistent naming and organisation in the source folder

### Implementation Details

My implementation successfully integrated the two systems, automating what was previously a multi-step manual process. The technical integration worked as intended, with masks being properly passed between components and results being saved with consistent organization.

### Significant Limitations

While the pipeline itself functioned as designed, the underlying MatAnyone method had severe limitations for our use case:

- **Poor Subject Performance**: Performed poorly on inanimate objects despite working well with human subjects
- **Color Similarity Issues**: Struggled with objects sharing similar colors with backgrounds (e.g., sofas blending with floors)
- **Camera Movement Problems**: Failed when camera movement introduced previously unobserved regions
- **Frame Rate Sensitivity**: Performed inconsistently depending on frame rates
- **Resolution Constraints**: Required significant downscaling from 6K×9K to 2048×1080 due to VRAM limitations

Despite the pipeline functioning correctly from a technical integration standpoint, the underlying approach proved unsuitable for our Gaussian splat preparation needs. Testing showed the SAM2Video method to be a more effective alternative for our specific requirements.

# Dataset:
https://storage.googleapis.com/anmstorage/Master_class/Chair_splat_dataset.zip
# Example broken output video: 

[![MatAnyone Fail Thumbnail](https://storage.googleapis.com/anmstorage/Master_class/matanyone_fail.0122.png)](https://storage.googleapis.com/anmstorage/Master_class/matanyone_fail.mp4)

(Click on photo to watch video)
