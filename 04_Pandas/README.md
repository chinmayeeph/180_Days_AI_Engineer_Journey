# 🐼 Pandas — Data Analysis & Manipulation

Welcome to the **Pandas** section of my **180 Days AI Engineer Journey**.

Pandas is a Python library used to load, clean, manipulate, analyze, and transform structured data. It is an essential tool for data analysis, exploratory data analysis (EDA), machine learning, and AI engineering.

This section focuses on building practical Pandas skills through topic-wise exercises, practice notebooks, and real-world projects.

---

## 🎯 Learning Objectives

By completing this section, I aim to:

- Understand Pandas `Series` and `DataFrame` objects.
- Load datasets from CSV, Excel, and other supported file formats.
- Inspect datasets and understand their structure.
- Select, filter, sort, and index rows and columns.
- Handle missing values and duplicate records.
- Work with data types, strings, and date-time values.
- Group data and perform aggregations.
- Combine datasets using merge, join, and concatenate operations.
- Create pivot tables and summarize data.
- Clean and transform raw datasets into analysis-ready data.
- Apply Pandas to practical data analysis projects.
- Prepare datasets for visualization and machine learning.

---

## 🗺️ Learning Roadmap

| No. | Topic | Key Concepts |
|---|---|---|
| 01 | Series & DataFrames | `Series`, `DataFrame`, creation, attributes, basic operations |
| 02 | Loading & Inspecting Data | `read_csv()`, `read_excel()`, `head()`, `info()`, `describe()` |
| 03 | Indexing, Filtering & Sorting | `loc`, `iloc`, boolean filtering, `sort_values()` |
| 04 | Missing Data & Duplicates | `isna()`, `fillna()`, `dropna()`, `duplicated()`, `drop_duplicates()` |
| 05 | Data Types, Strings & DateTime | `astype()`, `.str`, `to_datetime()`, date extraction |
| 06 | GroupBy & Aggregation | `groupby()`, `agg()`, `sum()`, `mean()`, `count()` |
| 07 | Merge, Join & Concat | `merge()`, `join()`, `concat()`, join types |
| 08 | Pivot Tables | `pivot()`, `pivot_table()`, `melt()`, reshaping data |
| 09 | Data Cleaning & Transformation | `replace()`, `apply()`, `map()`, `rename()`, feature creation |
| 10 | Practice Notebooks | Topic-wise exercises, revision, mini challenges |

---

## 📂 Folder Structure

```text
04_Pandas/
│
├── README.md
│
├── 01_Series_DataFrames/
│   ├── README.md
│   ├── series_basics.ipynb
│   ├── dataframe_basics.ipynb
│   └── exercises.ipynb
│
├── 02_Loading_Inspecting_Data/
│   ├── README.md
│   ├── loading_csv.ipynb
│   ├── loading_excel.ipynb
│   └── inspecting_datasets.ipynb
│
├── 03_Indexing_Filtering_Sorting/
│   ├── README.md
│   ├── indexing_loc_iloc.ipynb
│   ├── filtering_data.ipynb
│   └── sorting_data.ipynb
│
├── 04_Missing_Data_Duplicates/
│   ├── README.md
│   ├── handling_missing_values.ipynb
│   └── handling_duplicates.ipynb
│
├── 05_DataTypes_String_DateTime/
│   ├── README.md
│   ├── data_types.ipynb
│   ├── string_operations.ipynb
│   └── datetime_operations.ipynb
│
├── 06_GroupBy_Aggregation/
│   ├── README.md
│   ├── groupby_basics.ipynb
│   └── aggregation_operations.ipynb
│
├── 07_Merge_Join_Concat/
│   ├── README.md
│   ├── merge_dataframes.ipynb
│   ├── join_dataframes.ipynb
│   └── concatenate_dataframes.ipynb
│
├── 08_Pivot_Tables/
│   ├── README.md
│   ├── pivot_basics.ipynb
│   └── pivot_table_analysis.ipynb
│
├── 09_Data_Cleaning_Transformation/
│   ├── README.md
│   ├── cleaning_workflow.ipynb
│   └── data_transformation.ipynb
│
├── 10_Practice_Notebooks/
│   ├── README.md
│   ├── beginner_exercises.ipynb
│   ├── intermediate_exercises.ipynb
│   └── pandas_challenges.ipynb
│
└── projects/
    │
    ├── student_performance_analyzer/
    │   ├── README.md
    │   ├── student_performance_analyzer.ipynb
    │   └── data/
    │
    └── sales_data_analysis/
        ├── README.md
        ├── sales_data_analysis.ipynb
        └── data/
```

*Note: This is the planned structure. Create the files and folders as you progress through each topic.*

---

## 🛠️ Tools & Technologies

- **Language:** Python
- **Library:** Pandas
- **Supporting libraries:** NumPy, Matplotlib, Seaborn
- **Environment:** Google Colab / Jupyter Notebook
- **Version control:** Git & GitHub
- **Datasets:** CSV and Excel files, plus public datasets where appropriate

### Installation

Install Pandas in a local Python environment:

```bash
python -m pip install pandas numpy matplotlib seaborn jupyter
```

In Google Colab, Pandas and the other core libraries are generally preinstalled.

Verify the installation:

```python
import pandas as pd

print(pd.__version__)
```

---

## 📚 Topics in Detail

### 01. Series & DataFrames

Learn the fundamental data structures used throughout Pandas.

- Create Series and DataFrames.
- Understand indexes, columns, shapes, and data types.
- Access rows and columns.
- Perform basic arithmetic and data operations.

**Practice outcome:** Create and inspect structured datasets using Python.

### 02. Loading & Inspecting Data

Learn how to import datasets and understand their contents before analysis.

- Read CSV and Excel files.
- Inspect the first and last rows.
- Check row counts, column names, and data types.
- Generate descriptive statistics.
- Identify potential data-quality issues.

**Practice outcome:** Load a dataset and prepare an initial data overview.

### 03. Indexing, Filtering & Sorting

Learn how to retrieve the exact data needed for analysis.

- Select rows and columns.
- Use `loc` and `iloc`.
- Filter records using conditions.
- Combine conditions with `&` and `|`.
- Sort values and reset indexes.

**Practice outcome:** Answer questions by filtering and sorting a dataset.

### 04. Missing Data & Duplicates

Learn to identify and handle common data-quality problems.

- Detect missing values.
- Remove or fill missing data appropriately.
- Identify duplicate rows.
- Remove duplicates when justified.
- Check how cleaning decisions affect the dataset.

**Practice outcome:** Produce a dataset with documented cleaning decisions.

### 05. Data Types, Strings & DateTime

Learn to work with different types of real-world data.

- Convert columns using `astype()`.
- Clean text with string methods.
- Standardize text values.
- Convert strings to dates using `pd.to_datetime()`.
- Extract year, month, day, and other date components.

**Practice outcome:** Standardize inconsistent text, data types, and date columns.

### 06. GroupBy & Aggregation

Learn to summarize data by categories.

- Group records using `groupby()`.
- Calculate sums, averages, counts, minimums, and maximums.
- Use multiple aggregations with `agg()`.
- Compare results across groups.

**Practice outcome:** Generate meaningful summaries, such as average marks by subject or revenue by region.

### 07. Merge, Join & Concat

Learn how to combine information from multiple datasets.

- Understand keys and relationships between tables.
- Use inner, left, right, and outer merges.
- Join DataFrames using indexes.
- Concatenate rows or columns.
- Validate results and identify unmatched records.

**Practice outcome:** Combine related datasets into a single analysis-ready DataFrame.

### 08. Pivot Tables

Learn to summarize and reshape data for reporting.

- Create pivot tables.
- Specify row and column groupings.
- Apply aggregation functions.
- Handle missing combinations.
- Reshape data between wide and long formats.

**Practice outcome:** Build summary tables for business and performance analysis.

### 09. Data Cleaning & Transformation

Combine your skills into a repeatable data-preparation workflow.

- Rename columns.
- Standardize inconsistent values.
- Replace incorrect or unwanted values.
- Apply transformations.
- Create new columns and derived features.
- Validate the final dataset.

**Practice outcome:** Transform raw data into a reliable dataset ready for EDA or machine learning.

### 10. Practice Notebooks

Reinforce the concepts through independent coding.

- Complete beginner exercises.
- Solve intermediate filtering and aggregation problems.
- Practice cleaning messy datasets.
- Work on multi-step challenges.
- Revisit mistakes and document what you learned.

**Practice outcome:** Develop confidence using Pandas without relying entirely on tutorials.

---

## 🚀 Projects

### 1. Student Performance Analyzer

**Objective:** Analyze student marks and identify academic performance patterns using Pandas.

**Skills applied:**

- Load and inspect student datasets.
- Handle missing values and duplicate records.
- Calculate total and average marks.
- Group students by class, subject, or other available categories.
- Identify top-performing students and subjects.
- Summarize performance using tables and visualizations.

**Expected deliverables:**

- `student_performance_analyzer.ipynb`
- Project-specific `README.md`
- Dataset or instructions for obtaining it
- Key findings and conclusions

**Portfolio value:** Demonstrates data cleaning, aggregation, and analytical reasoning.

### 2. Sales Data Analysis

**Objective:** Analyze sales transactions to understand revenue, product performance, and business trends.

**Skills applied:**

- Load and validate sales records.
- Handle missing and duplicate data.
- Convert dates and numeric columns correctly.
- Calculate revenue and other relevant metrics.
- Group sales by product, region, category, or month when those fields exist.
- Merge datasets when multiple related tables are provided.
- Create pivot tables and visualizations.
- Summarize business insights and recommendations.

**Expected deliverables:**

- `sales_data_analysis.ipynb`
- Project-specific `README.md`
- Dataset or instructions for obtaining it
- Visualizations and key findings

**Portfolio value:** Demonstrates practical business analysis and data-preparation skills.

---

## ✅ Learning Checklist

### Core Pandas

- [ ] Understand Series and DataFrames.
- [ ] Create and manipulate DataFrames.
- [ ] Load CSV and Excel datasets.
- [ ] Inspect and summarize data.
- [ ] Select, filter, and sort rows and columns.
- [ ] Handle missing values and duplicates.
- [ ] Work with data types, strings, and dates.
- [ ] Perform grouping and aggregation.
- [ ] Merge, join, and concatenate datasets.
- [ ] Create pivot tables.
- [ ] Clean and transform data.
- [ ] Complete practice exercises independently.

### Projects & GitHub

- [ ] Complete Student Performance Analyzer.
- [ ] Complete Sales Data Analysis.
- [ ] Write a README for each project.
- [ ] Document important decisions and findings.
- [ ] Push notebooks and relevant files to GitHub.
- [ ] Review and improve code readability.

---

## 📖 Learning Resources

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas)
- [Google Colab](https://colab.research.google.com/)

---

## 💡 My Learning Approach

For each topic, I will follow this process:

1. Learn the concept and understand why it is useful.
2. Follow a small example in a notebook.
3. Rewrite the example without looking at the solution.
4. Complete practice exercises.
5. Apply the concept to a real dataset.
6. Document mistakes, corrections, and key takeaways.
7. Commit and push completed work to GitHub.

**My goal is not just to memorize Pandas functions. It is to learn how to use Pandas to solve real data problems.**

---

## 🔗 Connection to My AI Engineer Journey

Pandas is an important foundation for the next stages of my roadmap:

- **EDA:** Explore patterns, distributions, and relationships in data.
- **Machine Learning:** Clean and prepare datasets for model training.
- **Feature Engineering:** Create and transform useful input features.
- **AI Engineering:** Inspect datasets, analyze evaluation results, and prepare structured data for AI workflows.

This section is one step toward becoming a practical, job-ready **AI/ML Engineer**.

---

*Part of my [180 Days AI Engineer Journey](../README.md) — Learn consistently, build projects, and improve every day.* 🐍
