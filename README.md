# Sign Classification Task

## Overview

This project focuses on building and training a machine-learning model to classify signs. The goal is to correctly identify and classify the era of signs based on their visual features. The project involves data preprocessing, model selection, training, and evaluation.
The results are presented [here](https://github.com/ElectronicBabylonianLiterature/signs-classification/blob/main/resnet101_full_data.ipynb)


## Table of Contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Model Selection](#model-selection)
- [Training](#training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Dataset and Data Retrieval

To retrieve the cropped images of signs in EBL database, please use this [script](data_retrieval/get_signs.py). It will automatically create folder data with signs, specified in `sign_filter`. 
You need to pass your database connection string to the script's arguments.
For retrieving images from [Late Babylonian signs website](https://labasi.acdh.oeaw.ac.at/) was used  this [script](https://github.com/ElectronicBabylonianLiterature/signs-classification/blob/main/data_retrieval/labasi_data/crawl_labasi_page.py).
Also, this  [CDP](https://github.com/urschrei/CDP/tree/master/static/img/instance) dataset was used. This [script](https://github.com/ElectronicBabylonianLiterature/signs-classification/blob/main/data_retrieval/get_era.py) retrieve era of the image using this [Excel file](https://github.com/urschrei/CDP/blob/master/csvs/corrected_instance.xlsx) and EBL database.

* Train Dataset - 14,528 Images
* Validation Dataset - 3,365 Images 
* Test Dataset - 4,459 Images
  
Full dataset can be downloaded [here](https://drive.google.com/file/d/1xsEBllly6B-CG4V9P8zOUtX7K3fl0Iwe/view?usp=drive_link)

## Model Selection

[Resnet101](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet101.html).

## Training
* Optimizer - Adam
* Loss - Cross Entropy
* 50 epochs with Early Stopping

## Evaluation
| **Sign** | **Neo-Assyrian** | **Neo-Babylonian** |
|----------|------------------|--------------------|
| `Non-diagnostic' Signs | | |
| an | 67.9% | 91.4% |
| a | 62.7% | 93.8% |
| aš | 65.2% | 88.1% |
| bad | 94.5% | 87.3% |
| diš | 77.8% | 90.0% |
| giš | 56.8% | 68.9% |
| igi | 83.0% | 85.0% |
| ma | 80.0% | 73.2% |
| mu | 75.7% | 91.1% |
| na | 71.0% | 76.8% |
| nu | 41.7% | 85.6% |
| ud | 52.8% | 85.5% |
| šu2 | 65.7% | 75.0% |
| **Average** | 68.83% | 83.97% |
| `Diagnostic' Signs | | |
| e | 82.1% | 80.5% |
| gar | 80.4% | 71.5% |
| i | 86.2% | 93.0% |
| ka | 90.3% | 83.8% |
| ki | 78.3% | 82.6% |
| meš | 57.1% | 89.8% |
| ni | 85.0% | 80.4% |
| ru | 92.9% | 67.6% |
| ta | 84.4% | 92.0% |
| ti | 64.5% | 75.9% |
| u2 | 81.6% | 89.6% |
| šu | 80.6% | 77.1% |
| **Average** | 80.28% | 81.98% |


|           | Top 1 | Top 2 | Top 3 |
|-----------|-------|-------|-------|
| ResNet101 | 0.82  | 0.90  | 0.94  |



![Image Alt Text](imgs/heatmap.png)

