

# Based on research from:
# Jurski, K. (2024). Semantic 3D segmentation of 3D Gaussian Splats: Assessing existing
# point cloud segmentation techniques on semantic segmentation of synthetic 3D Gaussian
# Splats scenes. Bachelor's Thesis, Delft University of Technology.
# Extended implementation: "https://github.com/karol-202/direct-3dgs-segmentation"
     

from datasets.base_3dgs_dataset import Base3DGSDataset
from data_utils.scene_composer import compose_scene
from data_utils.utils import split_into_random_subsets


class Composed3DGSDataset(Base3DGSDataset):
    def __init__(self, model_paths, class2label, sampling, num_point=4096, extra_features=None):
        super().__init__(model_paths, class2label, sampling, num_point, extra_features)
        self.scenes = split_into_random_subsets(self.models, min_subset_size=3, max_subset_size=5)

    def __getitem__(self, idx):
        # Get the scene models (same as the original script)
        scene_models = self.scenes[idx]

        # Compose the scene
        composed_scene = compose_scene(scene_models)
        
        # Use get_data_for_model_with_uniform_sampling as in the original script
        selected_points, selected_labels, _ = self.get_data_for_model_with_uniform_sampling(composed_scene, self.extra_features)

        return selected_points, selected_labels

    def __len__(self):
        return len(self.scenes)


