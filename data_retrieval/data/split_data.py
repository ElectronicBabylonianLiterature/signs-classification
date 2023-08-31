from data import base_dataset
from sklearn.model_selection import train_test_split
import numpy as np
from torch.utils.data import Subset
import torch 

def split_data(annotations_path, data_path, transformations):
    data = base_dataset.Signs_Dataset(annotations_path, data_path ,transformations)
    targets = data.img_labels.to_numpy()
    train_indices, test_val_indices = train_test_split(np.arange(targets.shape[0]), stratify=targets[:,1], train_size=0.6, random_state=21)
    test_val_targets = targets[test_val_indices]
    val_indices, test_indices = train_test_split(test_val_indices, stratify=test_val_targets[:,1], train_size=0.5, random_state=21)
    train = Subset(data, indices=train_indices)
    val = Subset(data, indices=val_indices)
    test = Subset(data, indices=test_indices)
    
    return train, val, test
def get_mean_std(annotations_path, data_path, transformations):
    data = base_dataset.Signs_Dataset(annotations_path, data_path ,transformations)
    num_pixels = 0
    mean = 0.0
    std = 0.0
    for images, label in data:
        num_channels, height, width = images.shape
        num_pixels += height * width
        mean += torch.mean(images.float(), dim = [1,2]).sum()
        std += torch.std(images.float(), dim = [1,2]).sum()

    mean /= num_pixels
    std /= num_pixels
    del data
    return mean, std