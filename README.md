# Gaussian Splat Segmentation Methods

## Overview

This repository contains multiple approaches to segment Gaussian splat representations, providing both 2D and 3D segmentation techniques. Each method is maintained in its own branch to keep implementations clean and separate.

## Branch Structure

Each method is contained in its own branch:

- **main**: Overview and documentation
- **3D-Pointnet++**: Implementation of PointNet++ classification approach
- **2D-Sam2Video**: SAM2 video segmentation with mask propagation
- **2D-MatAnyone**: MatAnyone mask-agnostic segmentation approach
- **3D-SpatialLM**: SpatialLM-based segmentation using large language models for 3D understanding

## Methods Overview

### 3D-Based Approaches

#### 3D-SpatialLM
The most promising approach using language models for 3D understanding. SpatialLM processes point clouds to identify objects and architectural elements, generating bounding boxes around identified categories. Despite limitations in orientation sensitivity and run-to-run consistency, it effectively generalizes to unseen environments.

#### 3D-Pointnet++
A true 3D approach that achieved high accuracy (86.77%) but requires extensive processing time and manual dataset preparation. While effective, it's unclear if PointNet++ can recognize similar objects within categories without specific training.

### 2D-Based Approaches

#### 2D-Sam2Video
SAM2 provides effective interactive refinement capabilities for 2D mask creation. It works well with high-resolution images and handles occlusion effectively. This approach lets you correct specific frames where segmentation fails and supports manual intervention when needed.

#### 2D-MatAnyone
A mask-agnostic approach that propagates segmentation across frames when provided with a first-frame mask. While efficient for human subjects, it struggles with inanimate objects and scenes where objects have similar colors to backgrounds.

## Integration with Open3D & GSOPS

The repository includes tools for:
- Extracting points from bounding boxes using Open3D's `get_point_indices_within_bounding_box` function
- Assigning classification attributes to points for filtering and segmentation
- Working with Houdini's GSOPS (Gaussian Splat Operators) for visualization and refinement

## Custom Exporting

Includes code for creating versioned output directories and processing masks as alpha channels in the format required by Postshot:

```python
def create_versioned_directory(base_dir, base_name):
    """
    Creates a versioned directory like 'Mask_v001' inside of the source directory 
    and increments if other ones exists.
    Returns the path to the created directory.
    """
    version = 1
    while True:
        dir_name = f"{base_name}_v{version:03d}"
        full_path = os.path.join(base_dir, dir_name)
        
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            return full_path
        
        version += 1
