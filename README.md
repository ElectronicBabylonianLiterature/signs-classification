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
| Class              | Accuracy  |
|--------------------|-----------|
| E_Neo-Assyrian     | 87.7%     |
| E_Neo-Babylonian   | 88.9%     |
| GAR_Neo-Assyrian   | 78.3%     |
| GAR_Neo-Babylonian | 94.4%     |
| KA_Neo-Assyrian    | 92.7%     |
| KA_Neo-Babylonian  | 83.2%     |
| KI_Neo-Assyrian    | 89.1%     |
| KI_Neo-Babylonian  | 94.6%     |
| MEŠ_Neo-Assyrian   | 88.9%     |
| MEŠ_Neo-Babylonian | 95.1%     |
| NI_Neo-Assyrian    | 88.7%     |
| NI_Neo-Babylonian  | 97.1%     |
| RU_Neo-Assyrian    | 95.9%     |
| RU_Neo-Babylonian  | 96.9%     |
| TA_Neo-Assyrian    | 85.2%     |
| TA_Neo-Babylonian  | 95.3%     |
| TI_Neo-Assyrian    | 89.1%     |
| TI_Neo-Babylonian  | 92.5%     |
| U₂_Neo-Assyrian    | 74.2%     |
| U₂_Neo-Babylonian  | 89.4%     |
| ŠU_Neo-Assyrian    | 79.3%     |
| ŠU_Neo-Babylonian  | 95.7%     |

* Overall accuracy: 0.8984737889847378
* Overall Top-2 accuracy:  0.9535501003265381
* Overall Top-3 accuracy:  0.9688122272491455





![Image Alt Text](imgs/heatmap.png)

