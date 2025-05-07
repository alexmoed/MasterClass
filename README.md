# PointNet++ for 3D Gaussian Splat Segmentation

Implementation of PointNet++ for semantic segmentation of 3D Gaussian Splats, based on research by Jurski (2024) and adapted from the Pointnet_Pointnet2_pytorch repository.

## Overview

This repository implements Jurski's method which uses PointNet++ for 3D semantic segmentation of Gaussian Splats. Unlike approaches that rely on 2D projections, this method works directly with 3D data for view-independent results. As described in Jurski's thesis, the approach treats Gaussian splats as "more sophisticated point clouds" and leverages PointNet++'s hierarchical feature learning for point-level classification.

My implementation focuses on making Jurski's approach more practical and robust, addressing several challenges encountered during testing.


## Demo

[![Click to watch the video](https://storage.googleapis.com/anmstorage/Master_class/houdini_screen_capture.PNG)](https://storage.googleapis.com/anmstorage/Master_class/point_net_results.mp4)


Here are the results of this method in houdini (click on image to play video)


## Implementation Details

In implementing Jurski's method, I've added several practical enhancements:

1. **Robust Path Handling**: Added a Pandas-based solution to manage dataset inconsistencies and improve compatibility across different file structures.

2. **Parameter Optimization**: By adjusting configurations (increasing point count, expanding batch size from 8 to 32, and running 230 epochs), I achieved 87.54% accuracy, slightly exceeding the original 86.77% reported.

3. **Visualization Pipeline**: At 50-epoch intervals (or a value you choose), the system generates PLY files showing segmentation results that can be viewed in standard 3D software.

4. **Training Improvements**: Implemented optimizations that accelerated training convergence, achieving 68% evaluation accuracy in just 30 epochs when including opacity features.

## Features
- Semantic segmentation of 3D Gaussian Splat point clouds
- Multi-attribute support (position, opacity, scale, rotation)
- Checkpoint saving/loading and evaluation metrics
- Visualization of segmentation results

## Requirements
- Python 3.7+, PyTorch 1.8+, NumPy, Pandas, tqdm, TensorBoard
- PyTorch3D (specific Meta repository version)

## Dataset:

https://data.4tu.nl/datasets/3eabd3f5-d814-48be-bbff-b440f2d48a2b


Do not use Download all files! Download each catagory seperatly and place in the dataset folder. 
