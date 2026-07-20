# Sign Classification Task

# Repository Updates (2026)

This section summarizes recent extensions to the original sign-classification framework.

## Extension Code

All 2026 extension experiments are located in:

```text
sign_classification_extension/
```

This folder contains the notebooks and code for:

- ResNet18 / ResNet50 / ResNet101
- ConvNeXt Base
- ViT Base
- Swin Base
- Tablet-holdout evaluation
- Embedding and similarity analysis
- Tablet fragment matching retrieval
- Join retrieval experiments (Remaining)
- Occlusion bias analysis

## Extended Dataset

The original era-classification dataset has been extended using sign annotations from the Electronic Babylonian Library (EBL).

### Dataset Statistics

| Property | Value |
|-----------|-----------|
| Total sign crops | 133,791 |
| Sign classes | 482 |
| Minimum samples per class | 100 |
| Train split | 65% |
| Validation split | 15% |
| Test split | 20% |

---

## Models Evaluated

The extended framework evaluates both convolutional and transformer-based architectures.

### Convolutional Neural Networks

- ResNet18
- ResNet50
- ResNet101
- ConvNeXt Base

### Vision Transformers

- Vision Transformer (ViT Base)
- Swin Transformer (Swin Base)

All models were trained and evaluated using identical tablet-holdout splits to enable fair comparison.

---

## Experiments

The following experiments were conducted to evaluate sign recognition, embedding quality, tablet-level retrieval, period attribution, and model robustness.

### 1. Sign Classification

Metrics:

- Top-1 Accuracy
- Top-2 Accuracy
- Top-3 Accuracy
- Macro Precision
- Macro Recall
- Macro F1

### 2. Sign Similarity Analysis

Embedding-based similarity experiments were performed to investigate whether learned sign embeddings capture historical stylistic variation in addition to sign identity.

For each sign class, cosine similarity was measured between signs originating from:

1. The same tablet
2. Different tablets from the same period
3. Different tablets from different periods

Sign purity and tablet purity were additionally measured using the 10 nearest neighbors of each embedding.

### 3. Tablet Fragment Matching and Similarity Retrieval

Tablet representations were constructed from sign embeddings and used for nearest-neighbor retrieval.

## Tablet Fragment Matching (Tablet-Holdout)

To evaluate whether learned sign embeddings can associate fragments originating from the same tablet, each unseen test tablet was divided into multiple artificial fragments according to the spatial distribution of its signs.

A fragment-level representation was constructed by averaging the embeddings of the signs contained within each fragment. Each fragment was then used as a query against all remaining fragments.

Retrieval performance was measured using:

- Recall@1
- Recall@5
- Recall@10
- Mean Reciprocal Rank (MRR)

This experiment evaluates the potential of the learned representations for tablet-fragment association and future join-discovery applications.

| Model | Recall@1 | Recall@5 | Recall@10 | MRR |
|---------|---------:|---------:|---------:|---------:|
| ResNet18 | 0.3428 | 0.5096 | 0.5902 | 0.4262 |
| ResNet50 | **0.5424** | **0.7106** | **0.7862** | **0.6245** |
| ResNet101 | 0.4932 | 0.6771 | 0.7455 | 0.5788 |
| ConvNeXt Base | 0.3272 | 0.5004 | 0.5902 | 0.4153 |
| ViT Base | 0.4875 | 0.6543 | 0.7327 | 0.5703 |
| Swin Base | 0.4098 | 0.5823 | 0.6650 | 0.4961 |

### Key Findings

- **ResNet50** achieves the best fragment matching performance across all retrieval metrics.
- **ResNet101** and **ViT Base** also demonstrate strong tablet-fragment association capability.
- More than **78%** of ResNet50 queries retrieve a fragment from the same tablet within the top 10 results.
- The results indicate that learned sign embeddings retain information that allows different fragments from the same unseen tablet to be associated successfully.
- These findings suggest potential applicability to future tablet-fragment matching and join-discovery tasks.

### 5. Occlusion Bias Analysis

Quantitative occlusion experiments were used to assess whether predictions primarily depend on sign morphology or on image-specific artifacts.

Central and peripheral image regions were systematically masked, and the resulting change in classification confidence was measured separately for correct and incorrect predictions.

---

## Additional Outputs

The updated framework produces:

- Sign embeddings
- Tablet and fragment embeddings
- Similarity matrices
- Fragment-retrieval rankings
- Tablet-level period predictions
- Crop-level confidence predictions
- Period-voting details
- Accuracy results grouped by confident-crop count 
- Occlusion sensitivity analyses
- Grad-CAM visualizations

---

## Results

## Sign Classification Performance (Image-Level Split)

| Model | Top-1 | Top-2 | Top-3 | Precision | Recall | Macro-F1 |
|---------|---------|---------|---------|---------|---------|---------|
| ResNet18 | **0.8555** | 0.9267 | 0.9490 | **0.8712** | **0.8380** | **0.8495** |
| ResNet50 | 0.8345 | 0.9181 | 0.9429 | 0.8500 | 0.8151 | 0.8260 |
| ResNet101 | 0.8498 | 0.9249 | 0.9475 | 0.8619 | 0.8342 | 0.8424 |
| ConvNeXt Base | 0.8165 | 0.9057 | 0.9357 | 0.8349 | 0.7960 | 0.8065 |
| ViT Base | 0.8188 | 0.9121 | 0.9414 | 0.8365 | 0.7957 | 0.8048 |
| Swin Base | 0.8519 | **0.9329** | **0.9543** | 0.8575 | 0.8371 | 0.8409 |

### Best Performing Models

- **Best Top-1 Accuracy:** ResNet18 (85.55%)
- **Best Top-2 Accuracy:** Swin Base (93.29%)
- **Best Top-3 Accuracy:** Swin Base (95.43%)
- **Best Precision:** ResNet18 (87.12%)
- **Best Recall:** ResNet18 (83.80%)
- **Best Macro-F1:** ResNet18 (84.95%)

## Large-Scale Tablet Period Attribution

### Collection Filtering and DETR Processing

The large-scale processing pipeline initially examined **312,148 tablet fragments** from the EBL database.

The fragments were filtered as follows:

| Processing Category | Number of Fragments | Description |
|---|---:|---|
| Total fragments examined | 312,148 | Complete set of database fragments considered by the processing script |
| Skipped with existing annotations | 9,911 | Fragments excluded because sign-level annotations were already available |
| Skipped without photographs | 216,197 | Fragments excluded because no corresponding tablet image was available |
| Unannotated fragments processed with DETR | 86,040 | Fragments with available photographs and no existing sign annotations |

The collection totals satisfy:

```text
86,040 processed fragments
+ 9,911 fragments with annotations
+ 216,197 fragments without photographs
= 312,148 total fragments examined
```

Therefore, **312,148** represents the complete collection examined by the filtering pipeline, whereas only **86,040 unannotated fragments with available photographs** were passed through DETR.

DETR produced **1,279,146 automatically detected sign crops**. Among the 86,040 processed fragments, **77,442 fragments produced at least one crop prediction** and entered the subsequent tablet-level period-attribution analysis.

The remaining number of fragments was:

```text
86,040 - 77,442 = 8,598 fragments
```

These **8,598 fragments** did not contribute crop predictions to the downstream period-attribution file.

### Dataset Flow Summary

```text
312,148 total database fragments examined
│
├── 9,911 skipped: existing sign annotations
│
├── 216,197 skipped: no photograph available
│
└── 86,040 unannotated fragments processed with DETR
    │
    ├── 77,442 fragments produced crop predictions
    │   └── 1,279,146 automatically detected sign crops
    │
    └── 8,598 fragments produced no downstream crop predictions
```

For each classification model, only crop predictions satisfying the configured confidence and agreement criteria were retained. The retained crop predictions were then aggregated through tablet-level period voting.

Because confidence filtering was performed independently for each model, the number of retained crops and evaluated fragments differs slightly across architectures.

Results are therefore reported in terms of:

- Crop-prediction retention
- Fragment evaluation coverage
- Overall tablet-level period-attribution accuracy
- Accuracy grouped by the number of confident crops

### Period-Attribution Pipeline

The large-scale period-attribution pipeline consists of the following steps:

1. Detect candidate sign regions from each tablet-fragment image.
2. Classify each detected crop using a tablet-holdout-trained sign classifier.
3. Remove crop predictions that do not satisfy the confidence and agreement thresholds.
4. Obtain the historical-period prediction associated with each retained sign crop.
5. Aggregate sign-level period predictions using majority voting.
6. Compare the predicted tablet period with the available period metadata.

### Inference and Evaluation Settings

The large-scale period-attribution experiment used the following thresholds and metadata source:

| Component | Setting |
|---|---|
| DETR detection threshold | Detection confidence $\geq 0.60$ |
| Sign-classification threshold | Crop-prediction confidence $\geq 0.50$ |
| Reference period | MongoDB `script.period` field |

Only DETR detections with confidence scores of at least **0.60** were retained as candidate sign crops. Each retained crop was then classified using a tablet-holdout-trained sign classifier, and crop predictions with confidence scores below **0.50** were excluded from tablet-level voting.

The predicted tablet period was compared with the reference period stored in the MongoDB `script.period` field.

---

### Crop-Prediction Retention and Fragment Coverage

| Model | Total Crop Predictions | Crop Predictions Used | Crop Usage (%) | Fragments Evaluated | Coverage (%) | Without Confident Crops |
|---|---:|---:|---:|---:|---:|---:|
| ResNet18 Tablet Holdout | 1,279,146 | 624,798 | 48.84 | 70,463 | 90.99 | 6,979 |
| ResNet50 Tablet Holdout | 1,279,146 | 635,891 | 49.71 | 69,789 | 90.12 | 7,653 |
| ResNet101 Tablet Holdout | 1,279,146 | 637,601 | 49.85 | 70,064 | 90.47 | 7,378 |
| ConvNeXt Base | 1,279,146 | 730,904 | 57.14 | 71,686 | 92.57 | 5,756 |
| ViT Base | 1,279,146 | 670,884 | 52.45 | 70,541 | 91.09 | 6,901 |
| Swin Base | 1,279,146 | 835,693 | **65.33** | 73,687 | **95.15** | **3,755** |

Crop-prediction usage is calculated as:

$$
\text{Crop Usage (\%)} =
\frac{\text{Crop Predictions Used}}
{\text{Total Crop Predictions}}
\times 100
$$

Fragment evaluation coverage is calculated as:

$$
\text{Coverage (\%)} =
\frac{\text{Fragments Evaluated}}
{\text{Fragments Before Thresholding}}
\times 100
$$

#### Key Findings

- **Swin Base** retains the largest proportion of crop predictions, using **65.33%** of all detected crops.
- Swin Base evaluates **73,687 fragments**, corresponding to the highest coverage of **95.15%**.
- **ConvNeXt Base** provides the second-highest fragment coverage at **92.57%**.
- **ResNet50** evaluates the fewest fragments, with a coverage of **90.12%**.
- The lower coverage of ResNet50 should be considered together with its higher period-attribution accuracy, since it produces predictions for a slightly smaller and potentially more confidently filtered subset of fragments.

---

### Overall Tablet-Level Period-Attribution Performance

| Model | Fragments Evaluated | Correct | Incorrect | Accuracy (%) |
|---|---:|---:|---:|---:|
| ResNet18 Tablet Holdout | 70,463 | 51,459 | 19,004 | 73.03 |
| ResNet50 Tablet Holdout | 69,789 | 52,778 | 17,011 | **75.63** |
| ResNet101 Tablet Holdout | 70,064 | 49,964 | 20,100 | 71.31 |
| ConvNeXt Base | 71,686 | 52,363 | 19,323 | 73.04 |
| ViT Base | 70,541 | 50,523 | 20,018 | 71.62 |
| Swin Base | 73,687 | 53,885 | 19,802 | 73.13 |

Tablet-level period-attribution accuracy is calculated as:

$$
\text{Tablet Accuracy (\%)} =
\frac{\text{Correct Period Predictions}}
{\text{Fragments Evaluated}}
\times 100
$$

#### Key Findings

- **ResNet50** achieves the highest overall tablet-level period-attribution accuracy of **75.63%**.
- ResNet50 correctly predicts the periods of **52,778 out of 69,789 evaluated fragments**.
- **Swin Base** achieves an accuracy of **73.13%** while providing the highest fragment coverage.
- **ConvNeXt Base** and **ResNet18** obtain similar accuracies of **73.04%** and **73.03%**, respectively.
- **ResNet101** and **ViT Base** obtain the lowest overall accuracies, at **71.31%** and **71.62%**, respectively.
- These results reveal a trade-off between prediction accuracy and collection coverage:
  - ResNet50 provides the highest period-attribution accuracy.
  - Swin Base provides predictions for the largest proportion of the collection.

---

### Accuracy by Number of Confident Crops

To investigate how the amount of sign-level evidence affects tablet-level period attribution, fragments were divided into four groups according to the number of confident crop predictions available for voting:

- 1 confident crop
- 2–4 confident crops
- 5–9 confident crops
- 10 or more confident crops

The `Share (%)` column indicates the percentage of all evaluated fragments for a model that belongs to the corresponding crop-count group.

| Model | Crop Group | Fragments | Correct | Incorrect | Accuracy (%) | Share (%) |
|---|---|---:|---:|---:|---:|---:|
| ResNet18 Tablet Holdout | 1 confident crop | 9,004 | 4,858 | 4,146 | 53.95 | 12.78 |
| ResNet18 Tablet Holdout | 2–4 confident crops | 19,537 | 13,113 | 6,424 | 67.12 | 27.73 |
| ResNet18 Tablet Holdout | 5–9 confident crops | 19,640 | 15,454 | 4,186 | 78.69 | 27.87 |
| ResNet18 Tablet Holdout | 10 or more confident crops | 22,282 | 18,034 | 4,248 | 80.94 | 31.62 |
| ResNet50 Tablet Holdout | 1 confident crop | 9,001 | 5,155 | 3,846 | **57.27** | 12.90 |
| ResNet50 Tablet Holdout | 2–4 confident crops | 18,778 | 13,216 | 5,562 | **70.38** | 26.91 |
| ResNet50 Tablet Holdout | 5–9 confident crops | 19,017 | 15,518 | 3,499 | **81.60** | 27.25 |
| ResNet50 Tablet Holdout | 10 or more confident crops | 22,993 | 18,889 | 4,104 | **82.15** | 32.95 |
| ResNet101 Tablet Holdout | 1 confident crop | 9,000 | 4,964 | 4,036 | 55.16 | 12.85 |
| ResNet101 Tablet Holdout | 2–4 confident crops | 18,968 | 12,584 | 6,384 | 66.34 | 27.07 |
| ResNet101 Tablet Holdout | 5–9 confident crops | 19,278 | 14,536 | 4,742 | 75.40 | 27.51 |
| ResNet101 Tablet Holdout | 10 or more confident crops | 22,818 | 17,880 | 4,938 | 78.36 | 32.57 |
| ConvNeXt Base | 1 confident crop | 7,986 | 4,505 | 3,481 | 56.41 | 11.14 |
| ConvNeXt Base | 2–4 confident crops | 17,794 | 11,914 | 5,880 | 66.96 | 24.82 |
| ConvNeXt Base | 5–9 confident crops | 19,013 | 14,664 | 4,349 | 77.13 | 26.52 |
| ConvNeXt Base | 10 or more confident crops | 26,893 | 21,280 | 5,613 | 79.13 | 37.51 |
| ViT Base | 1 confident crop | 8,610 | 4,686 | 3,924 | 54.43 | 12.21 |
| ViT Base | 2–4 confident crops | 18,553 | 12,174 | 6,379 | 65.62 | 26.30 |
| ViT Base | 5–9 confident crops | 19,164 | 14,480 | 4,684 | 75.56 | 27.17 |
| ViT Base | 10 or more confident crops | 24,214 | 19,183 | 5,031 | 79.22 | 34.33 |
| Swin Base | 1 confident crop | 7,260 | 3,951 | 3,309 | 54.42 | 9.85 |
| Swin Base | 2–4 confident crops | 16,617 | 10,907 | 5,710 | 65.64 | 22.55 |
| Swin Base | 5–9 confident crops | 19,228 | 14,658 | 4,570 | 76.23 | 26.09 |
| Swin Base | 10 or more confident crops | 30,582 | 24,369 | 6,213 | 79.68 | **41.50** |

Accuracy within each crop-count group is calculated as:

$$
\text{Group Accuracy (\%)} =
\frac{\text{Correct Predictions in Group}}
{\text{Fragments in Group}}
\times 100
$$

The share of evaluated fragments is calculated as:

$$
\text{Share (\%)} =
\frac{\text{Fragments in Crop Group}}
{\text{Total Evaluated Fragments}}
\times 100
$$

---

### Crop-Count Accuracy Summary

| Model | 1 Crop | 2–4 Crops | 5–9 Crops | 10+ Crops |
|---|---:|---:|---:|---:|
| ResNet18 | 53.95 | 67.12 | 78.69 | 80.94 |
| ResNet50 | **57.27** | **70.38** | **81.60** | **82.15** |
| ResNet101 | 55.16 | 66.34 | 75.40 | 78.36 |
| ConvNeXt Base | 56.41 | 66.96 | 77.13 | 79.13 |
| ViT Base | 54.43 | 65.62 | 75.56 | 79.22 |
| Swin Base | 54.42 | 65.64 | 76.23 | 79.68 |

#### Key Findings

- Period-attribution accuracy consistently increases as more confident sign crops become available.
- Fragments supported by only one confident crop achieve approximately **54–57% accuracy**.
- Fragments supported by at least 10 confident crops achieve approximately **78–82% accuracy**.
- **ResNet50 achieves the highest accuracy in every crop-count category.**
- ResNet50 improves from **57.27%** with one confident crop to **82.15%** with at least 10 confident crops.
- ResNet50 achieves **81.60%** accuracy with 5–9 confident crops and **82.15%** with at least 10 crops.
- The relatively small improvement between the final two groups suggests that ResNet50 performance begins to saturate once approximately five confident sign predictions are available.
- **Swin Base** places **41.50%** of its evaluated fragments in the 10-or-more-crop group, the largest proportion among all models.
- **ConvNeXt Base** also provides high confident-crop coverage, with **37.51%** of its evaluated fragments containing at least 10 confident predictions.
- Increasing model depth from ResNet50 to ResNet101 does not improve tablet-level period attribution.
- Transformer-based architectures provide broader confident-crop coverage in some cases but do not outperform ResNet50 in period-attribution accuracy.

---

### Interpretation

The results demonstrate that tablet-level period attribution benefits substantially from aggregating evidence across multiple recognized signs.

Predictions based on a single confident crop are comparatively unreliable because one incorrect or ambiguous sign directly determines the tablet-level result. As the number of confident crops increases, the influence of individual sign-classification errors is reduced through majority voting.

ResNet50 provides the strongest balance between sign-level reliability and tablet-level voting performance. It achieves:

- The highest overall tablet-level accuracy
- The highest accuracy in every crop-count group
- More than 81% accuracy when at least five confident crops are available

Swin Base provides the greatest collection coverage by retaining more crop predictions and evaluating more fragments. However, its tablet-level period-attribution accuracy remains below that of ResNet50.

These results indicate that the number of confident detected signs can serve as a practical reliability indicator for tablet-level period attribution. Predictions supported by at least five confident crops are substantially more reliable than predictions based on only one to four crops.

## Embedding Quality (k = 10 Nearest Neighbors)

- **Sign Purity** measures how often neighboring embeddings belong to the same sign class.
- **Tablet Purity** measures how often neighboring embeddings originate from the same tablet.

Higher sign purity indicates better sign discrimination, while lower tablet purity suggests reduced reliance on tablet-specific characteristics.

| Model | Embedding Dim. | Sign Purity | Tablet Purity |
|---------|---------|---------|---------|
| ResNet18 | 512 | 0.8649 | 0.0689 |
| ResNet50 | 2048 | 0.8051 | 0.1006 |
| ResNet101 | 2048 | 0.8350 | 0.0967 |
| ConvNeXt Base | 1024 | 0.8829 | **0.0580** |
| ViT Base | 768 | 0.8621 | 0.0819 |
| Swin Base | 1024 | **0.8860** | 0.0771 |

### Key Findings

- **Swin Base** achieves the highest sign purity (**88.60%**), indicating the strongest sign-level clustering in the embedding space.
- **ConvNeXt Base** achieves the lowest tablet purity (**5.80%**), suggesting the least dependence on tablet-specific characteristics.
- Both **ConvNeXt Base** and **Swin Base** produce highly discriminative embeddings while maintaining low tablet-level bias.
- All architectures achieve substantially higher sign purity than tablet purity, indicating that embeddings primarily capture sign identity rather than tablet identity.

## Same-Sign Similarity by Tablet and Period (Image-Level Split)

Average cosine similarity between signs belonging to the same sign class.

| Model | Same Tablet | Same Period Different Tablet | Different Period Different Tablet | Tablet Effect | Period Effect |
|---------|---------|---------|---------|---------|---------|
| ResNet18 | 0.8264 | 0.7048 | 0.4708 | 0.1216 | 0.2341 |
| ResNet50 | 0.8031 | 0.6642 | 0.4812 | 0.1389 | 0.1830 |
| ResNet101 | 0.7504 | 0.5816 | 0.3529 | 0.1687 | 0.2287 |
| ConvNeXt Base | **0.9015** | **0.7347** | 0.2139 | 0.1668 | **0.5208** |
| ViT Base | 0.7653 | 0.5702 | 0.1889 | 0.1950 | 0.3813 |
| Swin Base | 0.8495 | 0.6495 | **0.1772** | **0.1999** | 0.4724 |

### Key Findings

```text
  Same Tablet > Same Period > Different Period
  ```

- **ConvNeXt Base** achieves the highest same-tablet similarity (**0.9015**) and the strongest period separation (**0.5208**).

- **Swin Base** achieves the lowest different-period similarity (**0.1772**), indicating strong period discrimination.

- These results suggest that the learned embeddings capture both sign identity and period-specific stylistic variation.

## Sign Classification Performance (Tablet-Holdout)

The tablet-holdout protocol ensures that signs originating from the same tablet never appear in both training and testing sets, providing a realistic evaluation of model generalization to previously unseen tablets.

| Model | Top-1 | Top-2 | Top-3 | Precision | Recall | Macro-F1 |
|---------|---------|---------|---------|---------|---------|---------|
| ResNet18 | 0.7371 | 0.8426 | 0.8852 | 0.7604 | 0.7203 | 0.7169 |
| ResNet50 | 0.7412 | 0.8524 | 0.8915 | **0.7700** | 0.7258 | 0.7228 |
| ResNet101 | 0.7465 | 0.8528 | 0.8903 | 0.7696 | 0.7375 | 0.7280 |
| ConvNeXt Base | **0.7572** | 0.8679 | **0.9102** | 0.7682 | **0.7413** | **0.7296** |
| ViT Base | 0.7054 | 0.8205 | 0.8671 | 0.7224 | 0.6911 | 0.6773 |
| Swin Base | 0.7465 | 0.8556 | 0.8985 | 0.7564 | 0.7307 | 0.7217 |

### Key Findings

- **ConvNeXt Base** achieves the best overall tablet-holdout performance with:
  - Highest Top-1 Accuracy (**75.72%**)
  - Highest Top-3 Accuracy (**91.02%**)
  - Highest Recall (**74.13%**)
  - Highest Macro-F1 (**72.96%**)

- **ResNet50** achieves the highest Precision (**77.00%**).

- **Swin Base** performs competitively with ResNet101 despite using a transformer-based architecture.

- **ViT Base** shows the largest performance drop under tablet-holdout evaluation, suggesting lower robustness to unseen tablet styles compared to ConvNeXt, Swin, and ResNet architectures.

- The relatively small gap between ConvNeXt Base and ResNet101 indicates that both CNN-based architectures generalize well to previously unseen tablets.

## Same-Sign Similarity by Tablet and Period (Tablet-Holdout)

| Model | Same Tablet | Same Period Different Tablet | Different Period Different Tablet | Tablet Effect | Period Effect |
|---------|---------|---------|---------|---------|---------|
| ResNet18 | **0.7860** | **0.6955** | 0.4967 | 0.0905 | 0.1988 |
| ResNet50 | 0.7730 | 0.6444 | 0.4288 | 0.1285 | 0.2157 |
| ResNet101 | 0.7607 | 0.6325 | 0.4143 | 0.1282 | 0.2182 |
| ConvNeXt Base | 0.7598 | 0.6442 | 0.2649 | 0.1155 | 0.3794 |
| ViT Base | 0.6603 | 0.5304 | **0.1858** | **0.1299** | 0.3446 |
| Swin Base | 0.7366 | 0.6281 | 0.2065 | 0.1085 | **0.4216** |

### Key Findings

- For all models, same-sign similarity follows:

  ```text
  Same Tablet > Same Period > Different Period
  ```

- **ResNet18** achieves the highest same-tablet similarity (**0.7860**) and same-period similarity (**0.6955**).

- **ViT Base** achieves the lowest different-period similarity (**0.1858**), indicating strong separation between periods.

- **Swin Base** achieves the largest period separation (**0.4216**), suggesting the strongest sensitivity to period-specific stylistic variation.

- These results indicate that the learned embeddings capture both sign identity and historical stylistic differences, even when evaluated on previously unseen tablets.

## Quantitative Occlusion Bias Analysis

Occlusion experiments were performed by systematically masking image regions and measuring confidence changes. Models that rely primarily on sign morphology should exhibit larger confidence drops when central sign regions are occluded than when border regions are masked.

### Occlusion Summary

| Model | Correct Mean Drop | Wrong Mean Drop | Center Drop (Wrong) | Border Drop (Wrong) |
|---------|---------|---------|---------|---------|
| ResNet18 | 0.0009 | 0.0121 | 0.0207 | 0.0042 |
| ResNet50 | 0.0023 | 0.0136 | 0.0209 | 0.0069 |
| ResNet101 | 0.0014 | 0.0160 | 0.0246 | 0.0080 |
| ConvNeXt Base | 0.0015 | **0.0079** | 0.0127 | 0.0034 |
| ViT Base | 0.0047 | 0.0168 | 0.0179 | 0.0159 |
| Swin Base | 0.0031 | 0.0129 | 0.0188 | 0.0075 |

### Key Findings

- Correct predictions are highly stable under local occlusions for all architectures.
- Wrong predictions are substantially more sensitive to occlusions.
- For CNN-based models (ResNet and ConvNeXt), occluding central image regions consistently causes larger confidence drops than occluding border regions.
- ConvNeXt Base exhibits the smallest confidence degradation under occlusion, suggesting particularly robust feature representations.
- The stronger effect of central occlusions indicates that models primarily rely on sign morphology rather than peripheral image artifacts.

### Interpretation

The observed behavior suggests that the learned representations are driven mainly by sign structure and shape rather than tablet-specific backgrounds, illumination patterns, or image acquisition artifacts.

---

## Future Work

Planned extensions include:

- Automatic join discovery

---

# Original Implementation

The code and experiments below this section correspond to the original era-classification framework presented in:

> Yugay, V., Paliwal, K., Cobanoglu, Y., Sáenz, L., Gogokhia, E., Gordin, S., & Jiménez, E. (2024). *Stylistic classification of cuneiform signs using convolutional neural networks*. **IT – Information Technology**, 66(1), 15–27. De Gruyter Oldenbourg.

```bibtex
@article{yugay2024stylistic,
  title={Stylistic classification of cuneiform signs using convolutional neural networks},
  author={Yugay, Vasiliy and Paliwal, Kartik and Cobanoglu, Yunus and Sáenz, Luis and Gogokhia, Ekaterine and Gordin, Shai and Jiménez, Enrique},
  journal={IT-Information Technology},
  volume={66},
  number={1},
  pages={15--27},
  year={2024},
  publisher={De Gruyter Oldenbourg}
}
```

The original code reproduces the experiments described in the above publication, while the preceding sections document the 2026 extensions, including expanded sign classification, tablet-holdout evaluation, embedding analysis, fragment retrieval, and additional experiments.

# Original Era Classification Experiments

## Overview

This project focuses on building and training a machine-learning model to classify signs. The goal is to correctly identify and classify the era of signs based on their visual features. The project involves data preprocessing, model selection, training, and evaluation.
The results are presented [here](https://github.com/ElectronicBabylonianLiterature/signs-classification/blob/main/resnet101_full_data.ipynb)


## Table of Contents

- [Dataset](#dataset)
- [Model Selection](#model-selection)
- [Training](#training)
- [Evaluation](#evaluation)


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

