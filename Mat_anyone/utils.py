import os
import cv2
import random
import numpy as np

import torch
import torchvision

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
VIDEO_EXTENSIONS = ('.mp4', '.mov', '.avi', '.MP4', '.MOV', '.AVI')

def read_frame_from_videos(frame_root):
    if frame_root.endswith(VIDEO_EXTENSIONS):  # Video file path
        video_name = os.path.basename(frame_root)[:-4]
        frames, _, info = torchvision.io.read_video(
            filename=frame_root, 
            pts_unit='sec', 
            output_format='TCHW'  # [T, C, H, W]
        )
        fps = info['video_fps']
    elif os.path.isdir(frame_root):  # Image sequence folder
        video_name = os.path.basename(os.path.normpath(frame_root))
        frame_paths = sorted([
            os.path.join(frame_root, f) 
            for f in os.listdir(frame_root) 
            if f.endswith(IMAGE_EXTENSIONS)
        ])
        frames = []
        for fr in frame_paths:
            img = cv2.imread(fr)
            if img is None:
                continue
            img = img[..., [2, 1, 0]]  # BGR to RGB
            frames.append(img)
        if len(frames) == 0:
            raise ValueError(f"No valid image frames found in {frame_root}")
        fps = 24  # default FPS for image sequences
        frames = torch.Tensor(np.array(frames)).permute(0, 3, 1, 2).contiguous()  # [T, C, H, W]
    else:
        raise ValueError(f"Unsupported input: {frame_root}")

    length = frames.shape[0]
    return frames, fps, length, video_name

def get_video_paths(input_root):
    video_paths = []
    for root, _, files in os.walk(input_root):
        for file in files:
            if file.lower().endswith(VIDEO_EXTENSIONS):
                video_paths.append(os.path.join(root, file))
    return sorted(video_paths)

def str_to_list(value):
    return list(map(int, value.split(',')))

def gen_dilate(alpha, min_kernel_size, max_kernel_size): 
    kernel_size = random.randint(min_kernel_size, max_kernel_size)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    fg_and_unknown = np.array(np.not_equal(alpha, 0).astype(np.float32))
    dilate = cv2.dilate(fg_and_unknown, kernel, iterations=1) * 255
    return dilate.astype(np.float32)

def gen_erosion(alpha, min_kernel_size, max_kernel_size): 
    kernel_size = random.randint(min_kernel_size, max_kernel_size)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    fg = np.array(np.equal(alpha, 255).astype(np.float32))
    erode = cv2.erode(fg, kernel, iterations=1) * 255
    return erode.astype(np.float32)
