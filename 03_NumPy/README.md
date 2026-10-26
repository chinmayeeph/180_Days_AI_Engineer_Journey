# 🧪 NumPy

Welcome to my **NumPy** learning section as part of my [180 Days AI Engineer Journey](../README.md).

A beginner-friendly introduction to **NumPy (Numerical Python)**, a fundamental Python library for numerical computing, array manipulation, mathematical operations, and statistical analysis.

This folder contains topic-wise notes, code examples, exercises, Jupyter notebooks, and a practical project to build a strong foundation in NumPy for Data Analysis, Machine Learning, and AI.

---

## 🎯 Learning Objectives

By completing this module, I aim to:

- Understand NumPy arrays and how they differ from Python lists.
- Create, access, modify, and reshape multidimensional arrays.
- Understand array data types and vectorized operations.
- Master NumPy broadcasting and mathematical operations.
- Perform statistical calculations and aggregations.
- Generate random numbers for simulations and experiments.
- Learn the fundamentals of linear algebra using NumPy.
- Apply NumPy concepts to real-world data analysis problems.
- Build a strong foundation for Pandas, Data Analysis, and Machine Learning.

---

## 🗺️ Learning Roadmap

| Day    | Main Focus                  | Repo                                                                                                                                       			 | Output                       |
| ------ | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------| ---------------------------- |
| **13** | NumPy fundamentals          | [day01_python_foundations](https://github.com/chinmayeeph/180_Days_AI_Engineer_Journey/tree/main/01_Python/day01_python_foundations)                    | Arrays notebook              |
| **14** | NumPy operations            | [day01_python_foundations](https://github.com/chinmayeeph/180_Days_AI_Engineer_Journey/tree/main/01_Python/day01_python_foundations)                    | NumPy exercises              |
| **15** | NumPy mini project          | [day01_python_foundations](https://github.com/chinmayeeph/180_Days_AI_Engineer_Journey/tree/main/01_Python/day01_python_foundations)                    | Data analysis with NumPy     |

---

## 📂 Folder Structure

```text
03_NumPy/
│
├── README.md
│
├── 01_Array_Creation/
│   └── Creating arrays using NumPy functions
│
├── 02_Indexing_Slicing_Reshaping/
│   └── Accessing, slicing, and reshaping arrays
│
├── 03_DataTypes_Vectorization/
│   └── Array data types and vectorized operations
│
├── 04_Broadcasting/
│   └── Performing operations on arrays of different shapes
│
├── 05_Mathematical_Operations/
│   └── Arithmetic, universal functions, and mathematical calculations
│
├── 06_Statistics_Aggregations/
│   └── Mean, median, standard deviation, sum, and other statistics
│
├── 07_Random_Number_Generation/
│   └── Generating random numbers and reproducible samples
│
├── 08_Linear_Algebra_Basics/
│   └── Dot products, matrix multiplication, and basic linear algebra
│
├── 09_Exercises/
│   └── Topic-wise practice problems and solutions
│
├── notebooks/
│   └── Jupyter notebooks for hands-on learning
│
└── projects/
    └── student_marks_analysis/
        └── Student marks analysis using NumPy
```

---

## 📚 Learning Roadmap

### 1. Array Creation

**Folder:** `01_Array_Creation/`

- [ ] What is NumPy?
- [ ] Installing and importing NumPy
- [ ] Understanding `ndarray`
- [ ] Creating arrays using `np.array()`
- [ ] Creating arrays with `np.zeros()` and `np.ones()`
- [ ] Using `np.full()` and `np.empty()`
- [ ] Using `np.arange()` and `np.linspace()`
- [ ] Understanding array dimensions, shape, size, and number of dimensions
- [ ] Creating one-dimensional, two-dimensional, and three-dimensional arrays

### 2. Indexing, Slicing, and Reshaping

**Folder:** `02_Indexing_Slicing_Reshaping/`

- [ ] Positive and negative indexing
- [ ] Slicing one-dimensional arrays
- [ ] Indexing and slicing two-dimensional arrays
- [ ] Selecting rows and columns
- [ ] Boolean indexing
- [ ] Fancy indexing
- [ ] Reshaping arrays using `reshape()`
- [ ] Flattening arrays using `flatten()` and `ravel()`
- [ ] Transposing arrays using `.T`
- [ ] Understanding `reshape(-1)` and inferred dimensions

### 3. Data Types and Vectorization

**Folder:** `03_DataTypes_Vectorization/`

- [ ] Understanding NumPy data types (`dtype`)
- [ ] Integer, floating-point, Boolean, and string arrays
- [ ] Converting data types using `astype()`
- [ ] Understanding type conversion
- [ ] Performing element-wise operations
- [ ] Understanding vectorization
- [ ] Comparing vectorized operations with Python loops
- [ ] Using conditional operations with `np.where()`

### 4. Broadcasting

**Folder:** `04_Broadcasting/`

- [ ] Understanding broadcasting
- [ ] Performing operations between arrays and scalars
- [ ] Broadcasting one-dimensional arrays
- [ ] Broadcasting two-dimensional arrays
- [ ] Understanding compatible array shapes
- [ ] Identifying broadcasting errors
- [ ] Applying broadcasting to practical numerical problems

### 5. Mathematical Operations

**Folder:** `05_Mathematical_Operations/`

- [ ] Addition, subtraction, multiplication, and division
- [ ] Floor division and modulus
- [ ] Exponentiation and square roots
- [ ] Absolute values and rounding
- [ ] Minimum and maximum operations
- [ ] Using universal functions (ufuncs)
- [ ] Comparing arrays element by element
- [ ] Applying conditional mathematical operations

### 6. Statistics and Aggregations

**Folder:** `06_Statistics_Aggregations/`

- [ ] Calculating the sum and product
- [ ] Finding minimum and maximum values
- [ ] Calculating mean and median
- [ ] Understanding variance and standard deviation
- [ ] Calculating percentiles and quantiles
- [ ] Using `argmin()` and `argmax()`
- [ ] Understanding the `axis` parameter
- [ ] Performing row-wise and column-wise calculations
- [ ] Handling missing or invalid numerical values

### 7. Random Number Generation

**Folder:** `07_Random_Number_Generation/`

- [ ] Creating random numbers with `np.random`
- [ ] Understanding `default_rng()`
- [ ] Generating random integers
- [ ] Generating random floating-point numbers
- [ ] Sampling from arrays
- [ ] Generating normally distributed values
- [ ] Understanding random seeds and reproducibility
- [ ] Applying random sampling to simple experiments

### 8. Linear Algebra Basics

**Folder:** `08_Linear_Algebra_Basics/`

- [ ] Understanding vectors and matrices
- [ ] Performing matrix addition and subtraction
- [ ] Understanding element-wise multiplication versus matrix multiplication
- [ ] Using `np.dot()` and `@`
- [ ] Understanding transpose operations
- [ ] Calculating determinants
- [ ] Finding matrix inverses
- [ ] Solving systems of linear equations
- [ ] Understanding vector norms

### 9. Exercises

**Folder:** `09_Exercises/`

- [ ] Complete array creation exercises
- [ ] Solve indexing and slicing problems
- [ ] Practice reshaping and broadcasting
- [ ] Perform mathematical calculations
- [ ] Solve statistical problems
- [ ] Practice random number generation
- [ ] Solve basic linear algebra problems
- [ ] Complete mixed-topic challenges without referring to notes

---

## 💻 Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Programming language |
| NumPy | Numerical computing and array operations |
| Jupyter Notebook | Interactive coding and experimentation |
| VS Code | Code editing and execution |
| Git and GitHub | Version control and project documentation |

### Installation

Install NumPy using pip:

```bash
python -m pip install numpy
```

Install Jupyter Notebook if needed:

```bash
python -m pip install notebook
```

Import NumPy in Python:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Data type:", arr.dtype)
print("Mean:", np.mean(arr))
```

Expected output:

```text
[10 20 30 40 50]
Shape: (5,)
Dimensions: 1
Data type: int64
Mean: 30.0
```

*Note: The displayed integer data type may vary by platform.*

---

## 🧪 Practical Project

### Student Marks Analysis Using NumPy

**Location:** `projects/student_marks_analysis/`

**Objective:** Analyze student marks across multiple subjects using NumPy arrays and statistical operations.

**Tasks:**

- [ ] Create a two-dimensional array containing student marks.
- [ ] Calculate each student's total and average marks.
- [ ] Calculate subject-wise average marks.
- [ ] Identify the highest and lowest marks.
- [ ] Find the topper in each subject.
- [ ] Calculate the class average and standard deviation.
- [ ] Identify students who scored above the class average.
- [ ] Count students who passed or failed using a defined passing criterion.
- [ ] Rank students based on their total marks.
- [ ] Display a clear summary of the results.

**Skills demonstrated:** Array creation, indexing, slicing, vectorization, broadcasting, aggregations, Boolean indexing, and basic statistical analysis.

---

## 📓 Jupyter Notebooks

The `notebooks/` directory contains hands-on notebooks for experimenting with NumPy concepts.

Suggested notebooks:

1. `01_NumPy_Basics.ipynb`
2. `02_Indexing_Slicing_Reshaping.ipynb`
3. `03_DataTypes_and_Vectorization.ipynb`
4. `04_Broadcasting.ipynb`
5. `05_Mathematical_Operations.ipynb`
6. `06_Statistics_and_Aggregations.ipynb`
7. `07_Random_Number_Generation.ipynb`
8. `08_Linear_Algebra_Basics.ipynb`
9. `09_NumPy_Practice_Problems.ipynb`

Each notebook should include explanations, code examples, expected outputs, common mistakes, and practice questions.

---

## ✅ Completion Checklist

- [ ] Understand the fundamentals of NumPy arrays.
- [ ] Complete all eight core topic folders.
- [ ] Solve the exercises independently.
- [ ] Complete the Student Marks Analysis project.
- [ ] Write clean, readable, and documented Python code.
- [ ] Upload the notebooks and project to GitHub.
- [ ] Explain the difference between Python lists and NumPy arrays.
- [ ] Explain broadcasting, vectorization, and the `axis` parameter.
- [ ] Complete a small numerical analysis task without following a tutorial.

---

## 🎯 Why NumPy Matters for AI/ML

NumPy provides important building blocks for:

- **Data Analysis:** Numerical calculations and statistical summaries.
- **Machine Learning:** Vectors, matrices, numerical transformations, and data preparation.
- **Deep Learning:** Understanding the array and tensor operations underlying many ML frameworks.
- **Scientific Computing:** Efficient operations on multidimensional numerical data.

NumPy is a foundation, not a substitute for learning Pandas, statistics, or machine learning algorithms.

---

## 📌 Learning Guidelines

1. Understand the concept before memorizing the syntax.
2. Type every example yourself and predict the output before running it.
3. Change array values and shapes to see how operations behave.
4. Practice for at least 30–60 minutes after learning a new topic.
5. Write short notes explaining concepts in your own words.
6. Revisit incorrect exercises and solve them again without looking at the solution.
7. Focus on understanding `shape`, `axis`, indexing, and broadcasting before moving to advanced topics.

**Final Goal:** Build enough NumPy proficiency to manipulate numerical data confidently and move on to Pandas, exploratory data analysis (EDA), statistics, and machine learning.

---

*Learning by coding, practicing, and building projects — one concept at a time.* 🚀
