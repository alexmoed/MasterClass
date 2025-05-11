# Gaussian Splat Segmentation Methods

## Overview

This repository contains multiple approaches to segment Gaussian splats, providing both 2D and 3D segmentation techniques. Each method is maintained in its own branch to keep implementations organised.

## Branch Structure

**Each method is contained in its own branch:**

- **main**: Overview and documentation

- **3D-Pointnet++**: Implementation of PointNet++ classification approach
  
  https://github.com/alexmoed/MasterClass/tree/3D-Pointnet%2B%2B

- **2D-Sam2Video**: SAM2 video segmentation with mask propagation
 
   https://github.com/alexmoed/MasterClass/tree/2D-Sam2Video

- **2D-MatAnyone**: MatAnyone mask-agnostic segmentation approach
  
   https://github.com/alexmoed/MasterClass/tree/2D-MatAnyone

- **3D-SpatialLM**: SpatialLM-based segmentation using large language models for 3D understanding
 
   https://github.com/alexmoed/MasterClass/tree/3D-SpatialLM


## Methods Overview

### 3D-Based Approaches

#### 3D-SpatialLM
**Description**: Leverages large language models for 3D understanding of point clouds. SpatialLM processes unstructured point cloud data to identify objects and architectural elements, generating bounding boxes around identified categories.

**Key Features**:
- Processes unstructured point clouds from various sources (LiDAR, Gaussian splats)
- Identifies patterns and classifies objects into semantic categories
- Generates bounding boxes that can be used for segmentation
- Processes scenes in minutes rather than hours
- Works with reasonable VRAM requirements (~15GB with default settings)

**Limitations**:
- Orientation sensitivity (requires Z-up orientation and specific rotation)
- Inconsistent results between identical processing runs
- Variable performance between model variants (Qwen-0.5B better for furniture, Llama-1B better for structural elements)
- Occasional omission of primary objects
- Bounding box accuracy limitations

**Implementation Notes**:
- Point extraction from bounding boxes implemented with Open3D
- Generates a Classified PLY file 
- Customizable parameters discovered: num_beams, top_k, temperature

#### 3D-Pointnet++
**Description**: Application of PointNet++ to semantic 3D segmentation of Gaussian splats at point level. Treats Gaussian splats as sophisticated point clouds and builds hierarchical feature learning.

**Key Features**:
- Achieved high accuracy (87.54% in our testing)
- Works directly with 3D point cloud data on a point level
- Effectively incorporates multiple feature types (position, opacity, scale, rotation)

**Limitations**:
- Requires extensive processing time (24+ hours on A100 GPU)
- Needs a fixed number of points (Current implementations uniform sampling limiting objects to 4096-1288 points) or a number of your choosing. 
- Dataset-specific implementation 
- Appears to memorise specific examples rather than learning generalizable features

**Implementation Notes**:
- Includes sampling, grouping, and feature extraction layers
- Pandas-based solution implemented for path management
- Class distribution analysis shows relatively even weighting across categories
- Export of classified PLY files 

### 2D-Based Approaches

#### 2D-Sam2Video
**Description**: Leverages SAM2's video segmentation capabilities to create masks that propagate across frames. This approach allows for interactive refinement when segmentation fails.

**Key Features**:
- Effective interactive refinement capabilities
- Support for high-resolution images (tested with 6000×9000px photos)
- Modest VRAM requirements (5GB) with substantial RAM usage (56.2GB)
- Handles occlusion well, tracking partially visible objects

**Limitations**:
- Consistency issues between runs
- Requires manual intervention on problematic frames
- High RAM requirements may limit accessibility
- Occasional difficulties with thin elements like chair legs

**Implementation Notes**:
- Successfully tested with panoramic image sequences
- Post-processing workflow includes alpha channel handling in Nuke and Photoshop
- Compatible with PostShot for Gaussian splat generation
- Creates a Image with a Alpha Channel 
- Combines multiple object selections into binary masks

#### 2D-MatAnyone
**Description**: A mask-agnostic approach where first-frame masking allows propagation across all frames. Designed to maintain temporal consistency across video sequences.

**Key Features**:
- Mask-agnostic approach providing flexibility for integration
- Automated process after initial mask creation
- High-quality performance for human subjects
- Integration options with existing post-production workflows

**Limitations**:
- Primarily designed for human subjects, less effective for inanimate objects
- Struggles with objects sharing similar colour profiles with backgrounds
- Difficulty with semi-occluded objects that change over time
- Sensitive to frame rate 

**Implementation Notes**:
- Requires downscaling high-resolution images due to VRAM constraints
- Technical workflow obstacles include frame transposition issues
- Performs better with video footage than image sequences


### Method Selection Guide
- For high-quality results with manual refinement capability: **2D-Sam2Video**
- For fully automated processing of human subjects: **2D-MatAnyone**
- For direct 3D scene understanding with object categories: **3D-SpatialLM**
- For detailed point-level segmentation with training capability: **3D-Pointnet++**

- ## Additional Resources

- **GSOPS (Gaussian Splat Operators)**: While not part of this repository, GSOPS is a Houdini plugin that was used during testing to visualize and refine segmentation results. It provides functionality for viewing and filtering splat attributes, performing clean-up operations, and classifying splats using built-in methods like DBSCAN. https://github.com/david-rhodes/GSOPs

- **PostShot**: Used for generating Gaussian splats from image sequences with the alpha channel masks created by the 2D-based methods in this repository.
