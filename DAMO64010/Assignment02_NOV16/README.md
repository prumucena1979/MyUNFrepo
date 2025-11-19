# DAMO-640-10 Assignment 2: Machine Learning Analysis of Wholesale Customers Dataset

## 📋 Project Overview

This project applies both **supervised** and **unsupervised machine learning** techniques to the UCI Wholesale Customers Dataset. The analysis focuses on:

- **Classification**: Predicting customer channel (Horeca vs Retail) using ensemble methods and SVM
- **Clustering**: Identifying distinct customer segments based on spending patterns

## 🎯 Objectives

1. **Supervised Learning**: Build and evaluate classification models to predict customer channel
2. **Unsupervised Learning**: Perform customer segmentation using clustering algorithms
3. **Model Comparison**: Compare performance across different algorithms and hyperparameters
4. **Data Visualization**: Generate comprehensive plots and analysis reports

## 📊 Dataset Information

- **Source**: UCI Machine Learning Repository
- **Dataset ID**: 292 (Wholesale Customers)
- **Samples**: 440 customers
- **Features**: 6 spending categories + Region + Channel
- **Target Variable**: Channel (1=Horeca, 2=Retail → mapped to 0,1)

### Features:
- **Fresh**: Annual spending on fresh products
- **Milk**: Annual spending on milk products  
- **Grocery**: Annual spending on grocery products
- **Frozen**: Annual spending on frozen products
- **Detergents_Paper**: Annual spending on detergents and paper products
- **Delicassen**: Annual spending on delicatessen products
- **Region**: Customer region (categorical)
- **Channel**: Customer type (Horeca=0, Retail=1)

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab

### Install Dependencies
```bash
# Clone the repository
git clone <repository-url>
cd DAMO64010/Assignment02_NOV16

# Install required packages
pip install -r requirements.txt
```

### Required Libraries
- pandas >= 2.0.0
- numpy >= 1.24.0
- scikit-learn >= 1.3.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- ucimlrepo >= 0.0.3
- tabulate >= 0.9.0

## 📁 Project Structure

```
Assignment02_NOV16/
├── Notebook/
│   ├── Assignment2_DAMO64010_Notebook.ipynb  # Main analysis notebook
│   └── Assignment2_Draft.ipynb               # Draft version
├── requirements.txt                          # Python dependencies
├── .gitignore                               # Git ignore rules
└── README.md                                # This file
```

## 🚀 Usage

### Running the Analysis

1. **Open the main notebook**:
   ```bash
   jupyter notebook Notebook/Assignment2_DAMO64010_Notebook.ipynb
   ```

2. **Run all cells sequentially** to reproduce the complete analysis:
   - Data loading and preprocessing
   - Ensemble methods (Random Forest, Gradient Boosting)
   - Support Vector Machines (Linear & RBF kernels)
   - Clustering analysis (K-Means, DBSCAN)
   - Model evaluation and comparison

### Generated Outputs

The notebook generates several visualizations and saves them as PNG files:
- `spending_boxplots.png` - Feature distribution analysis
- `spending_correlation_heatmap.png` - Feature correlation matrix
- `gbm_confusion_matrix.png` - Best model confusion matrix
- `kmeans_pca_plot.png` - Customer cluster visualization
- `roc_curve_comparison.png` - Model ROC curve comparison

## 🔬 Analysis Methodology

### 1. Data Preprocessing
- **Standardization**: Applied StandardScaler to spending features
- **Encoding**: One-hot encoding for categorical Region variable
- **Train-Test Split**: 70/30 stratified split (random_state=42)

### 2. Supervised Learning

#### Ensemble Methods
- **Random Forest (Bagging)**: n_estimators = [50, 200]
- **Gradient Boosting**: n_estimators = [50, 200], learning_rate = 0.1
- **Evaluation**: 5-fold cross-validation + test set performance

#### Support Vector Machines  
- **Kernels**: Linear, RBF
- **Regularization**: C = [0.1, 1.0]
- **Evaluation**: 5-fold cross-validation accuracy comparison

### 3. Unsupervised Learning

#### K-Means Clustering
- **Clusters**: k = [2, 3, 4]
- **Evaluation**: Silhouette score optimization
- **Visualization**: PCA projection to 2D space

#### DBSCAN Clustering
- **Parameters**: eps = [0.5, 1.0], min_samples = 5
- **Evaluation**: Cluster count and silhouette score

## 📈 Key Results

### Model Performance Summary

| Algorithm | Configuration | CV Accuracy | Test Accuracy |
|-----------|--------------|-------------|---------------|
| **Gradient Boosting** | n_estimators=200 | **Best CV** | 93.18% |
| **Random Forest** | n_estimators=50 | 90.90% | 93.18% |
| **SVM RBF** | C=1.0 | 89.77% | **Best Test** |

### Clustering Results
- **Best K-Means**: k=2 with highest silhouette score
- **DBSCAN**: eps=1.0 produces meaningful clusters
- **Key Feature**: Detergents_Paper most discriminative (60%+ importance)

### Final Model Selection
**Gradient Boosting Machine (GBM)** with 200 estimators selected for deployment based on:
- Highest cross-validation stability
- Excellent test set performance
- Superior ROC AUC score
- Robust feature importance ranking

## 🎓 Academic Context

- **Course**: DAMO-640-10 (Fall 2025)
- **Institution**: University of Niagara Falls Canada
- **Assignment**: Module 5-7 (Ensemble Methods, SVM, Clustering)
- **Date**: November 3, 2025

## 📋 Assignment Requirements Met

✅ **Data Loading**: UCI repository integration with proper preprocessing  
✅ **Ensemble Methods**: Random Forest + Gradient Boosting with specified parameters  
✅ **SVM Analysis**: Linear/RBF kernels with C parameter comparison  
✅ **Clustering**: K-Means (k=2,3,4) + DBSCAN (eps=0.5,1.0)  
✅ **Evaluation**: 5-fold CV, test metrics, confusion matrix, ROC curves  
✅ **Visualization**: All required plots with proper formatting  
✅ **Documentation**: Comprehensive analysis and model selection justification  

## 🔄 Reproducibility

All analysis uses `random_state=42` for consistent results across runs. The notebook can be executed end-to-end to reproduce all results, plots, and model evaluations.

## 📝 Notes

- **Data Source**: Automatically downloaded via `ucimlrepo` library
- **Kernel Restart**: Required after package installation
- **Plot Display**: All visualizations show inline and save as PNG files
- **Performance**: Cross-validation results may vary slightly with different random seeds

## 🤝 Contributing

This is an academic assignment. For questions or clarifications, please refer to the course materials or contact the instructor.

---

**Author**: [Your Name]  
**Student ID**: [Your ID]  
**Course**: DAMO-640-10 (Fall 2025)  
**Institution**: University of Niagara Falls Canada