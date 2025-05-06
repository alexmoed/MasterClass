# PointNet++ for 3D Gaussian Splat Segmentation

Implementation of PointNet++ for semantic segmentation of 3D Gaussian Splats, based on research by Jurski (2024) and adapted from the Pointnet_Pointnet2_pytorch repository.

## Overview

This repository implements Jurski's method which uses PointNet++ for 3D semantic segmentation of Gaussian Splats. Unlike approaches that rely on 2D projections, this method works directly with 3D data for view-independent results. As described in Jurski's thesis, the approach treats Gaussian splats as "more sophisticated point clouds" and leverages PointNet++'s hierarchical feature learning for point-level classification.

My implementation focuses on making Jurski's approach more practical and robust, addressing several challenges encountered during testing.

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

5,375,467,257 bytesMD5:e5e59812ce27af6e1ee72d8568d6dd183DGS_bathtub.rar
30,889,396,053 bytesMD5:dfa6d66e1d9ef0a8b321f8ea427245753DGS_bed.rar
44,186,767,323 bytesMD5:b7747a6cced408b051a38622c8efba5c3DGS_chair.rar
12,523,258,874 bytesMD5:3d7b1032e2da3a0ab1703e0b38b466c03DGS_desk.rar
15,279,758,621 bytesMD5:b44476afa1a56d7d652727d818686f683DGS_dresser.rar
21,995,165,548 bytesMD5:d8c20ba50d60d1b90c18d2b9292651bd3DGS_monitor.rar
17,880,282,631 bytesMD5:53ab88a72543b118cacded001921c49f3DGS_night_stand.rar
29,589,761,274 bytesMD5:4fdfd05bbfa73f3eebfd851101250ea93DGS_sofa.rar
20,470,978,396 bytesMD5:bffaecae63693dff7223425bf9852c6b3DGS_table.rar
20,626,864,343 bytesMD5:33df1627c47020022b5a84eb8e587ef23DGS_toilet.rar
68,511,949 bytesMD5:6e059a224c68ff512ce3cc71f955e6bcBlenderMVScript.rar
Do not use Download all files! Download each catagory seperatly and place in the dataset folder. 
