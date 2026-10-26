# 🧠 Generative AI — LLMs, RAG, AI Agents & Projects

Welcome to my **Generative AI Learning and Projects** repository!

This folder documents my journey of learning Generative AI engineering, from understanding Large Language Models (LLMs) and prompt engineering to building Retrieval-Augmented Generation (RAG) applications, connecting models to tools, and developing AI agents.

The goal is to move beyond simply calling an LLM API and learn how to build useful, reliable, evaluated, and maintainable AI applications.

This section combines theoretical foundations, hands-on exercises, experiments, and end-to-end portfolio projects using Python and the modern GenAI ecosystem.

---

## 🎯 Learning Objectives

By completing this section, I aim to learn how to:

- Understand LLMs, their capabilities, and their limitations.
- Write, test, and improve prompts systematically.
- Work with hosted LLM APIs and locally available models.
- Understand tokenization, embeddings, and semantic similarity.
- Store and retrieve vector embeddings.
- Load documents and prepare them for retrieval.
- Build Retrieval-Augmented Generation (RAG) pipelines.
- Improve retrieval using filtering, hybrid search, and reranking.
- Evaluate retrieval quality and generated answers.
- Work with Hugging Face models and datasets.
- Use frameworks such as LangChain and LlamaIndex where appropriate.
- Understand fine-tuning and when it is useful.
- Connect LLMs to tools using structured tool calling.
- Build AI agents and multi-step workflows.
- Manage conversation memory, application state, and workflow execution.
- Evaluate agent behavior, reliability, and safety.
- Build end-to-end AI applications with clear documentation and reproducible results.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| LLM APIs | Accessing hosted language models |
| Hugging Face | Models, tokenizers, and datasets |
| Sentence Transformers | Generating text embeddings |
| FAISS | Efficient vector similarity search |
| Chroma | Vector storage and retrieval |
| LangChain | Components and orchestration for LLM applications |
| LlamaIndex | Data ingestion and retrieval-oriented applications |
| Pydantic | Structured output validation |
| FastAPI | Exposing AI functionality through APIs |
| Jupyter Notebook | Interactive experimentation |
| Git and GitHub | Version control and portfolio development |

**Recommended approach:** Learn the underlying concepts first, then introduce frameworks when they make a workflow easier to understand or maintain. Start with a small, working LLM application before building a complete RAG pipeline or agent.

Tool availability, APIs, model names, and framework interfaces can change. Use current official documentation when implementing each project.

---

## 📂 Repository Structure

```text
09_GenAI/
│
├── README.md
│
├── 01_LLM_Fundamentals/
│   ├── README.md
│   └── notebooks/
│
├── 02_Prompt_Engineering/
│   ├── README.md
│   └── notebooks/
│
├── 03_LLM_APIs_Local_Models/
│   ├── README.md
│   └── notebooks/
│
├── 04_Tokenization_Embeddings/
│   ├── README.md
│   └── notebooks/
│
├── 05_Vector_Databases/
│   ├── README.md
│   └── notebooks/
│
├── 06_Document_Loading_Chunking/
│   ├── README.md
│   └── notebooks/
│
├── 07_Retrieval_Augmented_Generation/
│   ├── README.md
│   └── notebooks/
│
├── 08_Retrieval_Reranking/
│   ├── README.md
│   └── notebooks/
│
├── 09_RAG_Evaluation/
│   ├── README.md
│   └── notebooks/
│
├── 10_Hugging_Face/
│   ├── README.md
│   └── notebooks/
│
├── 11_LangChain_LlamaIndex/
│   ├── README.md
│   └── notebooks/
│
├── 12_Fine_Tuning_Basics/
│   ├── README.md
│   └── notebooks/
│
├── 13_Tool_Calling/
│   ├── README.md
│   └── notebooks/
│
├── 14_AI_Agents/
│   ├── README.md
│   └── notebooks/
│
├── 15_Workflows_Memory_State/
│   ├── README.md
│   └── notebooks/
│
├── 16_Agent_Evaluation_Safety/
│   ├── README.md
│   └── notebooks/
│
├── 17_GenAI_Exercises/
│   ├── README.md
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── notebooks/
│   └── README.md
│
├── projects/
│   ├── README.md
│   │
│   ├── pdf_research_assistant/
│   │   └── README.md
│   │
│   ├── document_qa_rag/
│   │   └── README.md
│   │
│   ├── multi_document_knowledge_assistant/
│   │   └── README.md
│   │
│   ├── ai_research_agent/
│   │   └── README.md
│   │
│   └── ai_data_analyst_agent/
│       └── README.md
│
└── resources/
    └── README.md
```

*Note: Nested README files and notebook folders are suggested organizational conventions. Create them as needed. Git does not track empty directories, so add files to folders you want GitHub to display.*

---

## 📚 Learning Roadmap

### 01 — LLM Fundamentals

**Objective:** Understand what Large Language Models are and how they generate text.

Topics:
- Generative AI versus traditional Machine Learning.
- What Large Language Models do.
- High-level Transformer architecture.
- Pretraining and inference.
- Context windows and token limits.
- Parameters and model sizes.
- Temperature and sampling.
- System, user, and assistant messages.
- Model strengths and limitations.
- Hallucinations and uncertainty.
- Hosted models versus local models.
- Model latency, cost, and resource requirements.

Practice:
- Compare outputs from different prompts.
- Investigate how temperature changes responses.
- Observe how context length affects an application.
- Document examples of correct, incorrect, and unsupported answers.

### 02 — Prompt Engineering

**Objective:** Learn to give models clear instructions and systematically evaluate their responses.

Topics:
- Instruction clarity and task definition.
- System and user prompts.
- Zero-shot and few-shot prompting.
- Role and context specification.
- Prompt templates and reusable variables.
- Output formatting.
- Structured JSON outputs.
- Decomposition of complex tasks.
- Constraints and examples.
- Prompt iteration and versioning.
- Prompt injection awareness.
- Evaluation using representative examples.

Practice:
- Improve an ambiguous prompt.
- Compare zero-shot and few-shot approaches.
- Ask for structured output and validate it.
- Create a small prompt evaluation dataset.
- Record quality, consistency, and failure cases.

**Principle:** Prompt engineering should be evaluated with examples and measurable criteria, not just by whether one response looks impressive.

### 03 — LLM APIs and Local Models

**Objective:** Run language models through hosted APIs or locally available inference tools.

Topics:
- API requests and responses.
- Authentication and environment variables.
- Model selection.
- Timeouts and error handling.
- Rate limits and retries.
- Streaming responses.
- Token usage and cost estimation.
- Local model inference.
- Quantization fundamentals.
- Hardware and memory constraints.
- Latency and throughput.
- Provider abstraction and model configuration.

Practice:
- Build a simple command-line LLM application.
- Read API keys from environment variables.
- Handle timeouts and API errors.
- Compare the latency and output quality of suitable models.
- Run a small local model if hardware permits.

**Security:** Never commit API keys, access tokens, or other secrets to GitHub. Use environment variables and a local `.env` file excluded through `.gitignore`.

### 04 — Tokenization and Embeddings

**Objective:** Understand how text is represented numerically for language modeling and semantic retrieval.

Topics:
- Tokens and token IDs.
- Subword tokenization.
- Vocabulary and special tokens.
- Context length and token counts.
- Embedding vectors.
- Vector dimensions.
- Cosine similarity.
- Dot-product similarity.
- Semantic versus lexical similarity.
- Embedding model selection.
- Embedding normalization.
- Limitations across languages and domains.

Practice:
- Inspect tokenization for different sentences.
- Compare token counts.
- Generate embeddings for short text samples.
- Calculate similarity between related and unrelated texts.
- Investigate how embedding choice affects retrieval.

### 05 — Vector Databases

**Objective:** Store, index, and retrieve vector representations efficiently.

Topics:
- Vector storage and similarity search.
- Embeddings and document IDs.
- Metadata filtering.
- Distance and similarity metrics.
- Exact versus approximate nearest-neighbor search.
- Indexing fundamentals.
- Collections and namespaces.
- Upserting and deleting records.
- Persistence and data updates.
- Retrieval performance.
- Vector database limitations.

Practice:
- Store sample document embeddings.
- Retrieve the nearest matching documents.
- Filter results using metadata.
- Compare a simple NumPy similarity search with a vector database.
- Measure retrieval speed on a small dataset.

### 06 — Document Loading and Chunking

**Objective:** Convert documents into clean, retrievable text segments.

Topics:
- Reading text and Markdown files.
- PDF document extraction.
- HTML and other document formats.
- Document metadata.
- Text cleaning.
- Chunk size and overlap.
- Recursive and structure-aware splitting.
- Headers and section boundaries.
- Tables and structured content.
- Document identifiers.
- Duplicate detection.
- Source tracking.
- Incremental indexing.

Practice:
- Extract text from a PDF.
- Split a document using different chunk sizes.
- Compare fixed-size and structure-aware chunking.
- Preserve page numbers and source metadata.
- Inspect extraction errors and missing content.

### 07 — Retrieval-Augmented Generation (RAG)

**Objective:** Build applications that use retrieved external information to help generate grounded answers.

Topics:
- RAG architecture.
- Document ingestion.
- Chunking and embeddings.
- Index creation.
- Query embedding.
- Similarity search.
- Context construction.
- Prompting with retrieved context.
- Answer generation.
- Source attribution and citations.
- Handling insufficient evidence.
- Retrieval versus generation failures.
- Updating and rebuilding indexes.

Practice:
- Build a RAG pipeline over a small document collection.
- Ask questions that are answerable from the documents.
- Ask questions that are not answered by the documents.
- Inspect retrieved chunks for each question.
- Display source references alongside answers.

### 08 — Retrieval and Reranking

**Objective:** Improve the relevance of documents supplied to an LLM.

Topics:
- Query formulation.
- Dense retrieval.
- Keyword-based retrieval.
- Hybrid retrieval.
- Metadata filtering.
- Top-k retrieval.
- Candidate generation.
- Cross-encoder reranking.
- Query expansion and rewriting.
- Multi-query retrieval.
- Retrieval diversity.
- Context compression.
- Latency and relevance trade-offs.

Practice:
- Compare dense and keyword retrieval.
- Measure retrieval results at different top-k values.
- Compare retrieved rankings before and after reranking.
- Examine whether additional retrieved chunks improve answer quality.

### 09 — RAG Evaluation

**Objective:** Measure the quality and reliability of retrieval and generated answers.

Topics:
- Building representative evaluation questions.
- Ground-truth answers and source documents.
- Retrieval precision and recall.
- Hit rate and ranking metrics.
- Answer correctness.
- Context relevance.
- Faithfulness to retrieved evidence.
- Citation correctness.
- Handling unanswerable questions.
- Human evaluation.
- Automated evaluation and its limitations.
- Regression testing.
- Latency and cost measurement.

Practice:
- Create a small RAG evaluation dataset.
- Compare retrieval configurations.
- Review incorrect answers and unsupported claims.
- Measure the effect of chunking and reranking.
- Create a report of strengths, weaknesses, and failure cases.

**Important:** Automated evaluation scores are useful signals, not absolute proof of quality. Review representative examples manually.

### 10 — Hugging Face

**Objective:** Use the Hugging Face ecosystem to access models, tokenizers, and datasets.

Topics:
- Hugging Face Hub.
- Model and tokenizer loading.
- Text-generation pipelines.
- Embedding models.
- Dataset loading.
- Model inference.
- Model cards and dataset documentation.
- Model licenses and usage restrictions.
- Resource requirements.
- Quantization and local inference options.
- Reproducible model configurations.

Practice:
- Load a suitable pretrained model.
- Generate text or classify text.
- Inspect tokenization.
- Generate embeddings using an appropriate model.
- Compare two models on the same small evaluation set.

### 11 — LangChain and LlamaIndex

**Objective:** Understand frameworks that help organize LLM applications and data workflows.

Topics:
- Prompt templates.
- Model interfaces.
- Output parsers.
- Document loaders.
- Text splitters.
- Retrieval components.
- Chains and workflow composition.
- Indexing and query engines.
- Tool integration.
- Tracing and debugging.
- Framework abstractions versus direct Python implementations.
- Version compatibility.

Practice:
- Rebuild a simple LLM application using a framework.
- Implement a basic RAG pipeline.
- Compare framework-based and direct implementations.
- Document what the framework simplifies and what it hides.

**Learning principle:** Understand the data flow and underlying logic before depending on high-level abstractions.

### 12 — Fine-Tuning Basics

**Objective:** Understand when model fine-tuning may be useful and how it differs from retrieval and prompting.

Topics:
- Prompting versus RAG versus fine-tuning.
- Pretraining and supervised fine-tuning.
- Training data preparation.
- Instruction examples.
- Training and validation splits.
- Overfitting and evaluation.
- Parameter-efficient fine-tuning.
- LoRA fundamentals.
- Quantized fine-tuning concepts.
- Compute and memory requirements.
- Model versioning.
- Dataset licensing and privacy.

Practice:
- Identify whether a task needs prompting, retrieval, or fine-tuning.
- Prepare a small, documented training dataset.
- Inspect a fine-tuning example.
- Compare a baseline model with a fine-tuned model when resources permit.

Fine-tuning should not be treated as a substitute for current facts or access to private documents; retrieval may be more suitable for those needs.

### 13 — Tool Calling

**Objective:** Connect LLMs to controlled functions and external systems.

Topics:
- Function and tool schemas.
- Tool descriptions and parameters.
- Structured arguments.
- Input validation.
- Tool selection.
- Tool results and follow-up messages.
- Error handling.
- Timeouts and retries.
- Permission checks.
- Tool execution logging.
- Read-only versus state-changing tools.
- Human approval for consequential actions.

Practice:
- Create a calculator tool.
- Build a date or unit-conversion tool.
- Connect an LLM to a controlled search function.
- Validate tool arguments before execution.
- Test invalid inputs and failed tool calls.

**Security principle:** An LLM requesting an action does not make that action trustworthy. Validate inputs and enforce permissions in application code.

### 14 — AI Agents

**Objective:** Understand how LLM-driven systems choose tools and perform multi-step tasks.

Topics:
- Agents versus fixed workflows.
- Planning and task decomposition.
- Tool selection and execution.
- Observe–act loops.
- Stopping conditions.
- Iteration limits.
- Error recovery.
- Memory and state.
- Agent orchestration.
- Human-in-the-loop approval.
- Agent tracing and observability.
- Common failure modes.

Practice:
- Build a small agent with one or two safe tools.
- Limit the number of execution steps.
- Record tool calls and results.
- Test ambiguous tasks and tool failures.
- Compare an agent with a deterministic workflow.

### 15 — Workflows, Memory, and State

**Objective:** Build multi-step applications with explicit state and predictable execution.

Topics:
- Sequential workflows.
- Conditional branching.
- State representation.
- Workflow checkpoints.
- Short-term conversation history.
- Long-term memory concepts.
- Session management.
- State persistence.
- Retry and recovery strategies.
- Parallel tasks.
- Human approval steps.
- Workflow observability.

Practice:
- Create a multi-step document analysis workflow.
- Store conversation state for a session.
- Add conditional routing.
- Implement checkpoints and error handling.
- Compare explicit workflow logic with agent-driven control.

### 16 — Agent Evaluation and Safety

**Objective:** Test AI applications and agents for correctness, reliability, security, and responsible behavior.

Topics:
- Task success rate.
- Tool selection accuracy.
- Tool argument validation.
- Evaluation datasets.
- Regression testing.
- Prompt injection.
- Untrusted document content.
- Excessive permissions.
- Data leakage.
- Hallucination and unsupported claims.
- Human approval for high-impact actions.
- Rate and iteration limits.
- Observability and audit logs.
- Latency and cost monitoring.
- Failure recovery.
- Safe handling of secrets.

Practice:
- Create test cases for an agent.
- Simulate tool errors and malformed outputs.
- Test prompt injection using harmless examples.
- Verify that retrieved content cannot override application permissions.
- Add a human approval step before consequential actions.
- Track failures, cost, and execution time.

### 17 — Generative AI Exercises

**Objective:** Strengthen GenAI skills through focused implementation tasks.

**Beginner**
- Build a basic LLM application.
- Compare prompt variations.
- Count tokens.
- Generate embeddings.
- Calculate semantic similarity.
- Load and chunk a PDF.
- Retrieve relevant text from a small collection.

**Intermediate**
- Build a document question-answering application.
- Compare vector retrieval strategies.
- Add citations and source references.
- Evaluate RAG responses.
- Validate structured LLM outputs.
- Implement a tool-calling workflow.
- Add retries and error handling.

**Advanced**
- Compare retrieval and reranking configurations.
- Build a multi-document knowledge assistant.
- Evaluate an agent across a task dataset.
- Add human approval and permission controls.
- Implement regression tests.
- Benchmark latency, cost, and response quality.

For each exercise, document the problem, implementation, test cases, results, limitations, and lessons learned.

---

## 🧪 Portfolio Projects

All projects below are **Planned** until implementation and evaluation are complete.

| # | Project | Main Skills | Status |
|---|---|---|---|
| 1 | PDF Research Assistant | PDF extraction, RAG, source references | Planned |
| 2 | Document QA with RAG | Chunking, embeddings, retrieval, generation | Planned |
| 3 | Multi-Document Knowledge Assistant | Multi-document indexing, retrieval, citations | Planned |
| 4 | AI Research Agent | Tool calling, research workflow, verification | Planned |
| 5 | AI Data Analyst Agent | Python tools, data analysis, validation, reporting | Planned |

### Project 1 — PDF Research Assistant

**Goal:** Build an application that helps users explore a research paper or PDF and ask questions about its contents.

Potential workflow:
1. Load a PDF and extract its text.
2. Preserve page numbers and document metadata.
3. Clean and chunk the extracted content.
4. Generate embeddings and index the chunks.
5. Retrieve relevant passages for a user question.
6. Generate an answer grounded in the retrieved text.
7. Display page references or source excerpts.
8. Handle questions that cannot be answered from the document.
9. Test extraction quality and answer reliability.

**Deliverables:**
- Document ingestion workflow.
- Retrieval and answer generation pipeline.
- Source-linked answers.
- Evaluation examples.
- Usage instructions and limitations.

### Project 2 — Document QA with RAG

**Goal:** Build a question-answering system that answers questions using a selected collection of documents.

Potential workflow:
1. Load and inspect the source documents.
2. Build a reusable chunking and indexing pipeline.
3. Generate embeddings and store them in a vector index.
4. Retrieve relevant passages for each question.
5. Generate an answer using the retrieved context.
6. Include source references.
7. Test answerable and unanswerable questions.
8. Measure retrieval quality and answer correctness.
9. Document failure cases and improvement opportunities.

**Deliverables:**
- Reusable RAG pipeline.
- Document index.
- Evaluation dataset.
- Source-grounded responses.
- Evaluation report.

### Project 3 — Multi-Document Knowledge Assistant

**Goal:** Search and answer questions across multiple documents while preserving the sources of each claim.

Potential workflow:
1. Ingest multiple supported document formats.
2. Store source metadata and document identifiers.
3. Create and update the retrieval index.
4. Retrieve evidence from relevant documents.
5. Generate answers with citations.
6. Compare information across documents.
7. Handle conflicting or incomplete evidence.
8. Evaluate retrieval, citation correctness, and answer quality.

**Deliverables:**
- Multi-document ingestion pipeline.
- Search and question-answering interface.
- Source references.
- Evaluation report.
- Documentation for adding or updating documents.

### Project 4 — AI Research Agent

**Goal:** Build a controlled research assistant that plans a research task, uses approved tools, and produces an evidence-based report.

Potential workflow:
1. Convert a research request into a clear task.
2. Define permitted tools and execution limits.
3. Gather information from approved sources.
4. Track source references and key claims.
5. Identify missing evidence or conflicting information.
6. Draft a structured report.
7. Verify claims against collected evidence.
8. Request human review where needed.
9. Record tool usage, failures, and execution time.

**Deliverables:**
- Research workflow or agent.
- Tool schemas and permission controls.
- Source-linked report.
- Evaluation test cases.
- Safety and limitations documentation.

The project should not treat generated text as verified evidence. Source collection and claim verification must be explicit parts of the workflow.

### Project 5 — AI Data Analyst Agent

**Goal:** Build an assistant that helps analyze a structured dataset using controlled Python tools.

Potential workflow:
1. Load a sample CSV or other permitted dataset.
2. Inspect columns, data types, and data quality.
3. Translate an analytical question into a plan.
4. Execute approved analysis functions.
5. Calculate summaries and generate visualizations.
6. Validate numerical results against the data.
7. Produce a report with findings and limitations.
8. Handle unsupported requests and tool failures safely.
9. Record the steps used to generate the report.

**Deliverables:**
- Data inspection and analysis tools.
- Controlled agent or workflow.
- Reproducible calculations.
- Visualizations and analytical report.
- Evaluation and safety tests.

**Safety rule:** Run generated code only in a controlled environment with limited permissions. Validate inputs and outputs, and do not give the agent unrestricted filesystem, network, or system access.

*Project results and performance claims will be added only after the implementations have been tested.*

---

## 📁 Recommended Project Structure

As projects grow, use a structure like this:

```text
document_qa_rag/
├── README.md
├── src/
│   ├── ingestion.py
│   ├── chunking.py
│   ├── retrieval.py
│   ├── generation.py
│   └── evaluation.py
├── notebooks/
├── tests/
├── data/
├── reports/
├── requirements.txt
├── .env.example
└── .gitignore
```

Adapt the structure to each project. Keep reusable logic in Python modules and use notebooks for exploration and experiments.

Do not commit private documents, API keys, passwords, personal information, or other sensitive data. Large model files and datasets may be better referenced through documented download instructions rather than stored directly in Git.

---

## 📏 GenAI Project Checklist

Use this checklist for each application.

- [ ] Define the use case and success criteria.
- [ ] Choose an appropriate model and execution method.
- [ ] Record model, API, and dependency versions where practical.
- [ ] Protect credentials and private data.
- [ ] Validate input data and document formats.
- [ ] Implement appropriate error handling.
- [ ] Establish baseline test cases.
- [ ] Evaluate output quality on representative examples.
- [ ] Check unsupported claims and hallucinations.
- [ ] Validate retrieval and citations for RAG applications.
- [ ] Test tool arguments and execution permissions.
- [ ] Add iteration limits and failure recovery for agents.
- [ ] Test prompt injection and untrusted content handling.
- [ ] Measure latency and cost where relevant.
- [ ] Document limitations and reproducibility.
- [ ] Update the project README with actual results.

---

## 📈 Progress Tracker

| Learning Area | Status |
|---|---|
| LLM Fundamentals | Planned |
| Prompt Engineering | Planned |
| LLM APIs and Local Models | Planned |
| Tokenization and Embeddings | Planned |
| Vector Databases | Planned |
| Document Loading and Chunking | Planned |
| Retrieval-Augmented Generation | Planned |
| Retrieval and Reranking | Planned |
| RAG Evaluation | Planned |
| Hugging Face | Planned |
| LangChain and LlamaIndex | Planned |
| Fine-Tuning Basics | Planned |
| Tool Calling | Planned |
| AI Agents | Planned |
| Workflows, Memory, and State | Planned |
| Agent Evaluation and Safety | Planned |
| GenAI Exercises | Planned |
| PDF Research Assistant | Planned |
| Document QA with RAG | Planned |
| Multi-Document Knowledge Assistant | Planned |
| AI Research Agent | Planned |
| AI Data Analyst Agent | Planned |

**Projects completed:** 0

I will update the tracker as I complete exercises, test applications, evaluate results, and document working projects.

---

## 🚀 Getting Started

### 1. Prepare the Python environment

Create a virtual environment for each project where practical. For a basic environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install only the packages required for the current exercise. For example:

```bash
python -m pip install numpy pandas jupyter python-dotenv pydantic
```

For model APIs, document processing, vector retrieval, or agent frameworks, install the appropriate additional dependencies according to their current official documentation.

### 2. Configure secrets safely

Use environment variables for API keys. A local `.env` file may be convenient during development, but it must be excluded from Git.

A safe `.env.example` can document required variable names without containing real secrets.

### 3. Start with a small application

Recommended sequence:

1. Make a single LLM request.
2. Improve the prompt and test several examples.
3. Inspect tokenization and embeddings.
4. Build a small document retrieval workflow.
5. Add RAG and source references.
6. Evaluate the application.
7. Introduce tool calling.
8. Build an agent only when multi-step decision-making is genuinely useful.

---

## 📚 Recommended Learning Resources

Use official documentation and small reproducible experiments as the main references.

- [Hugging Face Documentation](https://huggingface.co/docs)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [FAISS Documentation](https://faiss.ai/)
- [Chroma Documentation](https://docs.trychroma.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

API behavior, package interfaces, and installation requirements can change. Check the relevant official documentation when starting an implementation.

---

## 📌 Learning Principles

- Learn the fundamentals before relying on frameworks.
- Start with the simplest working solution.
- Evaluate responses using representative test cases.
- Treat model-generated answers as outputs to verify, not facts by default.
- Ground document-based answers in retrieved evidence.
- Keep tool permissions narrow and explicit.
- Separate planning from execution when reliability matters.
- Protect secrets and sensitive data.
- Track latency, cost, and failure modes.
- Document limitations, assumptions, and model versions.
- Prefer measurable reliability improvements over unnecessary complexity.

---

## 🎯 Final Goal

Build a strong foundation in **Generative AI Engineering** by learning how to work with LLMs, design effective prompts, implement RAG, evaluate retrieval and generation, integrate tools, and build controlled AI agents.

By completing this section, I aim to demonstrate the ability to develop practical AI applications that are not only functional, but also testable, traceable, secure, and maintainable.

This folder is part of my long-term journey toward becoming an **AI/ML Engineer**, progressing from Python and Machine Learning to Deep Learning, Generative AI, RAG systems, AI Agents, and production-ready AI applications.

**Understand the model. Ground the answers. Test the system. Build responsibly.** 🚀

---

*This repository is a work in progress. All roadmap items remain planned until the corresponding exercises or projects have been completed and documented.*
