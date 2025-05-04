Gaussian Splat Segmentation Methods
This repository contains implementations of various segmentation approaches for Gaussian splats, with a focus on point cloud processing and classification. The research explores different techniques for segmenting 3D scenes reconstructed with Gaussian splatting.
Repository Structure
Each method is contained in its own branch to keep the implementations clean and separate:

main: Overview and documentation
3D-Pointnet++: Implementation of PointNet++ classification approach
2D-Sam2Video: SAM2 video segmentation with mask propagation
2D-MatAnyone: MatAnyone mask-agnostic segmentation approach
3D-SpatialLM: SpatialLM-based segmentation using large language models for 3D understanding

Methods Overview
PointNet++
A true 3D approach that achieved high accuracy (86.77%) but requires extensive processing time and manual dataset preparation. While effective, it's unclear if PointNet++ can recognize similar objects within categories without specific training.
2D Masking with SAM2
SAM2 provides effective interactive refinement capabilities for 2D mask creation. It works well with high-resolution images and handles occlusion effectively. This approach lets you correct specific frames where segmentation fails and supports manual intervention when needed.
MatAnyone
A mask-agnostic approach that propagates segmentation across frames when provided with a first-frame mask. While efficient for human subjects, it struggles with inanimate objects and scenes where objects have similar colors to backgrounds.
SpatialLM
The most promising approach using language models for 3D understanding. SpatialLM processes point clouds to identify objects and architectural elements, generating bounding boxes around identified categories. Despite limitations in orientation sensitivity and run-to-run consistency, it effectively generalizes to unseen environments.
