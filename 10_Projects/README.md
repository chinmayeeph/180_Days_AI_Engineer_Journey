# 🚀 AI/ML Engineering Projects Portfolio

Welcome to my **AI/ML Engineering Projects Portfolio**!

This folder brings together practical projects developed throughout my journey in Python, Data Analysis, Machine Learning, Deep Learning, Natural Language Processing, Generative AI, Retrieval-Augmented Generation (RAG), and AI Agents.

The goal is to transform theoretical knowledge into working applications that solve practical problems and demonstrate my ability to design, implement, test, document, and improve AI-driven solutions.

Each project will include a clear problem statement, implementation, evaluation, documentation, and reproducible instructions wherever applicable.

> **Portfolio principle:** Build projects that demonstrate understanding, not just the ability to follow a tutorial.

---

## 🎯 Portfolio Objectives

Through these projects, I aim to demonstrate the ability to:

- Write clean, reusable, and maintainable Python code.
- Analyze datasets and communicate meaningful insights.
- Clean data and build reliable data-processing workflows.
- Train and evaluate Machine Learning models.
- Build Deep Learning and NLP applications.
- Develop LLM-powered applications and RAG systems.
- Connect AI models to tools and controlled workflows.
- Evaluate performance, reliability, and limitations.
- Build APIs and end-to-end AI applications.
- Apply testing, version control, and reproducible development practices.
- Document technical decisions and communicate results professionally.

---

## 📂 Repository Structure

```text
10_Projects/
│
├── README.md
│
├── 01_Python_Projects/
│   ├── personal_expense_analyzer/
│   │   └── README.md
│   └── student_performance_analyzer/
│       └── README.md
│
├── 02_Data_Analysis_Projects/
│   └── sales_data_analysis_dashboard/
│       └── README.md
│
├── 03_Machine_Learning_Projects/
│   ├── house_price_prediction/
│   │   └── README.md
│   ├── customer_churn_prediction/
│   │   └── README.md
│   └── customer_segmentation/
│       └── README.md
│
├── 04_Deep_Learning_NLP_Projects/
│   ├── image_classification_system/
│   │   └── README.md
│   ├── sentiment_analysis_system/
│   │   └── README.md
│   └── transformer_text_classifier/
│       └── README.md
│
├── 05_GenAI_RAG_Projects/
│   ├── pdf_research_assistant/
│   │   └── README.md
│   ├── ai_document_qa/
│   │   └── README.md
│   └── multi_document_assistant/
│       └── README.md
│
├── 06_Agent_Projects/
│   ├── ai_research_agent/
│   │   └── README.md
│   └── ai_data_analyst_agent/
│       └── README.md
│
├── 07_End_to_End_AI_Applications/
│   └── README.md
│
└── 08_Portfolio_Showcase/
    └── README.md
```

*Note: The nested README files are suggested conventions for documenting each project. Add them when you start each project. Git does not track empty folders, so a folder must contain a file to appear in GitHub.*

---

## 🗺️ Project Roadmap

Projects are grouped by technical area, progressing from Python fundamentals to complete AI applications.

| Stage | Category | Main Skills | Status |
|---|---|---|---|
| 1 | Python Projects | Python, functions, files, data structures | Planned |
| 2 | Data Analysis Projects | Pandas, EDA, visualization, reporting | Planned |
| 3 | Machine Learning Projects | Scikit-learn, feature engineering, evaluation | Planned |
| 4 | Deep Learning and NLP | Neural networks, PyTorch, text and image models | Planned |
| 5 | Generative AI and RAG | LLMs, embeddings, retrieval, citations | Planned |
| 6 | AI Agents | Tool calling, workflows, controlled execution | Planned |
| 7 | End-to-End AI Applications | Integration, APIs, testing, deployment | Planned |
| 8 | Portfolio Showcase | Project presentation, documentation, demos | Planned |

---

# 01 — Python Projects

## Project 1: Personal Expense Analyzer

**Objective:** Build a Python application to record, categorize, and analyze personal expenses.

### Key features
- Add and view expenses.
- Categorize transactions.
- Filter by date or category.
- Calculate total and average expenses.
- Identify the highest spending categories.
- Generate monthly summaries.
- Read and save data using CSV or JSON.
- Validate user input and handle invalid records.

### Suggested implementation
1. Define the expense data structure.
2. Implement functions for adding and listing transactions.
3. Add input validation.
4. Implement filtering and summary calculations.
5. Store and load data from a file.
6. Write tests for important calculations.
7. Create a sample report with fictional data.

### Deliverables
- Python source code.
- Sample dataset.
- Tests.
- README with setup instructions.
- Example output or screenshots.

## Project 2: Student Performance Analyzer

**Objective:** Analyze student marks and produce useful performance summaries.

### Key features
- Load marks from a CSV file.
- Calculate total marks, averages, and percentages.
- Assign grades using documented rules.
- Identify top-performing and struggling subjects.
- Summarize class performance.
- Handle missing or invalid marks.
- Export results to a new file.

### Suggested implementation
1. Create a sample student dataset.
2. Load and validate the data.
3. Implement reusable calculation functions.
4. Calculate student-level and subject-level statistics.
5. Generate a summary report.
6. Test calculations using known examples.

### Deliverables
- Python scripts.
- Sample CSV dataset.
- Unit tests.
- Example report.
- Project documentation.

---

# 02 — Data Analysis Projects

## Project 3: Sales Data Analysis Dashboard

**Objective:** Analyze sales data and present business insights through visualizations and a dashboard.

### Key features
- Load and inspect sales data.
- Clean missing, duplicated, and invalid records.
- Calculate revenue and order metrics.
- Analyze monthly and regional sales.
- Identify top products and categories.
- Compare sales trends over time.
- Create charts and a dashboard.
- Summarize business findings and recommendations.

### Suggested tools
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Power BI, Streamlit, or another suitable dashboard tool

### Suggested implementation
1. Define the business questions.
2. Inspect and clean the dataset.
3. Perform exploratory data analysis.
4. Calculate key performance indicators.
5. Create visualizations.
6. Build the dashboard.
7. Validate the numbers against the source data.
8. Write an insight report.

### Deliverables
- Dataset source and data dictionary.
- Data cleaning and analysis code.
- Visualizations or dashboard.
- Key findings.
- Setup instructions and screenshots.

---

# 03 — Machine Learning Projects

## Project 4: House Price Prediction

**Objective:** Train a regression model to estimate house prices from relevant property features.

### Key concepts
- Exploratory data analysis.
- Missing-value handling.
- Categorical encoding.
- Feature scaling where appropriate.
- Train, validation, and test splits.
- Regression algorithms.
- MAE, RMSE, and \(R^2\).
- Residual analysis.
- Model saving and inference.

### Suggested implementation
1. Select a suitable, documented dataset.
2. Inspect the target and feature distributions.
3. Establish a simple baseline.
4. Build a preprocessing and modeling pipeline.
5. Train and compare suitable regression models.
6. Evaluate on held-out data.
7. Investigate prediction errors.
8. Save the final model and create a prediction example.

### Deliverables
- Reproducible training pipeline.
- Evaluation report.
- Saved model or instructions to recreate it.
- Example predictions.
- Discussion of limitations.

## Project 5: Customer Churn Prediction

**Objective:** Predict which customers may discontinue a service using historical customer data.

### Key concepts
- Binary classification.
- Class imbalance.
- Feature engineering.
- Data leakage prevention.
- Logistic regression and tree-based models.
- Precision, recall, F1-score, and ROC-AUC.
- Confusion matrix.
- Threshold selection.
- Model interpretation.

### Suggested implementation
1. Define the churn target and prediction task.
2. Inspect class balance and feature quality.
3. Create leakage-safe train/test splits.
4. Build a baseline classifier.
5. Compare suitable classification models.
6. Evaluate precision, recall, and other relevant metrics.
7. Investigate false positives and false negatives.
8. Explain how predictions could support retention decisions.

### Deliverables
- Training and evaluation code.
- Model comparison report.
- Confusion matrix and metrics.
- Feature interpretation.
- Documented assumptions and limitations.

## Project 6: Customer Segmentation

**Objective:** Group customers with similar characteristics to explore customer behavior and potential business opportunities.

### Key concepts
- Unsupervised learning.
- Data scaling.
- K-Means clustering.
- Cluster selection.
- PCA for visualization where useful.
- Silhouette score.
- Cluster profiling.
- Business interpretation.

### Suggested implementation
1. Select a customer dataset.
2. Choose relevant segmentation features.
3. Clean and scale features where appropriate.
4. Establish a clustering baseline.
5. Compare a reasonable range of cluster configurations.
6. Profile the resulting clusters.
7. Visualize differences.
8. Explain what the segments may mean and where uncertainty remains.

### Deliverables
- Clustering pipeline.
- Cluster visualizations.
- Segment profiles.
- Evaluation metrics.
- Business interpretation and limitations.

---

# 04 — Deep Learning and NLP Projects

## Project 7: Image Classification System

**Objective:** Build a model that assigns images to predefined categories.

### Key concepts
- Image preprocessing.
- Dataset splits.
- PyTorch or another suitable deep learning framework.
- Neural network fundamentals.
- CNNs and transfer learning.
- Training and validation.
- Accuracy and per-class metrics.
- Confusion matrix.
- Overfitting and augmentation.

### Suggested implementation
1. Select a permitted image dataset.
2. Inspect class balance and image quality.
3. Create training, validation, and test splits.
4. Establish a baseline.
5. Train a CNN or adapt a pretrained model.
6. Evaluate class-level performance.
7. Inspect incorrect predictions.
8. Save the model and demonstrate inference on new images.

### Deliverables
- Training and inference code.
- Evaluation report.
- Example predictions.
- Model configuration and reproducibility instructions.

## Project 8: Sentiment Analysis System

**Objective:** Classify text into sentiment categories, such as positive, negative, or neutral, according to the chosen dataset and labeling scheme.

### Key concepts
- Text cleaning.
- Tokenization.
- TF-IDF.
- Baseline text classification.
- Logistic regression or other suitable models.
- Transformer-based approaches.
- Precision, recall, F1-score.
- Error analysis.
- Class imbalance.

### Suggested implementation
1. Choose a labeled text dataset.
2. Inspect label quality and class balance.
3. Create leakage-safe dataset splits.
4. Train a simple TF-IDF baseline.
5. Compare a more advanced model if appropriate.
6. Evaluate per-class performance.
7. Inspect misclassified examples.
8. Create a reusable prediction function.

### Deliverables
- Text preprocessing pipeline.
- Baseline and model comparison.
- Evaluation report.
- Example predictions.
- Documented failure cases.

## Project 9: Transformer Text Classifier

**Objective:** Fine-tune or adapt a pretrained Transformer model for a text classification task.

### Key concepts
- Tokenizers and attention masks.
- Transformer architectures.
- Pretrained model selection.
- Dataset preparation.
- Fine-tuning fundamentals.
- Training and validation.
- Learning rates and batch sizes.
- Evaluation metrics.
- Resource constraints.
- Model cards and licenses.

### Suggested implementation
1. Choose a suitable dataset and pretrained model.
2. Review model licensing and requirements.
3. Tokenize the dataset.
4. Establish a simple baseline.
5. Fine-tune within available compute resources.
6. Evaluate on held-out data.
7. Compare against the baseline.
8. Document the model, configuration, and limitations.

### Deliverables
- Training or inference code.
- Model and tokenizer configuration.
- Evaluation results.
- Reproducible setup instructions.
- Model and dataset references.

---

# 05 — Generative AI and RAG Projects

## Project 10: PDF Research Assistant

**Objective:** Build an assistant that answers questions about a PDF and identifies the source passages supporting its responses.

### Key features
- PDF text extraction.
- Page-level metadata.
- Document chunking.
- Embedding generation.
- Vector retrieval.
- Context-grounded answers.
- Page references or source excerpts.
- Handling of unsupported questions.
- Evaluation dataset.

### Suggested implementation
1. Load and inspect a PDF.
2. Extract text while preserving page references.
3. Clean and split the extracted text.
4. Create embeddings and a searchable index.
5. Retrieve relevant passages for a query.
6. Generate an answer using retrieved context.
7. Display sources with the answer.
8. Evaluate retrieval and answer quality.

### Deliverables
- Working document-question-answering pipeline.
- Source-grounded responses.
- Evaluation examples.
- Documentation of extraction and retrieval limitations.

## Project 11: AI Document QA

**Objective:** Create a reusable question-answering application over a collection of documents.

### Key features
- Document ingestion.
- Configurable chunking.
- Embedding model selection.
- Vector search.
- Context construction.
- LLM response generation.
- Source references.
- Error handling.
- Retrieval and answer evaluation.

### Suggested implementation
1. Choose a small, documented document collection.
2. Build a reusable ingestion pipeline.
3. Generate and store document embeddings.
4. Implement retrieval.
5. Connect retrieved context to an LLM.
6. Add source references.
7. Test answerable and unanswerable questions.
8. Compare alternative retrieval settings.

### Deliverables
- Modular RAG application.
- Evaluation dataset.
- Retrieval and answer-quality report.
- Usage instructions and known limitations.

## Project 12: Multi-Document Assistant

**Objective:** Answer questions across multiple documents while tracking evidence and handling conflicting information.

### Key features
- Multiple-document ingestion.
- Source and metadata management.
- Search across documents.
- Multi-document synthesis.
- Citation or source references.
- Handling conflicting statements.
- Document updates and re-indexing.
- Retrieval evaluation.

### Suggested implementation
1. Ingest multiple documents.
2. Assign stable document identifiers.
3. Extract text and metadata.
4. Build the retrieval index.
5. Retrieve evidence for user questions.
6. Generate answers with source references.
7. Test questions requiring multiple sources.
8. Evaluate citation correctness and evidence coverage.

### Deliverables
- Multi-document retrieval pipeline.
- Question-answering interface.
- Source-linked responses.
- Evaluation report.
- Instructions for updating the document collection.

---

# 06 — AI Agent Projects

## Project 13: AI Research Agent

**Objective:** Build a controlled agent that gathers information from approved sources and creates a structured research report.

### Key features
- Task decomposition.
- Research planning.
- Approved search or retrieval tools.
- Tool calling.
- Source tracking.
- Evidence comparison.
- Report generation.
- Verification steps.
- Execution limits.
- Human review.

### Suggested implementation
1. Define a narrow research task.
2. Establish the permitted sources and tools.
3. Design tool schemas and input validation.
4. Implement a bounded workflow.
5. Collect and preserve evidence.
6. Generate a structured report.
7. Verify key claims against sources.
8. Test failure cases and record tool usage.

### Deliverables
- Research workflow or agent.
- Tool documentation.
- Source-linked reports.
- Evaluation test cases.
- Safety and limitations report.

The agent must distinguish retrieved evidence from generated interpretation. It should not claim that a statement has been verified unless a defined verification step supports that claim.

## Project 14: AI Data Analyst Agent

**Objective:** Build an assistant that uses controlled data-analysis tools to answer questions about a dataset and produce reproducible findings.

### Key features
- Dataset loading and inspection.
- Data quality checks.
- Natural-language analytical questions.
- Controlled Python analysis functions.
- Summary statistics.
- Visualizations.
- Validated calculations.
- Report generation.
- Error handling.
- Audit trail.

### Suggested implementation
1. Choose a sample CSV dataset.
2. Build data-inspection functions.
3. Add tools for approved calculations and visualizations.
4. Define input and output schemas.
5. Connect an LLM to the tools.
6. Validate analytical results against the data.
7. Generate a structured report.
8. Test incorrect assumptions, invalid inputs, and tool failures.

### Deliverables
- Reusable data-analysis tools.
- Agent or workflow implementation.
- Example reports and charts.
- Test cases and evaluation results.
- Documentation of permissions and limitations.

**Safety requirement:** Do not give an LLM unrestricted execution access. Use allowlisted operations, validate inputs, restrict permissions, and isolate any execution of generated code.

---

# 07 — End-to-End AI Applications

**Objective:** Integrate the skills from previous projects into complete, usable applications.

This category will contain larger projects that combine data preparation, model or LLM integration, application logic, testing, and deployment.

### Future project ideas

- Customer support assistant with RAG.
- Document intelligence application.
- AI-powered sales insights application.
- ML prediction service with a REST API.
- Customer churn analysis and prediction platform.
- Research assistant with evidence verification.
- Data analyst application with charts and reports.
- Knowledge assistant with document management.
- AI application with user authentication and access controls.
- Model monitoring and evaluation dashboard.

### Suggested architecture

```text
User Interface
      |
      v
Application API
      |
      v
Validation and Business Logic
      |
      +----------------------+
      |                      |
      v                      v
ML / LLM Service       Data / Retrieval Layer
      |                      |
      +-----------+----------+
                  |
                  v
       Evaluation and Logging
                  |
                  v
          Results to User
```

### Engineering requirements

- Clear application architecture.
- Separation of business logic and model code.
- Input validation.
- Configuration and secret management.
- Automated tests.
- Logging and error handling.
- Model or prompt evaluation.
- Reproducible installation.
- Performance and cost awareness.
- Deployment instructions.
- Privacy and security considerations.

A deployed application should be described as production-ready only when its reliability, security, monitoring, and operational requirements have actually been assessed.

---

# 08 — Portfolio Showcase

**Objective:** Present selected projects clearly so that recruiters, engineers, and other reviewers can understand the problem, approach, results, and technical decisions.

### Each featured project should include

- [ ] A clear problem statement.
- [ ] A concise project overview.
- [ ] A documented dataset or data source.
- [ ] The tools and technologies used.
- [ ] A clear implementation workflow.
- [ ] Setup and execution instructions.
- [ ] Tests and evaluation methodology.
- [ ] Actual results and relevant metrics.
- [ ] Visualizations, screenshots, or a demo where useful.
- [ ] Limitations and future improvements.
- [ ] A clean GitHub repository.
- [ ] A license or source attribution where appropriate.

### Portfolio presentation principles

1. **Prioritize depth over quantity.** A small number of well-tested projects is stronger than many incomplete repositories.
2. **Explain decisions.** Document why a model, metric, retrieval strategy, or architecture was chosen.
3. **Report real results.** Never invent accuracy, speed, cost savings, or business impact.
4. **Show the baseline.** Explain what improved and how that improvement was measured.
5. **Make projects reproducible.** Include requirements, configuration guidance, and sample inputs where possible.
6. **Be transparent.** Identify limitations, known failures, and areas that need more work.
7. **Keep sensitive information private.** Never publish API keys, private datasets, or confidential information.

---

## 🧰 Recommended Project Folder Convention

As individual projects become more complex, consider organizing them like this:

```text
project_name/
├── README.md
├── src/
├── tests/
├── data/
├── notebooks/
├── reports/
├── requirements.txt
├── .env.example
├── .gitignore
└── LICENSE
```

Use only the directories needed for each project. Keep raw data, processed data, and generated outputs clearly distinguished. Do not commit large datasets, model weights, credentials, or restricted material without confirming that sharing is permitted.

---

## 🧪 General Quality Checklist

Before considering any project complete:

- [ ] The problem and intended user are clearly defined.
- [ ] The solution runs using documented instructions.
- [ ] The code is organized and understandable.
- [ ] Inputs and edge cases are handled appropriately.
- [ ] Important functions have tests.
- [ ] Data preparation and evaluation are reproducible.
- [ ] The evaluation method matches the task.
- [ ] Results are reported accurately.
- [ ] Known limitations are documented.
- [ ] Secrets and sensitive information are protected.
- [ ] The README explains how to run the project.
- [ ] Screenshots, examples, or a demo are included when useful.
- [ ] The repository is ready for another developer to inspect.

---

## 📊 Portfolio Progress Tracker

All projects start with the status **Planned**.

| Project | Status |
|---|---|
| Personal Expense Analyzer | Planned |
| Student Performance Analyzer | Planned |
| Sales Data Analysis Dashboard | Planned |
| House Price Prediction | Planned |
| Customer Churn Prediction | Planned |
| Customer Segmentation | Planned |
| Image Classification System | Planned |
| Sentiment Analysis System | Planned |
| Transformer Text Classifier | Planned |
| PDF Research Assistant | Planned |
| AI Document QA | Planned |
| Multi-Document Assistant | Planned |
| AI Research Agent | Planned |
| AI Data Analyst Agent | Planned |
| End-to-End AI Applications | Planned |
| Portfolio Showcase | Planned |

**Projects completed:** 0

Update this tracker only when projects meet their documented completion criteria. A project should not be marked complete merely because a tutorial was watched or code was copied.

---

## 🚀 Getting Started

### Step 1 — Choose a manageable project

Start with the Personal Expense Analyzer or Student Performance Analyzer to practice Python fundamentals.

### Step 2 — Define the requirements

Write down:
- What problem the project solves.
- What inputs it accepts.
- What outputs it produces.
- How correctness will be tested.
- What features are out of scope.

### Step 3 — Implement a small baseline

Build the simplest useful version first. Avoid adding unnecessary frameworks or advanced features before the core logic works.

### Step 4 — Test and improve

Use known examples, edge cases, and representative datasets. Record failures and improve the implementation based on evidence.

### Step 5 — Document and publish

Write the README, add setup instructions, remove secrets, test the documented workflow, and push the work to GitHub.

### Step 6 — Iterate

Add features only when they improve usability, correctness, performance, or learning value.

---

## 🎯 Final Goal

Build a professional portfolio demonstrating the journey from **Python programming and data analysis to Machine Learning, Deep Learning, Generative AI, RAG, AI Agents, and complete AI applications**.

The objective is not simply to collect projects. It is to demonstrate the ability to understand a problem, choose a suitable approach, build a solution, evaluate its behavior, explain the results, and improve it responsibly.

**Learn the fundamentals. Build the solution. Test the results. Explain the decisions. Ship responsibly.** 🚀

---

*This portfolio is a work in progress. Project descriptions define intended goals and possible approaches, not claims of completed implementation or measured performance.*
