# breakhis-dataset-statistics-and-exploration-numbers
Statistical analysis and structural exploration of the BreakHis breast cancer histopathology dataset, including binary and multiclass classification subsets across multiple magnification levels.
# BreakHis Breast Cancer Dataset – Statistics & Exploration

## 📌 Overview
This repository provides a detailed statistical analysis and structural overview of a breast
cancer histopathology image dataset derived from the BreakHis collection. The purpose of this
repository is to facilitate dataset understanding and transparency before training any
machine learning or deep learning models.

The dataset supports both binary (benign vs. malignant) and multiclass (tumor subtype)
classification tasks and includes images acquired at multiple magnification levels.

---

## 🧬 Dataset Organization

The dataset is divided into two main subsets:

- **Binary classification**
- **Multiclass classification**

Each subset is further organized by magnification level (40X, 100X, 200X, and 400X).

---

## 1️⃣ Binary Classification (Benign vs. Malignant)

### 📊 Total Image Count
| Class       | Number of Images |
|------------|------------------|
| Benign     | 2,480 |
| Malignant  | 5,429 |
| **Total**  | **7,909** |

### 🔬 Distribution per Magnification

| Magnification | Benign | Malignant | Total |
|--------------|--------|-----------|-------|
| 40X | 625 | 1,370 | 1,995 |
| 100X | 644 | 1,437 | 2,081 |
| 200X | 623 | 1,390 | 2,013 |
| 400X | 588 | 1,232 | 1,820 |

**Observation:**  
The binary classification subset exhibits a noticeable class imbalance, with malignant
samples comprising approximately 69% of the data across all magnification levels.

---

## 2️⃣ Multiclass Classification (Tumor Subtypes)

### 🧪 Tumor Classes
The multiclass subset includes the following eight histopathological tumor subtypes:

- Adenosis  
- Ductal Carcinoma  
- Fibroadenoma  
- Lobular Carcinoma  
- Mucinous Carcinoma  
- Papillary Carcinoma  
- Phyllodes Tumor  
- Tubular Adenoma  

---

### 📊 Total Image Count per Tumor Type

| Tumor Type | Number of Images |
|-----------|------------------|
| Adenosis | 444 |
| Ductal Carcinoma | 3,451 |
| Fibroadenoma | 1,014 |
| Lobular Carcinoma | 626 |
| Mucinous Carcinoma | 792 |
| Papillary Carcinoma | 560 |
| Phyllodes Tumor | 453 |
| Tubular Adenoma | 569 |

---

### 🔬 Distribution per Magnification

#### 40X
| Class | Images |
|------|--------|
| Adenosis | 114 |
| Ductal Carcinoma | 864 |
| Fibroadenoma | 253 |
| Lobular Carcinoma | 156 |
| Mucinous Carcinoma | 205 |
| Papillary Carcinoma | 145 |
| Phyllodes Tumor | 109 |
| Tubular Adenoma | 149 |

#### 100X
| Class | Images |
|------|--------|
| Adenosis | 113 |
| Ductal Carcinoma | 903 |
| Fibroadenoma | 260 |
| Lobular Carcinoma | 170 |
| Mucinous Carcinoma | 222 |
| Papillary Carcinoma | 142 |
| Phyllodes Tumor | 121 |
| Tubular Adenoma | 150 |

#### 200X
| Class | Images |
|------|--------|
| Adenosis | 111 |
| Ductal Carcinoma | 896 |
| Fibroadenoma | 264 |
| Lobular Carcinoma | 163 |
| Mucinous Carcinoma | 196 |
| Papillary Carcinoma | 135 |
| Phyllodes Tumor | 108 |
| Tubular Adenoma | 140 |

#### 400X
| Class | Images |
|------|--------|
| Adenosis | 106 |
| Ductal Carcinoma | 788 |
| Fibroadenoma | 237 |
| Lobular Carcinoma | 137 |
| Mucinous Carcinoma | 169 |
| Papillary Carcinoma | 138 |
| Phyllodes Tumor | 115 |
| Tubular Adenoma | 130 |

---

## ⚠️ Key Observations

- The multiclass dataset is **highly imbalanced**, with ductal carcinoma dominating the class
  distribution.
- Rare classes such as adenosis and phyllodes tumor contain significantly fewer samples.
- This imbalance should be carefully addressed in downstream modeling through appropriate
  evaluation metrics and training strategies.

---

## 🎯 Scope of This Repository

This repository focuses exclusively on:
- Dataset structure documentation
- Class distribution analysis
- Data transparency and reproducibility

❌ No model training or evaluation is performed here.

---
## Data:
https://data.mendeley.com/datasets/jxwvdwhpc2/1
