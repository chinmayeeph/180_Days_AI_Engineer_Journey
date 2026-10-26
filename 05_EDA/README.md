# 📊 Exploratory Data Analysis (EDA)

Welcome to my **Exploratory Data Analysis (EDA)** learning repository!

This folder documents my journey of learning how to inspect, clean, analyze, visualize, and interpret datasets using Python. The goal is to develop strong analytical thinking and turn raw data into meaningful insights that support data-driven decisions.

EDA is an essential step in the Data Science and AI/ML workflow because it helps uncover patterns, identify data-quality issues, understand relationships between variables, and prepare datasets for further analysis and machine learning.

---

## 🎯 Learning Objectives

By completing this section, I aim to learn how to:

- Understand unfamiliar datasets systematically.
- Inspect dataset structure, dimensions, and data types.
- Identify missing values, duplicate records, and inconsistent data.
- Calculate and interpret descriptive statistics.
- Perform univariate, bivariate, and multivariate analysis.
- Understand distributions, outliers, and correlations.
- Create clear visualizations using Matplotlib and Seaborn.
- Investigate patterns, trends, relationships, and anomalies.
- Develop evidence-based conclusions from data.
- Communicate findings through analytical reports and visual storytelling.
- Prepare datasets for downstream statistical analysis and machine learning.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical operations |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Interactive analysis |
| Google Colab | Cloud-based notebook execution |
| Git and GitHub | Version control and portfolio management |

---

## 📂 Repository Structure

```text
05_EDA/
│
├── README.md
│
├── 01_EDA_Workflow/
│   ├── README.md
│   └── notebooks/
│
├── 02_Data_Quality_Assessment/
│   ├── README.md
│   └── notebooks/
│
├── 03_Descriptive_Statistics/
│   ├── README.md
│   └── notebooks/
│
├── 04_Univariate_Analysis/
│   ├── README.md
│   └── notebooks/
│
├── 05_Bivariate_Multivariate_Analysis/
│   ├── README.md
│   └── notebooks/
│
├── 06_Outliers_Distributions_Correlation/
│   ├── README.md
│   └── notebooks/
│
├── 07_Matplotlib/
│   ├── README.md
│   └── notebooks/
│
├── 08_Seaborn/
│   ├── README.md
│   └── notebooks/
│
├── 09_Insight_Generation_Storytelling/
│   ├── README.md
│   └── notebooks/
│
├── datasets/
│   └── README.md
│
├── notebooks/
│   └── README.md
│
└── projects/
    ├── README.md
    │
    ├── titanic_survival_analysis/
    │   └── README.md
    │
    ├── sales_data_eda/
    │   └── README.md
    │
    └── customer_data_eda/
        └── README.md
```

*Note: The README files and notebook folders shown inside subfolders are suggested organizational conventions. Create them as needed. GitHub does not track empty directories, so add files to folders you want to appear in the repository.*

---

## 📚 Learning Roadmap

### 01 — EDA Workflow

**Objective:** Learn a repeatable process for exploring any new dataset.

Topics:
- Define the business or analytical question.
- Load data using Pandas.
- Inspect rows, columns, dimensions, and data types.
- Review missing values and duplicates.
- Summarize numerical and categorical variables.
- Select suitable visualizations.
- Investigate patterns and unexpected observations.
- Document findings and limitations.

**Practice tasks:**
- Explore a CSV file from beginning to end.
- Create a reusable EDA checklist.
- Write a short summary of the most important findings.

### 02 — Data Quality Assessment

**Objective:** Identify data problems before drawing conclusions.

Topics:
- Missing values and missing-value percentages.
- Duplicate records.
- Incorrect data types.
- Inconsistent category labels.
- Invalid values and impossible ranges.
- Whitespace and formatting issues.
- Unique values and category frequencies.
- Data-quality checks before and after cleaning.

**Practice tasks:**
- Generate a data-quality summary.
- Identify duplicated rows and investigate them.
- Compare a dataset before and after cleaning.

### 03 — Descriptive Statistics

**Objective:** Summarize the key characteristics of a dataset.

Topics:
- Mean, median, and mode.
- Minimum, maximum, and range.
- Variance and standard deviation.
- Quartiles and percentiles.
- Interquartile range (IQR).
- Frequency counts.
- Grouped summaries.
- Numerical versus categorical summaries.

**Practice tasks:**
- Calculate descriptive statistics for a dataset.
- Compare the mean and median when data is skewed.
- Summarize numerical values by category.

### 04 — Univariate Analysis

**Objective:** Understand one variable at a time.

Topics:
- Numerical and categorical variables.
- Frequency tables.
- Histograms.
- Box plots.
- Bar charts and count plots.
- Distribution shape and skewness.
- Central tendency and variability.
- Rare categories and unusual observations.

**Practice tasks:**
- Analyze the distribution of passenger ages.
- Examine sales values using histograms and box plots.
- Identify the most frequent categories in a dataset.

### 05 — Bivariate and Multivariate Analysis

**Objective:** Understand relationships between two or more variables.

Topics:
- Numerical versus numerical comparisons.
- Categorical versus numerical comparisons.
- Categorical versus categorical comparisons.
- Grouped aggregation.
- Scatter plots and grouped box plots.
- Cross-tabulation and pivot tables.
- Pair plots.
- Heatmaps and multivariable comparisons.
- Potential confounding variables.

**Practice tasks:**
- Compare survival rates across passenger groups.
- Investigate relationships between sales and profit.
- Compare customer behavior across multiple segments.

### 06 — Outliers, Distributions, and Correlation

**Objective:** Investigate unusual observations and relationships.

Topics:
- Normal, skewed, and other common distributions.
- Outlier detection using IQR.
- Z-scores and their assumptions.
- Pearson and Spearman correlation.
- Correlation matrices.
- Scatter plots and relationship patterns.
- Correlation versus causation.
- Limitations of correlation analysis.

**Practice tasks:**
- Detect and investigate outliers.
- Compare Pearson and Spearman correlations.
- Visualize correlations and explain what they do—and do not—mean.

**Important:** An outlier is not automatically an error. Investigate it before deciding whether it should be retained, corrected, or excluded.

### 07 — Matplotlib

**Objective:** Build clear, customizable visualizations.

Topics:
- Figure and axes.
- Line charts.
- Bar charts.
- Histograms.
- Scatter plots.
- Box plots.
- Titles, labels, legends, and annotations.
- Figure size and layout.
- Subplots.
- Saving charts to image files.

**Practice tasks:**
- Create a chart gallery.
- Customize labels, legends, and axes.
- Build a multi-chart analytical report.

### 08 — Seaborn

**Objective:** Create informative statistical visualizations.

Topics:
- Histograms and KDE plots.
- Count plots and bar plots.
- Box plots and violin plots.
- Scatter plots and regression plots.
- Pair plots.
- Heatmaps.
- Facet grids.
- Color palettes and categorical comparisons.

**Practice tasks:**
- Visualize a dataset using multiple chart types.
- Compare Matplotlib and Seaborn implementations.
- Create a correlation heatmap and grouped visualizations.

### 09 — Insight Generation and Storytelling

**Objective:** Communicate analytical findings clearly and responsibly.

Topics:
- Converting observations into insights.
- Separating facts from assumptions.
- Connecting findings to the original question.
- Selecting appropriate visualizations.
- Explaining business or practical implications.
- Documenting limitations and uncertainty.
- Writing concise conclusions and recommendations.
- Structuring an EDA report.

**Practice tasks:**
- Write a findings summary for each completed project.
- Support every major conclusion with evidence.
- Create a final report with charts, findings, limitations, and next steps.

---

## 🧪 Projects

All projects below are planned learning exercises. Their status will be updated as I complete and document the actual work.

| # | Project | Main Skills | Status |
|---|---|---|---|
| 1 | Titanic Survival Analysis | Data quality, distributions, group comparisons, visualization | Planned |
| 2 | Sales Data EDA | Sales trends, product performance, aggregation, visualization | Planned |
| 3 | Customer Data EDA | Customer segments, behavior, relationships, insights | Planned |

### Project 1 — Titanic Survival Analysis

**Goal:** Investigate which passenger characteristics are associated with survival in the Titanic dataset.

Potential analysis:
- Dataset structure and data quality.
- Missing values and duplicate checks.
- Age, fare, and passenger-class distributions.
- Survival rates by sex, passenger class, and age group.
- Relationships between passenger characteristics.
- Visualizations and evidence-based conclusions.

**Expected deliverables:**
- Jupyter Notebook.
- Key visualizations.
- Findings summary.
- Data limitations and next steps.

### Project 2 — Sales Data EDA

**Goal:** Explore sales performance and identify trends, high-performing categories, and potential business opportunities.

Potential analysis:
- Revenue and order distributions.
- Sales by product, category, or region.
- Monthly and seasonal trends.
- Product performance comparisons.
- Missing values, duplicates, and unusual transactions.
- Evidence-based recommendations.

**Expected deliverables:**
- Cleaned or documented dataset.
- Jupyter Notebook.
- Sales visualizations.
- Concise analytical report.

### Project 3 — Customer Data EDA

**Goal:** Understand customer characteristics, purchasing behavior, and differences between customer groups.

Potential analysis:
- Customer demographics, where available.
- Purchase frequency and spending distributions.
- Customer-group comparisons.
- Relationships between numerical variables.
- Outliers and data-quality issues.
- Potential segments for further investigation.

**Expected deliverables:**
- Jupyter Notebook.
- Customer analysis visualizations.
- Findings and limitations.
- Suggested next steps for deeper analysis.

*Project conclusions will be based on the actual datasets and observed results, not assumptions made in advance.*

---

## 📁 Folder Organization Guidelines

### `datasets/`

Store small, public, permitted practice datasets and dataset documentation.

Recommended practices:
- Record the dataset source and license.
- Document column meanings when needed.
- Avoid committing sensitive or personally identifiable data.
- Use `.gitignore` or Git LFS where appropriate for large files.
- Keep raw data separate from cleaned outputs when practical.

### `notebooks/`

Store general EDA practice notebooks that are not specific to a single portfolio project.

Suggested naming convention:

```text
01_dataset_inspection.ipynb
02_data_quality_checks.ipynb
03_descriptive_statistics.ipynb
04_univariate_analysis.ipynb
05_bivariate_analysis.ipynb
06_correlation_analysis.ipynb
07_visualization_practice.ipynb
08_insight_generation.ipynb
```

### `projects/`

Keep each portfolio project self-contained, with its own README, notebook, and relevant outputs.

Suggested project structure:

```text
project_name/
├── README.md
├── notebooks/
├── outputs/
└── reports/
```

Add a `data/` directory only when appropriate. Do not commit large or restricted datasets without checking their licensing and repository requirements.

---

## 📏 EDA Checklist

Use this checklist for each new dataset.

- [ ] Define the analytical question.
- [ ] Load the dataset successfully.
- [ ] Inspect dimensions, columns, and data types.
- [ ] Review missing values and duplicates.
- [ ] Check unique values and category consistency.
- [ ] Calculate descriptive statistics.
- [ ] Analyze individual variable distributions.
- [ ] Investigate relationships between variables.
- [ ] Examine outliers and correlations.
- [ ] Create suitable visualizations.
- [ ] Record meaningful findings.
- [ ] Document limitations and assumptions.
- [ ] Summarize conclusions and next steps.
- [ ] Save the notebook and update the project README.

---

## 📈 Progress Tracker

| Area | Status |
|---|---|
| EDA workflow | Planned |
| Data quality assessment | Planned |
| Descriptive statistics | Planned |
| Univariate analysis | Planned |
| Bivariate and multivariate analysis | Planned |
| Outliers, distributions, and correlation | Planned |
| Matplotlib | Planned |
| Seaborn | Planned |
| Insight generation and storytelling | Planned |
| Titanic Survival Analysis | Planned |
| Sales Data EDA | Planned |
| Customer Data EDA | Planned |

**Projects completed:** 0

I will update the progress tracker as I complete exercises, notebooks, and projects with documented results.

---

## 🚀 How to Run the Notebooks

1. Install Python and the required libraries.
2. Open the repository in VS Code or Google Colab.
3. Install the packages needed for the notebook:

   ```bash
   python -m pip install numpy pandas matplotlib seaborn jupyter
   ```

4. Start Jupyter Notebook if working locally:

   ```bash
   python -m jupyter notebook
   ```

5. Open the notebook and run its cells in order.
6. Review the results and record conclusions based on the evidence.

---

## 📌 Learning Principles

- Understand the question before analyzing the data.
- Investigate data-quality issues before drawing conclusions.
- Select charts based on the question and variable types.
- Explain what the results mean, not just what the code does.
- Avoid confusing correlation with causation.
- Document assumptions, limitations, and unexpected findings.
- Write readable, reproducible code.
- Prioritize analytical reasoning over the number of charts created.

---

## 🎯 Final Goal

Build a strong foundation in exploratory data analysis and develop the ability to transform raw datasets into **reliable findings, clear visualizations, and actionable insights**.

This folder is part of my long-term journey toward becoming an **AI/ML Engineer**, with a focus on Python, data analysis, machine learning, Generative AI, and production-ready AI systems.

**Learn consistently. Analyze carefully. Communicate clearly. Build projects that demonstrate real skills.** 🚀

---

*This repository is a work in progress. Project descriptions represent learning goals until the corresponding work has been completed and documented.*
