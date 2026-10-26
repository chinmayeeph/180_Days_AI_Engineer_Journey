# 🚀 Production AI & MLOps

Welcome to my **Production AI & MLOps Learning Roadmap**!

This folder focuses on the engineering skills required to turn Machine Learning and Generative AI prototypes into reliable, testable, secure, observable, and maintainable applications.

Building a model is only one part of AI engineering. A practical AI system also needs an API, input validation, automated tests, deployment infrastructure, monitoring, evaluation, security controls, and cost management.

The goal of this section is to learn these skills progressively and apply them through hands-on exercises and an end-to-end production AI capstone.

---

## 🎯 Learning Objectives

By completing this roadmap, I aim to learn how to:

- Serve ML models and AI applications through REST APIs.
- Build APIs using FastAPI and validate requests with Pydantic.
- Handle exceptions and return consistent error responses.
- Write automated tests using pytest.
- Package applications using Docker.
- Connect applications to PostgreSQL databases.
- Understand asynchronous programming and when to use it.
- Learn cloud fundamentals and deployment workflows.
- Automate testing and delivery using GitHub Actions.
- Track experiments and models using MLflow.
- Monitor application health, model performance, and data quality.
- Evaluate LLM and RAG applications.
- Implement logging, tracing, and observability.
- Manage secrets, access controls, and operational costs.
- Design AI systems with clear reliability and scalability trade-offs.
- Build and document an end-to-end production-style AI application.

---

## 📂 Folder Structure

```text
11_Production_AI_MLOps/
│
├── README.md
│
├── 01_FastAPI_Model_Serving/
├── 02_Request_Validation_Error_Handling/
├── 03_Testing_Pytest/
├── 04_Docker_Containerization/
├── 05_Databases_PostgreSQL/
├── 06_Async_Programming/
├── 07_Cloud_Fundamentals/
├── 08_Deployment/
├── 09_CI_CD_GitHub_Actions/
├── 10_MLflow_Experiment_Tracking/
├── 11_Model_Monitoring/
├── 12_AI_Evaluation_Observability/
├── 13_Security_Secrets_Cost_Optimization/
├── 14_AI_System_Design/
├── 15_Production_Capstone/
│
└── resources/
```

**GitHub note:** Empty folders are not tracked by Git. Add a `README.md`, Python file, notebook, or another appropriate file inside each folder when you start working on it.

---

## 🗺️ Recommended Learning Order

Follow this order to build the concepts gradually.

| Stage | Topic | Main Outcome |
|---|---|---|
| 1 | FastAPI and Model Serving | Expose a model through API endpoints |
| 2 | Validation and Error Handling | Build predictable API behavior |
| 3 | Testing with pytest | Verify application correctness |
| 4 | Docker | Package an application consistently |
| 5 | PostgreSQL | Persist structured application data |
| 6 | Async Programming | Understand concurrent I/O operations |
| 7 | Cloud Fundamentals | Understand cloud infrastructure |
| 8 | Deployment | Publish an application to an appropriate environment |
| 9 | CI/CD | Automate checks and delivery |
| 10 | MLflow | Track experiments and model artifacts |
| 11 | Model Monitoring | Observe model and data behavior |
| 12 | AI Evaluation and Observability | Measure AI quality and troubleshoot failures |
| 13 | Security and Cost | Protect applications and control operational costs |
| 14 | AI System Design | Make architecture and reliability decisions |
| 15 | Production Capstone | Integrate the skills into one application |

---

# 01 — FastAPI Model Serving

**Folder:** `01_FastAPI_Model_Serving/`

### Objective

Learn how to expose Python functionality and trained ML models through HTTP APIs.

### Topics to learn

- HTTP fundamentals.
- REST API concepts.
- FastAPI application structure.
- Routes and HTTP methods.
- Path and query parameters.
- Request bodies and response models.
- Pydantic schemas.
- Interactive API documentation.
- Loading a trained model.
- Prediction endpoints.
- Health-check endpoints.
- API configuration.

### Hands-on exercises

1. Build a basic welcome API.
2. Create a calculator API.
3. Create a student marks prediction endpoint using a simple baseline.
4. Load a previously trained Scikit-learn model.
5. Create a `/predict` endpoint.
6. Add a `/health` endpoint.
7. Return structured prediction results.
8. Test endpoints through the interactive API documentation.

### Expected deliverables

- FastAPI application.
- Model loading and prediction logic.
- Example requests and responses.
- Installation and execution instructions.
- Basic endpoint tests.

### Completion criteria

- [ ] The application starts using documented instructions.
- [ ] Valid requests return the expected response.
- [ ] The model loads correctly.
- [ ] Invalid requests are handled appropriately.
- [ ] API endpoints are documented.
- [ ] The application has a working health check.

---

# 02 — Request Validation and Error Handling

**Folder:** `02_Request_Validation_Error_Handling/`

### Objective

Make APIs predictable and robust when they receive invalid input or encounter runtime failures.

### Topics to learn

- Pydantic models and field constraints.
- Required and optional fields.
- Type validation.
- Custom validation.
- HTTP status codes.
- Exception handling.
- Consistent error response structures.
- Missing resources.
- Invalid model inputs.
- Configuration errors.
- Logging exceptions without exposing sensitive information.

### Hands-on exercises

1. Validate numeric input ranges.
2. Reject malformed prediction requests.
3. Validate required fields.
4. Return appropriate responses for missing resources.
5. Handle unavailable model files.
6. Create consistent error responses.
7. Add useful diagnostic logs.
8. Test validation and failure cases.

### Completion criteria

- [ ] Request schemas are documented.
- [ ] Invalid input is rejected safely.
- [ ] Appropriate HTTP status codes are returned.
- [ ] Error responses are understandable.
- [ ] Internal stack traces and secrets are not exposed to clients.
- [ ] Failure cases have automated tests.

---

# 03 — Testing with pytest

**Folder:** `03_Testing_Pytest/`

### Objective

Build confidence in the correctness of AI applications through automated testing.

### Topics to learn

- Unit testing.
- Integration testing.
- Test discovery.
- Assertions.
- Fixtures.
- Parameterized tests.
- Mocking external services.
- FastAPI test clients.
- Testing model predictions.
- Testing error paths.
- Code coverage.
- Regression tests.

### Hands-on exercises

1. Test utility functions.
2. Test input validation.
3. Test successful API responses.
4. Test invalid requests.
5. Mock an external API.
6. Test model-loading failures.
7. Test database operations.
8. Create a regression test for a previously fixed bug.

### Completion criteria

- [ ] Tests can be run using a documented command.
- [ ] Important business logic has unit tests.
- [ ] API endpoints have integration tests.
- [ ] Error paths are covered.
- [ ] External dependencies are mocked where appropriate.
- [ ] Tests run without requiring production credentials.

---

# 04 — Docker Containerization

**Folder:** `04_Docker_Containerization/`

### Objective

Package an application and its runtime dependencies into a reproducible container.

### Topics to learn

- Containers and images.
- Dockerfiles.
- Build and run commands.
- Dependency installation.
- Environment variables.
- Port mapping.
- Container logs.
- Volumes.
- Docker Compose.
- `.dockerignore`.
- Container security basics.
- Health checks.

### Hands-on exercises

1. Containerize a small Python application.
2. Containerize a FastAPI model API.
3. Configure the application port.
4. Pass configuration through environment variables.
5. Run the application locally inside a container.
6. Use Docker Compose for an API and database.
7. Inspect container logs.
8. Reduce unnecessary files and dependencies in the image.

### Completion criteria

- [ ] The image builds successfully.
- [ ] The container starts using documented instructions.
- [ ] The API is reachable from the host.
- [ ] Configuration is not hardcoded into the image.
- [ ] Secrets are not baked into the image.
- [ ] A fresh environment can reproduce the setup.

---

# 05 — Databases and PostgreSQL

**Folder:** `05_Databases_PostgreSQL/`

### Objective

Learn to persist application data using a relational database.

### Topics to learn

- Relational database fundamentals.
- Tables, columns, and data types.
- Primary and foreign keys.
- SQL queries.
- PostgreSQL connections.
- Database drivers.
- SQLAlchemy fundamentals.
- CRUD operations.
- Transactions.
- Connection configuration.
- Database migrations.
- Indexes and query performance.
- Database credentials and access control.

### Hands-on exercises

1. Create a PostgreSQL database.
2. Design tables for an AI application.
3. Store prediction requests and results.
4. Build create, read, update, and delete operations.
5. Connect FastAPI to PostgreSQL.
6. Validate data before insertion.
7. Test database operations.
8. Explore query plans for a representative query.

### Completion criteria

- [ ] Database schema is documented.
- [ ] The application connects through configuration.
- [ ] CRUD operations work correctly.
- [ ] Transactions and errors are handled appropriately.
- [ ] Credentials are kept out of source control.
- [ ] Database setup and migrations are documented.

---

# 06 — Asynchronous Programming

**Folder:** `06_Async_Programming/`

### Objective

Understand when asynchronous programming can improve responsiveness and throughput.

### Topics to learn

- Synchronous versus asynchronous execution.
- `async` and `await`.
- Event loops.
- I/O-bound versus CPU-bound tasks.
- Concurrent API requests.
- Asynchronous HTTP clients.
- Database connection behavior.
- Timeouts and cancellation.
- Concurrency limits.
- Background tasks.
- Blocking operations inside asynchronous applications.

### Hands-on exercises

1. Write synchronous and asynchronous versions of a simple I/O task.
2. Make concurrent requests to an approved test endpoint.
3. Add timeouts and exception handling.
4. Compare sequential and concurrent I/O performance.
5. Identify blocking operations in an API.
6. Measure performance under a controlled workload.

### Completion criteria

- [ ] The difference between concurrency and parallelism is understood.
- [ ] Async functions are used where they provide a benefit.
- [ ] Blocking work is handled appropriately.
- [ ] Timeouts and failures are tested.
- [ ] Performance comparisons use reproducible conditions.

**Important:** Asynchronous code is not automatically faster. CPU-intensive model inference may need different execution strategies depending on the model, framework, hardware, and workload.

---

# 07 — Cloud Fundamentals

**Folder:** `07_Cloud_Fundamentals/`

### Objective

Understand the core concepts behind deploying and operating applications in cloud environments.

### Topics to learn

- Cloud computing fundamentals.
- Regions and availability zones.
- Virtual machines.
- Object storage.
- Managed databases.
- Networking fundamentals.
- DNS and HTTPS.
- IAM and least-privilege access.
- Environment configuration.
- Logging and monitoring.
- Resource limits.
- Billing and cost controls.
- Shared responsibility for security.

### Hands-on exercises

1. Draw a basic cloud application architecture.
2. Compare virtual machines, containers, and serverless services.
3. Store a non-sensitive sample artifact in object storage.
4. Review identity and permission concepts.
5. Estimate the cost of a small deployment.
6. Create a deployment checklist.
7. Learn how to shut down or remove unused resources.

### Completion criteria

- [ ] Core cloud services can be explained.
- [ ] Application components are mapped to suitable services.
- [ ] Permissions follow least-privilege principles.
- [ ] Costs and usage limits are considered.
- [ ] No cloud credentials are committed to GitHub.

Start with free learning materials and local tools. Before creating paid resources, review pricing, quotas, and potential charges.

---

# 08 — Deployment

**Folder:** `08_Deployment/`

### Objective

Deploy an application to a suitable environment and make it accessible through a documented interface.

### Topics to learn

- Local versus hosted environments.
- Development and production configuration.
- Application startup.
- Environment variables.
- HTTPS and domains.
- Health checks.
- Deployment secrets.
- Database connectivity.
- Logs and troubleshooting.
- Resource sizing.
- Rollback fundamentals.
- Deployment documentation.

### Hands-on exercises

1. Prepare a deployment-ready FastAPI application.
2. Create a production configuration template.
3. Build and run the Docker image.
4. Deploy to a suitable hosting environment.
5. Verify the health endpoint.
6. Test valid and invalid requests.
7. Review logs after a controlled failure.
8. Document how to update or remove the deployment.

### Completion criteria

- [ ] Deployment instructions are reproducible.
- [ ] Secrets are configured securely.
- [ ] Health checks work.
- [ ] The application handles errors safely.
- [ ] Logs provide useful diagnostic information.
- [ ] Deployment limitations and costs are documented.

---

# 09 — CI/CD with GitHub Actions

**Folder:** `09_CI_CD_GitHub_Actions/`

### Objective

Automate code quality checks and testing whenever code changes.

### Topics to learn

- Continuous Integration and Continuous Delivery.
- GitHub Actions workflows.
- Workflow triggers.
- Jobs and steps.
- Dependency installation.
- Automated tests.
- Linting and formatting.
- Environment variables and secrets.
- Build validation.
- Docker image builds.
- Artifact handling.
- Protected deployment environments.
- Failure notifications.

### Hands-on exercises

1. Create a workflow that runs on pull requests.
2. Install Python dependencies.
3. Run pytest automatically.
4. Add a linting or formatting check.
5. Validate a Docker image build.
6. Save test results as workflow artifacts.
7. Require checks to pass before merging.
8. Add deployment automation only after the checks are reliable.

### Completion criteria

- [ ] Workflow triggers are documented.
- [ ] Tests run automatically.
- [ ] Failed checks are visible.
- [ ] Secrets are not printed in logs.
- [ ] The workflow uses appropriate permissions.
- [ ] Deployment requires deliberate, controlled conditions.

---

# 10 — MLflow Experiment Tracking

**Folder:** `10_MLflow_Experiment_Tracking/`

### Objective

Track ML experiments and make model comparisons reproducible.

### Topics to learn

- Experiment and run concepts.
- Parameters and metrics.
- Model artifacts.
- Dataset and configuration tracking.
- Reproducible training.
- Model comparison.
- Artifact storage.
- Model registry concepts.
- Model versioning.
- Model promotion workflows.

### Hands-on exercises

1. Train a baseline ML model.
2. Record parameters and evaluation metrics.
3. Compare multiple model configurations.
4. Save evaluation reports and artifacts.
5. Reproduce a run from its recorded configuration.
6. Track model versions.
7. Document the criteria for selecting a model.

### Completion criteria

- [ ] Experiments have clear names and descriptions.
- [ ] Parameters and metrics are recorded.
- [ ] Model artifacts can be located.
- [ ] Comparisons use consistent evaluation data.
- [ ] The selected model has a documented rationale.
- [ ] Artifact storage and access are understood.

---

# 11 — Model Monitoring

**Folder:** `11_Model_Monitoring/`

### Objective

Understand how to monitor deployed ML models and detect changes that may affect their performance.

### Topics to learn

- Service health.
- Prediction latency.
- Error rates.
- Request volume.
- Input data quality.
- Missing and unexpected values.
- Data drift.
- Concept drift.
- Prediction distribution changes.
- Delayed ground-truth labels.
- Model performance over time.
- Alert thresholds.
- Retraining considerations.

### Hands-on exercises

1. Log model request counts and latency.
2. Monitor prediction failures.
3. Define expected input ranges.
4. Compare training and incoming feature distributions.
5. Simulate a controlled data-distribution shift.
6. Create a basic monitoring report.
7. Define alert thresholds.
8. Document when an investigation or retraining review is justified.

### Completion criteria

- [ ] Service and model metrics are distinguished.
- [ ] Monitoring metrics have clear definitions.
- [ ] Drift checks use documented methods.
- [ ] Alerts have meaningful thresholds.
- [ ] Missing labels and delayed outcomes are considered.
- [ ] Retraining is not triggered solely by an unexplained metric change.

**Important:** Data drift does not automatically prove that model accuracy has decreased. Whenever possible, assess performance against reliable outcome labels.

---

# 12 — AI Evaluation and Observability

**Folder:** `12_AI_Evaluation_Observability/`

### Objective

Measure the quality and operational behavior of ML, LLM, and RAG applications.

### Topics to learn

- Evaluation datasets.
- Baselines and acceptance criteria.
- Classification and regression metrics.
- LLM response-quality evaluation.
- RAG retrieval evaluation.
- Context relevance and evidence coverage.
- Citation correctness.
- Hallucination analysis.
- Latency and token usage.
- Cost per request.
- Structured logging.
- Metrics and traces.
- Request identifiers.
- Failure analysis.
- Regression testing.

### Hands-on exercises

1. Create a fixed evaluation dataset.
2. Define expected behavior for representative test cases.
3. Evaluate a model against a baseline.
4. Evaluate RAG retrieval using relevant documents and queries.
5. Check whether generated answers are supported by retrieved evidence.
6. Track response latency and token usage.
7. Log errors with request identifiers.
8. Compare results before and after a prompt or model change.

### Completion criteria

- [ ] Evaluation datasets and metrics are documented.
- [ ] Baseline performance is recorded.
- [ ] LLM and RAG evaluation includes representative failure cases.
- [ ] Changes are tested for regressions.
- [ ] Logs avoid unnecessary sensitive information.
- [ ] Quality, latency, and cost are considered together.

LLM evaluation may combine automated metrics, structured model-based judging, and human review. No single metric reliably captures every dimension of answer quality.

---

# 13 — Security, Secrets, and Cost Optimization

**Folder:** `13_Security_Secrets_Cost_Optimization/`

### Objective

Build AI services that protect data, control access, and operate within practical cost limits.

### Topics to learn

- API keys and environment variables.
- Secret management.
- Authentication and authorization.
- Least-privilege access.
- Input validation.
- Dependency updates.
- Secure error handling.
- Rate limiting.
- Request-size limits.
- Data privacy.
- Prompt injection risks.
- Tool permission boundaries.
- LLM token budgets.
- Model selection and cost trade-offs.
- Caching.
- Timeouts and retries.
- Resource limits.
- Audit logging.

### Hands-on exercises

1. Remove hardcoded secrets from an example application.
2. Configure secrets through environment variables.
3. Add request-size and input limits.
4. Implement a simple rate limit.
5. Restrict an agent to an explicit tool allowlist.
6. Estimate cost per request for an LLM workflow.
7. Add timeouts and bounded retries.
8. Document data handling and retention decisions.

### Completion criteria

- [ ] No live secrets are committed to source control.
- [ ] Access permissions are limited appropriately.
- [ ] Inputs are validated.
- [ ] Sensitive information is not unnecessarily logged.
- [ ] Cost and usage limits are documented.
- [ ] External tools have explicit permission boundaries.
- [ ] Security limitations are clearly recorded.

---

# 14 — AI System Design

**Folder:** `14_AI_System_Design/`

### Objective

Learn to design AI applications by evaluating architecture, data flow, reliability, scalability, security, and operational trade-offs.

### Topics to learn

- Requirements gathering.
- Functional and non-functional requirements.
- API design.
- Component boundaries.
- Data flow diagrams.
- Model serving patterns.
- Synchronous versus asynchronous inference.
- Queues and background workers.
- Caching.
- Database and object storage choices.
- Vector search and retrieval.
- Horizontal scaling.
- Latency and throughput.
- Fault tolerance.
- Observability.
- Privacy and security.
- Cost estimation.
- Architecture decision records.

### Hands-on exercises

1. Design an ML prediction API.
2. Draw a RAG application architecture.
3. Design a document ingestion pipeline.
4. Compare synchronous and queued inference.
5. Identify bottlenecks in an AI application.
6. Design a monitoring and alerting plan.
7. Estimate cost under a hypothetical workload.
8. Write an architecture decision record explaining a key design choice.

### Completion criteria

- [ ] Requirements are explicit.
- [ ] Architecture diagrams show the main components and data flow.
- [ ] Reliability and failure cases are considered.
- [ ] Security boundaries are identified.
- [ ] Performance assumptions are documented.
- [ ] Cost estimates state their assumptions.
- [ ] Trade-offs and alternatives are explained.

---

# 15 — Production AI Capstone

**Folder:** `15_Production_Capstone/`

### Objective

Build a complete, documented AI application that combines API development, testing, deployment, evaluation, monitoring, and security.

## Recommended capstone: Production-Style Document Intelligence API

Build a document-question-answering service that accepts approved documents, retrieves relevant evidence, and returns answers with source references.

### Core features

- FastAPI application.
- Validated request and response schemas.
- Document ingestion and processing.
- Retrieval and answer generation.
- Source references in responses.
- Error handling and structured logs.
- Automated tests.
- Docker containerization.
- Configuration through environment variables.
- PostgreSQL persistence where appropriate.
- Evaluation dataset and quality report.
- Latency and usage monitoring.
- Security and cost controls.
- Deployment instructions.

### Suggested architecture

```text
Client
  |
  v
FastAPI
  |
  +--> Request Validation
  |
  +--> Document / Query Processing
  |          |
  |          v
  |      Retrieval Layer
  |          |
  |          v
  |      LLM Provider
  |
  +--> Database / Metadata Storage
  |
  +--> Logging and Metrics
  |
  v
Validated Response with Sources
```

### Development milestones

**Milestone 1 — Requirements and baseline**
- Define the user problem and supported document types.
- Select an approved dataset.
- Define measurable acceptance criteria.

**Milestone 2 — Core application**
- Implement document ingestion and retrieval.
- Build a basic API.
- Return answers with source references.

**Milestone 3 — Quality and testing**
- Create an evaluation dataset.
- Test valid, invalid, and unsupported questions.
- Add regression tests.

**Milestone 4 — Packaging and persistence**
- Containerize the application.
- Add database persistence if needed.
- Document configuration.

**Milestone 5 — Observability and security**
- Record useful operational metrics.
- Track latency and usage.
- Add access controls and safe error handling.

**Milestone 6 — Deployment**
- Deploy to an appropriate environment.
- Verify health checks and endpoints.
- Document costs, limitations, and rollback steps.

### Capstone deliverables

- [ ] Architecture diagram.
- [ ] Source code.
- [ ] API documentation.
- [ ] Automated test suite.
- [ ] Docker configuration.
- [ ] Evaluation dataset and report.
- [ ] Monitoring and logging setup.
- [ ] Security and cost notes.
- [ ] Deployment guide.
- [ ] Screenshots or demo.
- [ ] Clear limitations and future improvements.

The capstone is complete only when the implemented features have been tested and documented. A design or tutorial alone does not count as a finished deployment.

---

## 📚 Resources

Use official documentation as the primary reference. Follow the fundamentals before adding complex infrastructure.

### Python APIs and testing
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [pytest Documentation](https://docs.pytest.org/)
- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

### Containers and databases
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

### Automation, tracking, and deployment
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [Google Cloud Documentation](https://cloud.google.com/docs)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Microsoft Azure Documentation](https://learn.microsoft.com/en-us/azure/)

Choose one cloud platform when you are ready to deploy. You do not need to learn all cloud providers simultaneously.

### AI evaluation and observability
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Hugging Face Documentation](https://huggingface.co/docs)
- [OWASP GenAI Security Project](https://genai.owasp.org/)

---

## 📈 Progress Tracker

All topics begin as **Planned**.

| Topic | Status |
|---|---|
| FastAPI Model Serving | Planned |
| Request Validation and Error Handling | Planned |
| Testing with pytest | Planned |
| Docker Containerization | Planned |
| PostgreSQL | Planned |
| Async Programming | Planned |
| Cloud Fundamentals | Planned |
| Deployment | Planned |
| CI/CD with GitHub Actions | Planned |
| MLflow Experiment Tracking | Planned |
| Model Monitoring | Planned |
| AI Evaluation and Observability | Planned |
| Security, Secrets, and Cost Optimization | Planned |
| AI System Design | Planned |
| Production AI Capstone | Planned |

**Completed topics:** 0

Update the status only after completing the corresponding exercises and meeting the completion criteria.

---

## 🧭 How I Will Study This Section

1. Learn one concept at a time.
2. Create small examples before building a full application.
3. Save code, exercises, notes, and tests in the relevant folder.
4. Run the code locally before attempting deployment.
5. Use Git and GitHub to track changes.
6. Document errors and the solutions that worked.
7. Build the capstone incrementally rather than all at once.
8. Avoid unnecessary cloud spending and complex tools before they are needed.

---

## 🏁 Final Goal

Develop the engineering skills needed to move beyond notebooks and prototypes toward **reliable, evaluated, secure, observable, and maintainable AI applications**.

The focus is not on using the greatest number of tools. It is on understanding why each tool is needed, applying it correctly, testing the result, and documenting the trade-offs.

**Build it. Test it. Deploy it. Monitor it. Improve it.** 🚀

*This roadmap is a learning plan. It does not claim that the listed systems have been implemented, deployed, or evaluated yet.*
