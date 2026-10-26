# 🗄️ SQL — Structured Query Language

Welcome to my **SQL Learning and Projects** repository!

This folder documents my journey of learning SQL for data analysis, data science, and AI/ML engineering. It covers database fundamentals, data retrieval, filtering, aggregations, joins, subqueries, Common Table Expressions (CTEs), window functions, data manipulation, and Python–SQL integration.

The goal is to develop strong SQL skills to retrieve, transform, analyze, and prepare data efficiently for real-world applications.

---

## 🎯 Learning Objectives

By completing this section, I aim to learn how to:

- Understand relational databases, tables, rows, columns, and keys.
- Write SQL queries to retrieve and filter data.
- Sort and limit query results.
- Aggregate data using functions such as `COUNT()`, `SUM()`, and `AVG()`.
- Group records and filter aggregated results.
- Combine tables using different types of joins.
- Write subqueries and reusable CTEs.
- Analyze data using window functions.
- Work with conditional, date, and string functions.
- Create and modify database objects and records.
- Practice SQL problem-solving with increasing difficulty.
- Connect Python to a database and execute SQL queries.
- Build portfolio projects that demonstrate practical analytical skills.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|---|---|
| SQL | Querying and managing relational data |
| SQLite | Beginner-friendly, file-based database |
| PostgreSQL | Relational database and advanced SQL practice |
| MySQL | Relational database practice |
| Python | Data processing and automation |
| Pandas | Working with query results |
| SQLAlchemy | Python database connectivity and SQL workflows |
| Jupyter Notebook | Interactive practice and analysis |
| VS Code | Writing and organizing code |
| Git and GitHub | Version control and portfolio development |

**Recommended starting point:** Begin with SQLite for simple local exercises, then learn PostgreSQL for more advanced queries and realistic database workflows. You do not need to learn every database system at once.

---

## 📂 Repository Structure

```text
06_SQL/
│
├── README.md
│
├── 01_SQL_Fundamentals/
│   ├── README.md
│   └── exercises/
│
├── 02_SELECT_WHERE_ORDER_BY/
│   ├── README.md
│   └── exercises/
│
├── 03_Aggregations_GROUP_BY_HAVING/
│   ├── README.md
│   └── exercises/
│
├── 04_JOINS/
│   ├── README.md
│   └── exercises/
│
├── 05_Subqueries_CTEs/
│   ├── README.md
│   └── exercises/
│
├── 06_Window_Functions/
│   ├── README.md
│   └── exercises/
│
├── 07_CASE_Date_String_Functions/
│   ├── README.md
│   └── exercises/
│
├── 08_Data_Definition_Manipulation/
│   ├── README.md
│   └── exercises/
│
├── 09_SQL_Exercises/
│   ├── README.md
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── 10_Python_SQL_Integration/
│   ├── README.md
│   ├── notebooks/
│   └── scripts/
│
└── projects/
    ├── README.md
    ├── student_database_analysis/
    ├── sales_database_analysis/
    ├── employee_database_analysis/
    ├── ecommerce_sql_analysis/
    └── customer_retention_analysis/
```

*Note: The nested README files and subfolders are suggested organizational conventions. Create them as needed. Git does not track empty directories, so add a file to any directory you want GitHub to display.*

---

## 📚 Learning Roadmap

### 01 — SQL Fundamentals

**Objective:** Understand how relational databases organize and store information.

Topics:
- What SQL is and why it is used.
- Relational databases, tables, rows, and columns.
- Primary keys and foreign keys.
- Relationships between tables.
- Database schemas.
- SQL syntax and statement structure.
- Data types and `NULL`.
- Basic database concepts and terminology.

Practice:
- Create a simple student database.
- Identify primary and foreign keys.
- Explore a database containing multiple related tables.

### 02 — SELECT, WHERE, ORDER BY

**Objective:** Retrieve exactly the records needed for analysis.

Topics:
- `SELECT` and `FROM`.
- Selecting individual and multiple columns.
- Column aliases using `AS`.
- `DISTINCT`.
- Filtering with `WHERE`.
- Comparison operators.
- `AND`, `OR`, and `NOT`.
- `IN`, `BETWEEN`, and `LIKE`.
- Handling `NULL` with `IS NULL` and `IS NOT NULL`.
- Sorting using `ORDER BY`.
- Limiting results using `LIMIT` or database-specific alternatives.

Practice:
- Find students above a particular score.
- Filter products within a price range.
- Identify unique categories.
- Sort sales records and retrieve the highest-value transactions.

### 03 — Aggregations, GROUP BY, HAVING

**Objective:** Summarize large datasets into useful metrics.

Topics:
- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, and `MAX()`.
- `GROUP BY`.
- Filtering groups with `HAVING`.
- Grouping by multiple columns.
- Counting distinct values.
- Conditional aggregation.
- Differences between `WHERE` and `HAVING`.
- Understanding aggregate results when values are `NULL`.

Practice:
- Calculate average marks by subject.
- Summarize revenue by product category.
- Find departments with more than a specified number of employees.
- Calculate monthly sales and order counts.

### 04 — JOINS

**Objective:** Combine information from related tables.

Topics:
- `INNER JOIN`.
- `LEFT JOIN`.
- `RIGHT JOIN`, where supported.
- `FULL OUTER JOIN`, where supported.
- `CROSS JOIN`.
- Self joins.
- Joining multiple tables.
- Table aliases.
- Joining on primary and foreign keys.
- Duplicate rows caused by join relationships.
- Identifying unmatched records.

Practice:
- Combine student and examination tables.
- Join customers, orders, and order items.
- Find customers who have never placed an order.
- Compare results from different join types.

### 05 — Subqueries and CTEs

**Objective:** Organize complex queries into understandable steps.

Topics:
- Scalar subqueries.
- Subqueries returning multiple rows.
- Correlated subqueries.
- `IN` and `EXISTS`.
- `NOT EXISTS`.
- Common Table Expressions using `WITH`.
- Multiple CTEs.
- Recursive CTE fundamentals.
- Comparing subqueries with joins and CTEs.

Practice:
- Find employees earning more than the company average.
- Identify products priced above their category average.
- Use CTEs to calculate and filter intermediate results.
- Break a complex business question into smaller query steps.

### 06 — Window Functions

**Objective:** Perform calculations across related rows without collapsing the result into one row per group.

Topics:
- `OVER()`.
- `PARTITION BY`.
- `ORDER BY` within a window.
- `ROW_NUMBER()`.
- `RANK()` and `DENSE_RANK()`.
- `LAG()` and `LEAD()`.
- Running totals.
- Moving averages.
- Window aggregates.
- Ranking within categories.
- Differences between window functions and `GROUP BY`.

Practice:
- Rank products by revenue within each category.
- Calculate cumulative monthly sales.
- Compare each month's sales with the previous month.
- Identify the top three employees by salary in each department.

### 07 — CASE, Date, and String Functions

**Objective:** Transform and categorize values directly in SQL.

Topics:
- `CASE WHEN`.
- Conditional labels and classifications.
- Date extraction and date arithmetic.
- Date filtering and grouping by month or year.
- String concatenation.
- `LOWER()` and `UPPER()`.
- `TRIM()`.
- `LENGTH()`.
- `SUBSTRING()` or database-specific equivalents.
- Replacing text and formatting values.
- Handling missing or inconsistent text values.

Practice:
- Classify sales into performance categories.
- Calculate order counts by month.
- Standardize inconsistent text labels.
- Calculate the number of days between order and delivery dates.

*Function names and date syntax can vary between SQLite, PostgreSQL, and MySQL.*

### 08 — Data Definition and Manipulation

**Objective:** Understand how databases and their records are created and maintained.

Topics:
- `CREATE TABLE`.
- `ALTER TABLE`.
- `DROP TABLE`.
- `INSERT INTO`.
- `UPDATE`.
- `DELETE`.
- Primary key and foreign key constraints.
- `NOT NULL`, `UNIQUE`, and `CHECK`.
- Views.
- Index fundamentals.
- Transactions and rollback.
- Basic database integrity.

Practice:
- Create a small relational database.
- Insert sample records.
- Update records and validate the result.
- Define constraints that prevent invalid data.

**Safety rule:** Practice destructive operations such as `UPDATE`, `DELETE`, and `DROP` only on a test database. Use transactions and backups where appropriate.

### 09 — SQL Exercises

**Objective:** Develop problem-solving ability through regular practice.

**Beginner:**
- Retrieve selected columns.
- Filter and sort rows.
- Use comparison and logical operators.
- Handle `NULL` values.
- Calculate basic aggregates.
- Group and summarize data.

**Intermediate:**
- Join multiple tables.
- Use conditional aggregation.
- Write subqueries and CTEs.
- Compare groups and categories.
- Use date and string functions.
- Find missing relationships.

**Advanced:**
- Use ranking and window functions.
- Calculate running totals and period-over-period changes.
- Solve top-N-per-group problems.
- Analyze retention and cohorts.
- Write multi-step analytical queries.
- Compare alternative query approaches.

For every exercise, document:
1. The problem statement.
2. The SQL query.
3. The expected or observed result.
4. A short explanation of the approach.
5. Any assumptions or edge cases.

### 10 — Python and SQL Integration

**Objective:** Combine SQL querying with Python-based analysis and automation.

Topics:
- Connecting Python to SQLite.
- Connecting to PostgreSQL when ready.
- Executing SQL statements from Python.
- Parameterized queries.
- Retrieving query results.
- Working with Pandas DataFrames.
- Reading SQL query results into Pandas.
- Writing DataFrames to database tables.
- Managing database connections and transactions.
- Handling exceptions.
- Separating credentials from source code.
- Automating repeatable analytical workflows.

Practice:
- Load a CSV file into SQLite.
- Query the database from Python.
- Convert SQL query results into a Pandas DataFrame.
- Generate an analytical report from database results.
- Build a reusable Python script for repeated queries.

**Security note:** Use parameterized queries rather than constructing SQL statements by concatenating untrusted user input.

---

## 🧪 Portfolio Projects

All projects begin with **Planned** status. I will update their status only after completing the work and documenting the results.

| # | Project | Key Skills | Status |
|---|---|---|---|
| 1 | Student Database Analysis | Filtering, aggregation, joins | Planned |
| 2 | Sales Database Analysis | Revenue analysis, grouping, window functions | Planned |
| 3 | Employee Database Analysis | Joins, subqueries, ranking | Planned |
| 4 | E-Commerce SQL Analysis | Multi-table joins, order analysis, CTEs | Planned |
| 5 | Customer Retention Analysis | Dates, cohorts, window functions | Planned |

### Project 1 — Student Database Analysis

**Goal:** Analyze student performance across subjects, classes, and examinations.

Potential analysis:
- Average marks by student and subject.
- Highest and lowest scores.
- Pass rates and performance categories.
- Subject-level comparisons.
- Ranking students within a class.
- Identifying missing or inconsistent records.

Deliverables:
- Database schema and sample data.
- SQL query files.
- Documented results.
- Findings summary.

### Project 2 — Sales Database Analysis

**Goal:** Understand sales performance and identify important business trends.

Potential analysis:
- Revenue by month and category.
- Best-selling products.
- Average order value.
- Customer purchase frequency.
- Month-over-month changes.
- Running totals and product rankings.

Deliverables:
- Database tables and relationships.
- Reusable analytical queries.
- Results and explanations.
- Optional Python visualizations.

### Project 3 — Employee Database Analysis

**Goal:** Explore employee and department information using relational queries.

Potential analysis:
- Employee counts by department.
- Salary summaries.
- Employees earning above department averages.
- Department-level rankings.
- Missing department assignments.
- Comparisons between employee groups.

Deliverables:
- Sample employee database.
- SQL queries using joins, CTEs, and window functions.
- Documented findings.

### Project 4 — E-Commerce SQL Analysis

**Goal:** Investigate customer orders, products, and transaction behavior.

Potential analysis:
- Order volume and revenue.
- Product and category performance.
- Average order value.
- Repeat purchasing.
- Customers without orders.
- Monthly sales trends.
- Cancellation or return patterns, if the dataset contains them.

Deliverables:
- Relational database schema.
- Multi-table SQL analysis.
- Query results and insights.
- Optional Python-based visual report.

### Project 5 — Customer Retention Analysis

**Goal:** Understand how customer purchasing behavior changes over time.

Potential analysis:
- First purchase date.
- Repeat purchase rate.
- Monthly customer cohorts.
- Customer retention by cohort.
- Time between purchases.
- Customer activity trends.

Deliverables:
- SQL queries for cohort analysis.
- Retention tables.
- Explanation of the methodology.
- Findings and limitations.

*The analyses and findings will be based on the actual dataset. No business conclusions will be assumed before the queries are run.*

---

## 📏 SQL Practice Checklist

Use this checklist as I progress through the roadmap.

- [ ] Understand relational database fundamentals.
- [ ] Write `SELECT` queries confidently.
- [ ] Filter and sort query results.
- [ ] Calculate aggregates and group records.
- [ ] Use `HAVING` correctly.
- [ ] Understand and apply joins.
- [ ] Write subqueries and CTEs.
- [ ] Use window functions.
- [ ] Work with conditional, date, and string functions.
- [ ] Create and manipulate database tables safely.
- [ ] Complete beginner, intermediate, and advanced exercises.
- [ ] Connect Python to a database.
- [ ] Analyze query results using Pandas.
- [ ] Complete and document portfolio projects.

---

## 📈 Progress Tracker

| Learning Area | Status |
|---|---|
| SQL Fundamentals | Planned |
| SELECT, WHERE, ORDER BY | Planned |
| Aggregations, GROUP BY, HAVING | Planned |
| Joins | Planned |
| Subqueries and CTEs | Planned |
| Window Functions | Planned |
| CASE, Date, String Functions | Planned |
| Data Definition and Manipulation | Planned |
| SQL Exercises | Planned |
| Python–SQL Integration | Planned |
| Student Database Analysis | Planned |
| Sales Database Analysis | Planned |
| Employee Database Analysis | Planned |
| E-Commerce SQL Analysis | Planned |
| Customer Retention Analysis | Planned |

**Projects completed:** 0

Progress will be updated as I complete exercises, save working SQL scripts, validate results, and document each project.

---

## 🚀 Getting Started

### Option 1 — Start with SQLite

SQLite is a practical choice for beginner exercises because it can store a database in a local file without requiring a separate database server.

Recommended workflow:
1. Install or use a SQLite-compatible tool.
2. Create a small practice database.
3. Define tables and insert sample records.
4. Practice SQL queries against the database.
5. Save queries in `.sql` files.
6. Document results and observations.

### Option 2 — Use Python

Install the core libraries when needed:

```bash
python -m pip install pandas sqlalchemy
```

SQLite support is included with Python through the built-in `sqlite3` module. A separate database driver may be required for PostgreSQL or MySQL.

---

## 📌 Learning Principles

- Write queries yourself before looking at solutions.
- Understand why a query works instead of memorizing syntax.
- Check row counts after joins to catch unexpected duplication.
- Handle `NULL` values intentionally.
- Test queries on small datasets before scaling up.
- Use clear aliases and formatting.
- Compare results against simple manual checks when possible.
- Prefer readable queries before attempting premature optimization.
- Never expose database passwords, API keys, or private data in GitHub.
- Document assumptions and limitations in every project.

---

## 🎯 Final Goal

Build a strong SQL foundation for **Data Analytics, Data Science, Machine Learning, and AI Engineering**.

By the end of this learning journey, I aim to confidently query relational databases, solve analytical problems, work with real-world datasets, integrate SQL with Python, and present well-documented projects in my GitHub portfolio.

**Learn the fundamentals. Practice consistently. Solve real problems. Build reliable analytical skills.** 🚀

---

*This repository is a work in progress. All roadmap items remain planned until the corresponding exercises or projects are completed and documented.*
