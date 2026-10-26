# 🤖 Machine Learning — Fundamentals, Algorithms & Projects

Welcome to my **Machine Learning Learning and Projects** repository!

This folder documents my journey of learning Machine Learning (ML) using Python, statistics, data preprocessing, feature engineering, and Scikit-learn.

The goal is to understand how machine learning algorithms learn patterns from data, how to evaluate their performance correctly, and how to build reliable models that solve real-world problems.

This section progresses from foundational concepts to supervised learning, unsupervised learning, model optimization, explainability, and inference.

---

## 🎯 Learning Objectives

By completing this section, I aim to learn how to:

- Understand the fundamentals of machine learning and its applications.
- Apply probability and statistics to machine learning problems.
- Prepare datasets for model training.
- Handle missing values, categorical variables, and outliers.
- Perform feature engineering and feature selection.
- Split data into training, validation, and test sets correctly.
- Build regression and classification models.
- Apply clustering and dimensionality reduction.
- Evaluate models using suitable performance metrics.
- Use cross-validation and hyperparameter tuning.
- Build reusable Scikit-learn pipelines.
- Handle imbalanced datasets.
- Explain model predictions and limitations.
- Save trained models and use them for inference.
- Build complete, documented machine learning projects.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical computation |
| Pandas | Data preparation and analysis |
| Matplotlib | Visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning algorithms and workflows |
| SciPy | Scientific and statistical computing |
| Jupyter Notebook | Interactive experimentation |
| Joblib | Saving and loading suitable Python model objects |
| Git and GitHub | Version control and portfolio development |

**Recommended starting point:** Use Scikit-learn with small, well-understood datasets before moving to larger or more complex problems.

---

## 📂 Repository Structure

```text
07_ML/
│
├── README.md
│
├── 01_Statistics_Probability/
│   ├── README.md
│   └── notebooks/
│
├── 02_ML_Fundamentals/
│   ├── README.md
│   └── notebooks/
│
├── 03_Data_Preprocessing/
│   ├── README.md
│   └── notebooks/
│
├── 04_Feature_Engineering/
│   ├── README.md
│   └── notebooks/
│
├── 05_Train_Validation_Test_Splits/
│   ├── README.md
│   └── notebooks/
│
├── 06_Supervised_Learning/
│   ├── README.md
│   ├── regression/
│   │   └── README.md
│   └── classification/
│       └── README.md
│
├── 07_Unsupervised_Learning/
│   ├── README.md
│   ├── clustering/
│   │   └── README.md
│   └── dimensionality_reduction/
│       └── README.md
│
├── 08_Model_Evaluation/
│   ├── README.md
│   └── notebooks/
│
├── 09_Cross_Validation/
│   ├── README.md
│   └── notebooks/
│
├── 10_Hyperparameter_Tuning/
│   ├── README.md
│   └── notebooks/
│
├── 11_Scikit_Learn_Pipelines/
│   ├── README.md
│   └── notebooks/
│
├── 12_Imbalanced_Data/
│   ├── README.md
│   └── notebooks/
│
├── 13_Model_Explainability/
│   ├── README.md
│   └── notebooks/
│
├── 14_Model_Saving_Inference/
│   ├── README.md
│   ├── models/
│   └── scripts/
│
├── 15_Exercises/
│   ├── README.md
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── notebooks/
│   └── README.md
│
└── projects/
    ├── README.md
    │
    ├── house_price_prediction/
    │   └── README.md
    │
    ├── customer_churn_prediction/
    │   └── README.md
    │
    └── customer_segmentation/
        └── README.md
```

*Note: The nested README files and subfolders are suggested organizational conventions. Create them as needed. Git does not track empty directories, so add files to folders you want GitHub to display.*

---

## 📚 Learning Roadmap

### 01 — Statistics and Probability

**Objective:** Understand the mathematical concepts needed to reason about data and model performance.

Topics:
- Population and sample.
- Mean, median, mode, variance, and standard deviation.
- Probability fundamentals.
- Conditional probability and Bayes' theorem.
- Common probability distributions.
- Sampling and sampling bias.
- Correlation and covariance.
- Confidence intervals and hypothesis testing.
- Statistical significance versus practical significance.
- Linear relationships and basic mathematical notation.

Practice:
- Calculate descriptive statistics using Python.
- Simulate coin tosses and dice rolls.
- Explore distributions and sampling variability.
- Investigate correlation without assuming causation.

### 02 — Machine Learning Fundamentals

**Objective:** Understand what machine learning is and how models learn from examples.

Topics:
- Supervised, unsupervised, and reinforcement learning.
- Features and target variables.
- Training, prediction, and inference.
- Parameters and hyperparameters.
- Regression versus classification.
- Clustering and dimensionality reduction.
- Baseline models.
- Overfitting and underfitting.
- Bias–variance trade-off.
- Generalization to unseen data.
- Data leakage.
- The end-to-end ML workflow.

Practice:
- Train a simple model using a built-in Scikit-learn dataset.
- Compare a baseline with a trained model.
- Demonstrate overfitting using models of different complexity.
- Explain the difference between training performance and generalization.

### 03 — Data Preprocessing

**Objective:** Convert raw data into a suitable form for machine learning.

Topics:
- Inspecting data types and distributions.
- Handling missing values.
- Removing duplicate records where appropriate.
- Encoding categorical variables.
- Standardization and normalization.
- Handling inconsistent values.
- Outlier investigation.
- Data cleaning and validation.
- Avoiding preprocessing leakage.
- Fitting transformations only on training data.

Practice:
- Clean a dataset containing missing values.
- Encode categorical columns.
- Compare models with and without feature scaling.
- Build a reproducible preprocessing workflow.

### 04 — Feature Engineering

**Objective:** Create useful model inputs from existing data.

Topics:
- Feature selection and transformation.
- Numerical and categorical features.
- One-hot and ordinal encoding.
- Scaling and normalization.
- Binning numerical variables.
- Date and time features.
- Interaction features.
- Log transformations.
- Domain-informed feature creation.
- Feature importance.
- Multicollinearity awareness.
- Preventing target leakage.

Practice:
- Create new features from dates and numerical columns.
- Compare model performance before and after feature engineering.
- Evaluate whether new features improve validation performance.

### 05 — Train, Validation, and Test Splits

**Objective:** Evaluate models without accidentally using information they should not have seen.

Topics:
- Training, validation, and test sets.
- Random train-test splits.
- Reproducibility using random seeds.
- Stratified splitting for classification.
- Validation-based model selection.
- Time-aware splits for time-dependent data.
- Group-based splitting when observations are related.
- Data leakage prevention.
- Final evaluation on unseen test data.

Practice:
- Compare different split strategies.
- Investigate how leakage creates misleading results.
- Choose a suitable split for classification, grouped, and time-series problems.

### 06 — Supervised Learning

**Objective:** Learn from labelled examples to predict continuous values or categories.

#### Regression

Topics:
- Linear Regression.
- Multiple Linear Regression.
- Polynomial Regression.
- Decision Tree Regression.
- Random Forest Regression.
- Gradient Boosting fundamentals.
- Regularization with Ridge and Lasso.
- Residual analysis.
- Prediction errors and model assumptions.

Practice:
- Predict house prices.
- Compare linear and tree-based models.
- Analyze residuals and investigate large errors.

#### Classification

Topics:
- Logistic Regression.
- K-Nearest Neighbors (KNN).
- Decision Trees.
- Random Forest.
- Support Vector Machines (SVM).
- Naive Bayes.
- Gradient Boosting classifiers.
- Decision thresholds.
- Class probabilities.
- Multiclass classification.

Practice:
- Predict customer churn.
- Compare classification algorithms.
- Examine the trade-off between false positives and false negatives.

### 07 — Unsupervised Learning

**Objective:** Discover patterns and structure in data without labelled targets.

#### Clustering

Topics:
- K-Means.
- Hierarchical clustering.
- DBSCAN fundamentals.
- Distance and similarity measures.
- Feature scaling for distance-based algorithms.
- Choosing the number of clusters.
- Elbow method.
- Silhouette score.
- Cluster profiling and interpretation.

Practice:
- Segment customers based on purchasing behavior.
- Compare clustering approaches.
- Describe the characteristics and limitations of each cluster.

#### Dimensionality Reduction

Topics:
- Why dimensionality reduction is useful.
- Principal Component Analysis (PCA).
- Explained variance.
- Feature scaling before PCA.
- Visualizing high-dimensional data.
- Limitations of reduced-dimensional representations.

Practice:
- Apply PCA to a numerical dataset.
- Visualize data using two principal components.
- Compare explained variance before choosing the number of components.

### 08 — Model Evaluation

**Objective:** Measure model quality using metrics appropriate to the problem.

Topics:

**Regression metrics**
- Mean Absolute Error (MAE).
- Mean Squared Error (MSE).
- Root Mean Squared Error (RMSE).
- \(R^2\) score.
- Residual analysis.

**Classification metrics**
- Accuracy.
- Precision and recall.
- F1-score.
- Confusion matrix.
- ROC curve and ROC-AUC.
- Precision–recall curve.
- Log loss.
- Threshold selection.

**Clustering evaluation**
- Silhouette score.
- Cluster separation and cohesion.
- Practical interpretability.

Practice:
- Compare multiple metrics for the same model.
- Investigate why accuracy can be misleading for imbalanced data.
- Explain why the best metric depends on the business objective.

### 09 — Cross-Validation

**Objective:** Estimate how consistently a model performs across different data splits.

Topics:
- K-Fold cross-validation.
- Stratified K-Fold.
- Leave-One-Out cross-validation.
- Group-based cross-validation.
- Time-series cross-validation.
- Mean and variation of validation scores.
- Cross-validation with preprocessing pipelines.
- Leakage prevention.

Practice:
- Compare a single validation split with K-Fold results.
- Evaluate several algorithms using the same cross-validation strategy.
- Select a split strategy based on the data structure.

### 10 — Hyperparameter Tuning

**Objective:** Improve model performance through systematic experimentation.

Topics:
- Parameters versus hyperparameters.
- Manual tuning.
- GridSearchCV.
- RandomizedSearchCV.
- Search spaces and computational cost.
- Choosing a primary scoring metric.
- Cross-validation during tuning.
- Avoiding test-set overuse.
- Recording experiment results.

Practice:
- Tune a Decision Tree.
- Compare default and tuned Random Forest models.
- Document the selected hyperparameters and validation scores.

### 11 — Scikit-learn Pipelines

**Objective:** Build consistent, reusable machine learning workflows.

Topics:
- `Pipeline`.
- `ColumnTransformer`.
- Numerical and categorical preprocessing.
- Imputation and encoding.
- Feature scaling.
- Model integration.
- Cross-validation with pipelines.
- Hyperparameter tuning inside pipelines.
- Reproducibility.
- Prevention of preprocessing leakage.

Practice:
- Build a pipeline for mixed numerical and categorical data.
- Compare pipeline predictions with a manually processed workflow.
- Save a complete preprocessing-and-model pipeline.

### 12 — Imbalanced Data

**Objective:** Train and evaluate models when some classes are much less common than others.

Topics:
- Class imbalance.
- Why accuracy may be misleading.
- Class weights.
- Stratified sampling.
- Random oversampling and undersampling.
- SMOTE fundamentals.
- Precision–recall analysis.
- Threshold adjustment.
- Comparing approaches using suitable validation.
- Preventing resampling leakage.

Practice:
- Build a classifier on an imbalanced dataset.
- Compare baseline, class-weighted, and resampled approaches.
- Apply resampling only to training folds, never before splitting the full dataset.

### 13 — Model Explainability

**Objective:** Understand which factors influence model predictions and where interpretation can be misleading.

Topics:
- Model coefficients.
- Feature importance.
- Permutation importance.
- Partial dependence fundamentals.
- SHAP fundamentals.
- Local versus global explanations.
- Correlated feature limitations.
- Explanation stability.
- Fairness and responsible interpretation.

Practice:
- Compare feature importance across two models.
- Explain individual predictions where appropriate.
- Document the limits of each explanation method.

**Important:** Feature importance and explanation methods describe model behavior; they do not automatically establish causation.

### 14 — Model Saving and Inference

**Objective:** Reuse a trained model to generate predictions on new data.

Topics:
- Saving suitable Python model objects.
- Joblib and model persistence.
- Loading a saved model.
- Preserving preprocessing with the model.
- Input schema validation.
- Prediction scripts.
- Batch inference.
- Reproducible dependencies.
- Model and library version compatibility.
- Security considerations when loading serialized files.

Practice:
- Train and save a model pipeline.
- Load it in a separate Python script.
- Validate input columns and data types.
- Generate predictions for unseen records.

Only load serialized model files from trusted sources.

### 15 — Machine Learning Exercises

**Objective:** Strengthen understanding through independent implementation and problem-solving.

**Beginner**
- Explore a built-in dataset.
- Train a simple regression model.
- Train a basic classification model.
- Calculate evaluation metrics.
- Handle missing values.
- Encode categorical variables.

**Intermediate**
- Compare multiple algorithms.
- Build a preprocessing pipeline.
- Use cross-validation.
- Tune model hyperparameters.
- Analyze feature importance.
- Investigate class imbalance.

**Advanced**
- Build an end-to-end model pipeline.
- Compare multiple model families fairly.
- Implement leakage-safe feature engineering.
- Analyze errors across subgroups.
- Save and test an inference pipeline.
- Document reproducibility and model limitations.

For each exercise, record the problem, approach, code, results, interpretation, and lessons learned.

---

## 🧪 Portfolio Projects

All projects below are **Planned** until the actual work is completed and documented.

| # | Project | Problem Type | Status |
|---|---|---|---|
| 1 | House Price Prediction | Regression | Planned |
| 2 | Customer Churn Prediction | Classification | Planned |
| 3 | Customer Segmentation | Clustering | Planned |

### Project 1 — House Price Prediction

**Goal:** Predict property prices using available property characteristics.

Potential workflow:
1. Define the prediction target and evaluation metric.
2. Explore the dataset and identify data-quality issues.
3. Analyze price distributions and feature relationships.
4. Create training, validation, and test splits.
5. Build a simple baseline.
6. Develop preprocessing and feature engineering steps.
7. Train and compare regression models.
8. Use cross-validation and tune selected hyperparameters.
9. Evaluate final performance on the test set.
10. Analyze residuals and important features.
11. Save the model pipeline and document its usage.

**Potential metrics:** MAE, RMSE, and \(R^2\).

**Deliverables:**
- Jupyter Notebook.
- Reproducible training pipeline.
- Model evaluation report.
- Feature analysis and limitations.
- Inference example.

### Project 2 — Customer Churn Prediction

**Goal:** Predict which customers may stop using a service based on historical customer data.

Potential workflow:
1. Inspect customer records and define churn.
2. Explore class distribution and missing values.
3. Investigate relationships between customer attributes and churn.
4. Split data while preserving appropriate class proportions.
5. Build a baseline classifier.
6. Create a preprocessing pipeline.
7. Compare classification models.
8. Evaluate precision, recall, F1-score, and precision–recall behavior.
9. Investigate class imbalance and decision thresholds.
10. Explain model behavior and limitations.
11. Save the final model pipeline.

**Important:** Churn predictions indicate estimated risk, not certainty. Recommendations should account for false positives, false negatives, and potential subgroup differences.

**Deliverables:**
- Jupyter Notebook.
- Classification pipeline.
- Confusion matrix and evaluation report.
- Feature-importance analysis.
- Model limitations and next steps.

### Project 3 — Customer Segmentation

**Goal:** Discover meaningful groups of customers using relevant behavioral or purchasing features.

Potential workflow:
1. Explore customer data and define appropriate features.
2. Investigate missing values and outliers.
3. Scale features when required by the chosen algorithm.
4. Compare clustering approaches.
5. Evaluate cluster quality and stability.
6. Visualize clusters where appropriate.
7. Profile each cluster using interpretable statistics.
8. Explain the limitations of the segments.

**Potential methods:** K-Means and hierarchical clustering, with DBSCAN as an optional comparison.

**Potential evaluation:** Silhouette score, cluster profiles, and stability across reasonable choices.

**Deliverables:**
- Jupyter Notebook.
- Clustering experiments.
- Cluster visualization.
- Customer segment profiles.
- Interpretation and limitations.

*Project conclusions will be based on actual experiments and data. No model performance or business impact will be claimed before it is measured.*

---

## 📁 Recommended Project Structure

As individual projects grow, organize them like this:

```text
house_price_prediction/
├── README.md
├── notebooks/
│   └── house_price_analysis.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
├── tests/
├── reports/
├── requirements.txt
└── .gitignore
```

Adapt this structure to the needs of each project. Keep notebooks useful for exploration and move reusable logic into Python modules as the project matures.

Avoid committing large datasets, credentials, or unnecessary generated model files. Document how to obtain any external datasets and reproduce the experiments.

---

## 📏 Machine Learning Project Checklist

Use this checklist for every end-to-end project.

- [ ] Define the problem and target variable.
- [ ] Select a suitable evaluation metric.
- [ ] Inspect the dataset and assess data quality.
- [ ] Identify potential leakage and data dependencies.
- [ ] Create appropriate training, validation, and test splits.
- [ ] Establish a baseline model.
- [ ] Build preprocessing and feature engineering steps.
- [ ] Train and compare appropriate algorithms.
- [ ] Use cross-validation when appropriate.
- [ ] Tune hyperparameters without repeatedly using the test set.
- [ ] Evaluate the final model on held-out data.
- [ ] Analyze prediction errors and model limitations.
- [ ] Document explainability and fairness considerations.
- [ ] Save the complete model pipeline.
- [ ] Test inference on new data.
- [ ] Document dependencies and reproduction steps.
- [ ] Update the README with actual results.

---

## 📈 Progress Tracker

| Learning Area | Status |
|---|---|
| Statistics and Probability | Planned |
| ML Fundamentals | Planned |
| Data Preprocessing | Planned |
| Feature Engineering | Planned |
| Train, Validation, Test Splits | Planned |
| Supervised Learning — Regression | Planned |
| Supervised Learning — Classification | Planned |
| Unsupervised Learning — Clustering | Planned |
| Unsupervised Learning — Dimensionality Reduction | Planned |
| Model Evaluation | Planned |
| Cross-Validation | Planned |
| Hyperparameter Tuning | Planned |
| Scikit-learn Pipelines | Planned |
| Imbalanced Data | Planned |
| Model Explainability | Planned |
| Model Saving and Inference | Planned |
| ML Exercises | Planned |
| House Price Prediction | Planned |
| Customer Churn Prediction | Planned |
| Customer Segmentation | Planned |

**Projects completed:** 0

I will update the tracker as I finish exercises, validate model results, and document working projects.

---

## 🚀 Getting Started

Install the core libraries in your Python environment:

```bash
python -m pip install numpy pandas matplotlib seaborn scikit-learn jupyter joblib
```

Start Jupyter Notebook:

```bash
python -m jupyter notebook
```

Recommended workflow:

1. Learn one concept at a time.
2. Run a small example.
3. Modify the example and observe what changes.
4. Complete exercises without immediately copying solutions.
5. Record results and explanations in notebooks.
6. Apply the concept to one of the portfolio projects.
7. Commit meaningful, working progress to GitHub.

---

## 📌 Learning Principles

- Understand the problem before selecting an algorithm.
- Start with a simple baseline.
- Use appropriate validation strategies.
- Prevent data leakage at every stage.
- Select metrics that reflect the actual objective.
- Do not trust a high score without checking how it was obtained.
- Compare models on a fair, consistent basis.
- Investigate errors rather than reporting only aggregate metrics.
- Document assumptions, limitations, and reproducibility.
- Prefer clear, maintainable code over unnecessary complexity.

---

## 🎯 Final Goal

Build a strong foundation in **Machine Learning engineering** by progressing from mathematical and statistical fundamentals to complete, reproducible machine learning workflows.

By completing this section, I aim to demonstrate that I can prepare data, engineer features, train and evaluate appropriate models, interpret predictions, prevent common modeling mistakes, and build reliable inference pipelines.

This folder is part of my long-term journey toward becoming an **AI/ML Engineer**, progressing toward Deep Learning, NLP, Generative AI, RAG, AI Agents, and production AI systems.

**Understand the data. Build the baseline. Validate carefully. Improve systematically. Ship responsibly.** 🚀

---

*This repository is a work in progress. All roadmap items remain planned until the corresponding exercises or projects have been completed and documented.*
