

# @brief Train a semantic segmentation model for 3D Gaussian Splats
# Modified from :-
# Yanx27 (2019). PointNet_Pointnet2_pytorch [online].
# [Accessed 2024]. Available from: "https://github.com/yanx27/Pointnet_Pointnet2_pytorch"
# Based on research from:
# Jurski, K. (2024). Semantic 3D segmentation of 3D Gaussian Splats: Assessing existing
# point cloud segmentation techniques on semantic segmentation of synthetic 3D Gaussian
# Splats scenes. Bachelor's Thesis, Delft University of Technology.
# Extended implementation: "https://github.com/karol-202/direct-3dgs-segmentation"
     

import os
from datasets.base_dataset import BaseDataset
from data_utils.gaussian_model import GaussianModel

class Base3DGSDataset(BaseDataset):
    def __init__(self, model_paths, class2label, sampling, num_point=4096, extra_features=None):
        self.sampling = sampling
        self.extra_features = extra_features or []
        super().__init__(model_paths, class2label, num_point)

    def load_model(self, model_path, label):
        extra_feature_names = [f if isinstance(f, str) else f.name for f in self.extra_features]

        model = (GaussianModel.load_from(model_path, extra_feature_names)
                 .normalized()
                 .with_label(label))

        return model.fps_sampled(self.num_point) if self.sampling == 'fps' else model

    def get_data_for_model_with_uniform_sampling(self, model, extra_features):
        """Resample model points uniformly before processing."""
        resampled_model = model.uniformly_sampled(self.num_point)
        return self.get_data_for_model(resampled_model, extra_features)

    @property
    def get_channels_count(self):
        return self.get_channels_count_for_features(self.extra_features)
