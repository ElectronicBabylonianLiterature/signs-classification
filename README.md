# Sign Classification Task

## Overview

This project focuses on building and training a machine-learning model to classify signs. The goal is to correctly identify and classify the era of signs based on their visual features. The project involves data preprocessing, model selection, training, and evaluation.


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
For retrieving images from [Late Babylonian signs website](https://labasi.acdh.oeaw.ac.at/) was used  this [script](https://github.com/ElectronicBabylonianLiterature/signs-classification/blob/main/data_retrieval/labasi_data/crawl_labasi_page.py). 'KA', 'RU', 'ŠU' signs from that dataset were used in training
For model testing purposes [CDP](https://github.com/urschrei/CDP/tree/master/static/img/instance) dataset  and 10% of EBL data were used. This [script](https://github.com/ElectronicBabylonianLiterature/signs-classification/blob/main/data_retrieval/get_era.py) retrieve era of the image using this [Excel file](https://github.com/urschrei/CDP/blob/master/csvs/corrected_instance.xlsx) and EBL database.

* Train Dataset - 8882 Images
* Test Dataset - 1507 Images


## Model Selection

[Resnet101](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet101.html).

## Training
* Optimizer - Adam
* Loss - Cross Entropy
* 50 epochs with Early Stopping

## Evaluation

| Class               | Accuracy   |
|---------------------|------------|
| E_Neo-Assyrian      | 85.1%      |
| E_Neo-Babylonian    | 83.7%      |
| GAR_Neo-Assyrian    | 79.7%      |
| GAR_Neo-Babylonian  | 94.3%      |
| KA_Neo-Assyrian     | 93.2%      |
| KA_Neo-Babylonian   | 77.3%      |
| KI_Neo-Assyrian     | 87.0%      |
| KI_Neo-Babylonian   | 94.0%      |
| MEŠ_Neo-Assyrian    | 85.7%      |
| MEŠ_Neo-Babylonian  | 87.5%      |
| NI_Neo-Assyrian     | 86.3%      |
| NI_Neo-Babylonian   | 96.3%      |
| RU_Neo-Assyrian     | 94.7%      |
| RU_Neo-Babylonian   | 95.5%      |
| TA_Neo-Assyrian     | 81.4%      |
| TA_Neo-Babylonian   | 92.5%      |
| TI_Neo-Assyrian     | 86.7%      |
| TI_Neo-Babylonian   | 87.9%      |
| U₂_Neo-Assyrian     | 68.5%      |
| U₂_Neo-Babylonian   | 87.0%      |
| ŠU_Neo-Assyrian     | 69.2%      |
| ŠU_Neo-Babylonian   | 95.7%      |

* Overall accuracy: 0.87248322147651
Overall Top-2 accuracy:  0.9395973086357117
Overall Top-3 accuracy:  0.9588926434516907




![Image Alt Text](imgs/heatmap.png)

