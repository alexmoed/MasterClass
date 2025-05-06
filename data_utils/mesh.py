

# @brief Train a semantic segmentation model for 3D Gaussian Splats
# Modified from :-
# Yanx27 (2019). PointNet_Pointnet2_pytorch [online].
# [Accessed 2024]. Available from: "https://github.com/yanx27/Pointnet_Pointnet2_pytorch"
# Based on research from:
# Jurski, K. (2024). Semantic 3D segmentation of 3D Gaussian Splats: Assessing existing
# point cloud segmentation techniques on semantic segmentation of synthetic 3D Gaussian
# Splats scenes. Bachelor's Thesis, Delft University of Technology.
# Extended implementation: "https://github.com/karol-202/direct-3dgs-segmentation"
     

import random

import numpy as np
import trimesh

from data_utils.gaussian_model import GaussianModel


class Mesh:
    def __init__(self, path, label):
        self.mesh = trimesh.load_mesh(path)
        self.label = label

    def __len__(self):
        return 1

    def sample_from_faces(self, num_points):
        areas = self.mesh.area_faces
        cumulative_areas = np.cumsum(areas)

        # Sample random points in the range of total surface area
        sampled_faces = np.searchsorted(cumulative_areas, np.random.random(num_points) * cumulative_areas[-1])

        # Get the vertices of the sampled faces
        sampled_triangles = self.mesh.triangles[sampled_faces]

        sampled_points = []
        for tri in sampled_triangles:
            r1 = random.random()
            r2 = random.random()
            sqrt_r1 = np.sqrt(r1)
            u = 1 - sqrt_r1
            v = r2 * sqrt_r1
            w = 1 - u - v
            point = u * tri[0] + v * tri[1] + w * tri[2]
            sampled_points.append(point)

        xyz = np.array(sampled_points)

        return GaussianModel.empty().with_xyz(xyz).with_label(self.label)
