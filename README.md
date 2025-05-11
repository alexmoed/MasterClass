# PointNet++ for 3D Gaussian Splat Segmentation

Implementation of PointNet++ for semantic segmentation of 3D Gaussian Splats, based on research by Jurski (2024) and adapted from the Pointnet_Pointnet2_pytorch repository.

## Overview

This repository implements Jurski's method, which applies PointNet++ to semantic 3D segmentation of Gaussian splats by category. PointNet++ categorises points using hierarchical feature learning, enabling direct classification of each point in the Gaussian splat cloud. The method assigns semantic labels (chair, table, sofa, etc.) to each point, rather than working with 2D projections. This point-level segmentation approach creates consistent results that aren't dependent on viewing angle, making it particularly valuable for scene manipulation and object isolation in 3D space.

## Features

- Semantic segmentation of 3D Gaussian Splat point clouds
- Multi-attribute support (position, opacity, scale, rotation)
- Checkpoint saving/loading and evaluation metrics
- Visualization of segmentation results

## Demo

[![Click to watch the video](https://storage.googleapis.com/anmstorage/Master_class/houdini_screen_capture.PNG)](https://storage.googleapis.com/anmstorage/Master_class/point_net_results.mp4)

Here are the results of this method in Houdini (click on image to play video)

## Implementation Details

In implementing Jurski's method, I've added several practical enhancements:

1. **Robust Path Handling**: Added a Pandas-based solution to manage dataset inconsistencies and improve compatibility across different file structures.
2. **Parameter Optimization**: By adjusting configurations (increasing point count, expanding batch size from 8 to 32, and running 230 epochs), I achieved 87.54% accuracy, slightly exceeding the original 86.77% reported.
3. **Visualization Pipeline**: At 50-epoch intervals (or a value you choose), the system generates PLY files showing segmentation results that can be viewed in standard 3D software.
4. **Training Improvements**: Implemented optimizations that accelerated training convergence, achieving 68% evaluation accuracy in just 30 epochs when including opacity features.

## Installation and Setup

### Requirements

- Python 3.7+
- PyTorch 1.8+
- NumPy
- Pandas
- tqdm
- TensorBoard
- PyTorch3D (specific Meta repository version)

# Install dependencies
pip install -r requirements.txt

# Install PyTorch3D from Meta repository (required specific version)
# This step may take 20+ minutes
pip install "git+https://github.com/facebookresearch/pytorch3d.git"
