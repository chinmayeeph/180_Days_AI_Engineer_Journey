# 🧠 Deep Learning — Neural Networks, PyTorch & Projects

Welcome to my **Deep Learning Learning and Projects** repository!

This folder documents my journey of learning Deep Learning using Python, mathematical foundations, neural networks, PyTorch, computer vision, Natural Language Processing (NLP), and Transformer architectures.

Deep Learning is a branch of Machine Learning that uses neural networks with multiple layers to learn complex patterns from data. It powers applications such as image recognition, language understanding, text generation, speech processing, and modern Generative AI systems.

My goal is to understand the fundamentals, implement and train neural networks, evaluate model performance, and build reproducible projects that demonstrate practical skills.

---

## 🎯 Learning Objectives

By completing this section, I aim to learn how to:

- Understand the fundamentals of Deep Learning and neural networks.
- Work with tensors and essential linear algebra operations.
- Understand neurons, layers, activation functions, and network architectures.
- Explain forward propagation and backpropagation.
- Understand loss functions, optimizers, and gradient-based learning.
- Apply regularization techniques to improve generalization.
- Build neural networks using PyTorch.
- Load, transform, and batch datasets.
- Train, validate, and evaluate deep learning models.
- Build Convolutional Neural Networks (CNNs) for image classification.
- Understand sequence models such as RNNs and LSTMs.
- Learn NLP fundamentals, tokenization, and embeddings.
- Understand attention mechanisms and Transformer architectures.
- Use Hugging Face tools and pretrained models.
- Apply transfer learning to practical problems.
- Save trained models and reproduce experiments.
- Build and document end-to-end deep learning projects.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical operations |
| Matplotlib | Visualizing data and training results |
| Pandas | Dataset inspection and analysis |
| PyTorch | Building and training neural networks |
| Torchvision | Computer vision datasets, transforms, and models |
| Torchtext / Hugging Face Tokenizers | Text-processing concepts and tokenization tools |
| Hugging Face Transformers | Using pretrained Transformer models |
| Hugging Face Datasets | Loading and processing datasets |
| Jupyter Notebook | Interactive experimentation |
| Google Colab | Cloud-based experimentation with optional GPU access |
| Git and GitHub | Version control and portfolio development |

**Recommended starting point:** Begin with tensors, basic neural networks, and PyTorch on small datasets. Use Google Colab if your computer does not have a suitable GPU. A GPU is helpful for larger experiments but is not required for the introductory exercises.

---

## 📂 Repository Structure

```text
08_Deep_Learning/
│
├── README.md
│
├── 01_Deep_Learning_Fundamentals/
│   ├── README.md
│   └── notebooks/
│
├── 02_Tensors_Linear_Algebra/
│   ├── README.md
│   └── notebooks/
│
├── 03_Neural_Networks/
│   ├── README.md
│   └── notebooks/
│
├── 04_Forward_Propagation_Backpropagation/
│   ├── README.md
│   └── notebooks/
│
├── 05_Loss_Optimization_Regularization/
│   ├── README.md
│   └── notebooks/
│
├── 06_PyTorch_Fundamentals/
│   ├── README.md
│   └── notebooks/
│
├── 07_Datasets_DataLoaders/
│   ├── README.md
│   └── notebooks/
│
├── 08_Model_Training_Validation/
│   ├── README.md
│   └── notebooks/
│
├── 09_CNNs_Computer_Vision/
│   ├── README.md
│   └── notebooks/
│
├── 10_RNN_LSTM_Sequence_Models/
│   ├── README.md
│   └── notebooks/
│
├── 11_NLP_Fundamentals/
│   ├── README.md
│   └── notebooks/
│
├── 12_Tokenization_Embeddings/
│   ├── README.md
│   └── notebooks/
│
├── 13_Attention_Transformers/
│   ├── README.md
│   └── notebooks/
│
├── 14_Hugging_Face/
│   ├── README.md
│   └── notebooks/
│
├── 15_Transfer_Learning/
│   ├── README.md
│   └── notebooks/
│
├── 16_Exercises/
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
    ├── image_classification/
    │   └── README.md
    │
    ├── sentiment_analysis/
    │   └── README.md
    │
    └── transformer_text_classifier/
        └── README.md
```

*Note: Nested README files and notebook folders are suggested organizational conventions. Create them as needed. Git does not track empty directories, so add files to folders you want GitHub to display.*

---

## 📚 Learning Roadmap

### 01 — Deep Learning Fundamentals

**Objective:** Understand what deep learning is and how neural networks learn.

Topics:
- Machine Learning versus Deep Learning.
- Biological inspiration and artificial neurons.
- Neural network layers.
- Input, hidden, and output layers.
- Weights and biases.
- Activation functions.
- Parameters and hyperparameters.
- Training, validation, and inference.
- Overfitting and underfitting.
- Applications and limitations of deep learning.

Practice:
- Draw a simple neural network and identify its layers.
- Explain the role of weights, biases, and activation functions.
- Compare a simple ML model with a neural network.

### 02 — Tensors and Linear Algebra

**Objective:** Build the mathematical and computational foundations needed to work with neural networks.

Topics:
- Scalars, vectors, matrices, and higher-dimensional tensors.
- Tensor shapes, dimensions, and data types.
- Indexing, slicing, and reshaping.
- Element-wise operations.
- Matrix multiplication.
- Dot products.
- Transpose and broadcasting.
- Vector norms and distances.
- Basic matrix and vector operations.
- Gradients and partial derivatives.
- Why tensor shapes matter in neural network layers.

Practice:
- Create tensors of different shapes.
- Perform arithmetic and matrix multiplication.
- Reshape and combine tensors.
- Trace the shapes of inputs and outputs through a simple network.

### 03 — Neural Networks

**Objective:** Understand how neural networks represent and learn patterns.

Topics:
- The artificial neuron.
- Perceptrons.
- Fully connected layers.
- Weights and biases.
- Linear transformations.
- Activation functions: ReLU, sigmoid, and tanh.
- Softmax for multiclass outputs.
- Hidden layer size and network depth.
- Binary and multiclass prediction.
- Neural network parameter counts.

Practice:
- Implement a simple perceptron.
- Build a small feedforward network.
- Compare activation functions.
- Investigate how changing layer sizes affects model capacity.

### 04 — Forward Propagation and Backpropagation

**Objective:** Understand how neural networks produce predictions and calculate gradients for learning.

Topics:
- Forward propagation.
- Layer-by-layer computation.
- Prediction and target values.
- Loss calculation.
- Computational graphs.
- Derivatives and the chain rule.
- Gradient calculation.
- Backpropagation.
- Gradient descent.
- Parameter updates.
- PyTorch automatic differentiation using `autograd`.

Practice:
- Calculate a small forward pass manually.
- Work through a simple derivative.
- Use PyTorch tensors with gradient tracking.
- Compare manual calculations with automatic gradients.

### 05 — Loss, Optimization, and Regularization

**Objective:** Understand how a neural network improves its predictions and controls overfitting.

Topics:
- Mean Squared Error (MSE).
- Cross-entropy loss.
- Binary cross-entropy.
- Gradient descent.
- Stochastic Gradient Descent (SGD).
- Mini-batch gradient descent.
- Adam optimizer.
- Learning rates.
- Batch size and number of epochs.
- Learning-rate scheduling.
- Weight decay.
- Dropout.
- Early stopping.
- Vanishing and exploding gradients.
- Training and validation loss curves.

Practice:
- Compare loss functions for different tasks.
- Investigate the effect of learning rates.
- Plot training and validation loss.
- Compare a model with and without regularization.

### 06 — PyTorch Fundamentals

**Objective:** Learn the core PyTorch tools used to build neural networks.

Topics:
- Creating and manipulating tensors.
- Tensor operations and devices.
- CPU and GPU execution.
- Automatic differentiation.
- The `torch.nn` module.
- The `nn.Module` class.
- Defining layers and `forward()`.
- Loss functions and optimizers.
- `model.train()` and `model.eval()`.
- `torch.no_grad()`.
- Resetting gradients with `optimizer.zero_grad()`.
- Saving and loading model state dictionaries.
- Reproducible experiments.

Practice:
- Build a neural network using `nn.Module`.
- Train a model with a manual training loop.
- Move tensors and models between CPU and GPU when available.
- Save and reload a trained model.

### 07 — Datasets and DataLoaders

**Objective:** Prepare data for efficient and repeatable model training.

Topics:
- PyTorch `Dataset`.
- PyTorch `DataLoader`.
- Loading tabular and image data.
- Batch size and shuffling.
- Dataset transformations.
- Training and validation datasets.
- Custom datasets.
- Labels and feature-target relationships.
- Data augmentation fundamentals.
- Reproducible data preparation.

Practice:
- Create a custom dataset.
- Load and batch sample data.
- Visualize image batches.
- Compare training data with validation data.

### 08 — Model Training and Validation

**Objective:** Develop a reliable training and evaluation workflow.

Topics:
- Training loops.
- Forward pass and loss calculation.
- Backpropagation and optimizer updates.
- Validation loops.
- Training versus evaluation mode.
- Monitoring training and validation metrics.
- Overfitting detection.
- Checkpointing.
- Early stopping.
- Reproducibility and random seeds.
- Experiment tracking fundamentals.
- Error analysis.

Practice:
- Train a model across multiple epochs.
- Plot loss and evaluation metrics.
- Compare training and validation performance.
- Save the best checkpoint based on validation results.

### 09 — CNNs and Computer Vision

**Objective:** Learn how neural networks process images and recognize visual patterns.

Topics:
- Image tensors and channels.
- Convolution operations.
- Filters and feature maps.
- Stride and padding.
- Pooling.
- CNN architecture.
- Fully connected classification layers.
- Image normalization.
- Data augmentation.
- Image classification metrics.
- Transfer learning for vision.
- Introduction to image segmentation and object detection.

Practice:
- Visualize image tensors and feature maps.
- Build a basic CNN.
- Train an image classifier.
- Compare a small CNN with a pretrained model.

### 10 — RNNs, LSTMs, and Sequence Models

**Objective:** Understand neural network approaches for sequential data.

Topics:
- Sequential data and time steps.
- Sequence inputs and outputs.
- Recurrent Neural Networks (RNNs).
- Hidden states.
- Vanishing and exploding gradients.
- Long Short-Term Memory (LSTM).
- Gated Recurrent Units (GRUs).
- Sequence classification.
- Padding and variable-length sequences.
- Limitations of recurrent architectures.
- Comparison with Transformer models.

Practice:
- Build a simple sequence classifier.
- Explore how input sequence length affects processing.
- Compare an RNN or LSTM with a simpler baseline.

### 11 — NLP Fundamentals

**Objective:** Understand how text is prepared for machine learning.

Topics:
- Text classification and other NLP tasks.
- Text normalization.
- Tokenization concepts.
- Vocabulary construction.
- Word and character representations.
- Stopwords and stemming or lemmatization.
- Bag-of-Words.
- TF-IDF.
- Sparse versus dense representations.
- Text classification baselines.
- NLP evaluation metrics.

Practice:
- Clean and inspect a text dataset.
- Build a basic text classifier.
- Compare a TF-IDF baseline with a neural model.

### 12 — Tokenization and Embeddings

**Objective:** Learn how text is converted into numerical representations.

Topics:
- Token IDs and vocabularies.
- Word-level and subword tokenization.
- Special tokens.
- Padding and truncation.
- Attention masks.
- Word embeddings.
- Embedding layers.
- Contextual embeddings.
- Sequence length and memory use.
- Tokenization for pretrained models.

Practice:
- Tokenize example sentences.
- Inspect token IDs and attention masks.
- Compare tokenization approaches.
- Explore how embeddings represent text numerically.

### 13 — Attention and Transformers

**Objective:** Understand the foundations of modern language models.

Topics:
- Why attention is useful.
- Query, Key, and Value concepts.
- Scaled dot-product attention.
- Self-attention.
- Multi-head attention.
- Positional information.
- Transformer encoder and decoder concepts.
- Feedforward sublayers.
- Residual connections.
- Layer normalization.
- Encoder-only, decoder-only, and encoder-decoder architectures.
- Computational and memory considerations.

Practice:
- Trace the steps in self-attention.
- Calculate attention weights for a small example.
- Inspect a Transformer model's inputs and outputs.
- Explain the high-level differences between common Transformer architectures.

### 14 — Hugging Face

**Objective:** Learn to use pretrained models and datasets through the Hugging Face ecosystem.

Topics:
- The Hugging Face Hub.
- `transformers` pipelines.
- Tokenizers.
- Model loading.
- Pretrained model inference.
- Dataset loading and processing.
- Fine-tuning fundamentals.
- Training arguments.
- Evaluation.
- Saving and sharing model artifacts.
- Model cards and dataset documentation.
- Resource requirements and model licensing.

Practice:
- Run a pretrained sentiment classifier.
- Inspect a tokenizer and its output.
- Load a public dataset.
- Fine-tune a small suitable model when compute resources permit.

### 15 — Transfer Learning

**Objective:** Reuse pretrained models to solve new tasks efficiently.

Topics:
- Pretraining and fine-tuning.
- Frozen and trainable layers.
- Feature extraction.
- Replacing classification heads.
- Fine-tuning image models.
- Fine-tuning text models.
- Learning-rate selection.
- Dataset size and model capacity.
- Overfitting during fine-tuning.
- Compute and memory constraints.
- Comparing pretrained and training-from-scratch approaches.

Practice:
- Replace the final layer of a pretrained image model.
- Freeze and unfreeze model layers.
- Compare transfer learning with a small model trained from scratch.
- Document resource requirements and results.

### 16 — Deep Learning Exercises

**Objective:** Strengthen understanding by implementing concepts independently.

**Beginner**
- Tensor creation and manipulation.
- Matrix operations.
- Activation function exploration.
- Simple perceptron.
- Forward propagation.
- Basic PyTorch model.
- Loss calculation.

**Intermediate**
- Backpropagation and automatic differentiation.
- Custom training loops.
- Dataset and DataLoader implementation.
- Model regularization.
- CNN image classification.
- RNN or LSTM sequence classification.
- Training and validation curves.

**Advanced**
- Attention mechanism exploration.
- Transformer text classification.
- Transfer learning.
- Fine-tuning a pretrained model.
- Error analysis.
- Reproducible training and inference.

For every exercise, record the problem, implementation, expected behavior, actual results, and lessons learned.

---

## 🧪 Portfolio Projects

All projects below are **Planned** until the actual implementation and results are completed and documented.

| # | Project | Main Skills | Status |
|---|---|---|---|
| 1 | Image Classification | PyTorch, CNNs, data augmentation, evaluation | Planned |
| 2 | Sentiment Analysis | NLP, tokenization, embeddings, classification | Planned |
| 3 | Transformer Text Classifier | Attention, pretrained models, fine-tuning | Planned |

### Project 1 — Image Classification

**Goal:** Build a model that classifies images into predefined categories.

Potential workflow:
1. Choose a suitable, documented image dataset.
2. Inspect the classes and class distribution.
3. Create appropriate training, validation, and test splits.
4. Apply image transformations and normalization.
5. Build a baseline model.
6. Train a CNN using PyTorch.
7. Monitor training and validation performance.
8. Evaluate using appropriate metrics and a confusion matrix.
9. Investigate incorrectly classified images.
10. Compare a CNN with a pretrained model if resources allow.
11. Save the model and document inference.

**Deliverables:**
- Training notebook or scripts.
- Model evaluation report.
- Example predictions.
- Training curves.
- Instructions for reproducing the experiment.

### Project 2 — Sentiment Analysis

**Goal:** Predict whether a text sample expresses positive or negative sentiment, using a suitable labelled dataset.

Potential workflow:
1. Inspect the dataset, labels, and class distribution.
2. Split data before fitting any learned preprocessing.
3. Build a simple text classification baseline.
4. Prepare text using an appropriate tokenization strategy.
5. Train a neural classifier using embeddings or a suitable pretrained model.
6. Evaluate using precision, recall, F1-score, and a confusion matrix.
7. Investigate misclassifications and ambiguous text.
8. Document limitations such as sarcasm, domain differences, and label quality.

**Deliverables:**
- Text preprocessing workflow.
- Training notebook.
- Model comparison.
- Evaluation report.
- Example predictions and limitations.

### Project 3 — Transformer Text Classifier

**Goal:** Fine-tune a suitable pretrained Transformer to classify text into predefined categories.

Potential workflow:
1. Choose a task and dataset with clear labels.
2. Select an appropriately licensed pretrained model.
3. Inspect the tokenizer and model requirements.
4. Prepare training, validation, and test splits.
5. Tokenize and batch the dataset.
6. Establish a baseline.
7. Fine-tune the model with appropriate evaluation.
8. Monitor overfitting and computational requirements.
9. Evaluate on held-out data.
10. Inspect misclassifications and model limitations.
11. Save the model and tokenizer.
12. Document how to reproduce inference.

**Deliverables:**
- Fine-tuning notebook or script.
- Evaluation report.
- Saved model artifacts where practical.
- Example inference script.
- Model and dataset documentation.

*Project results, performance scores, and conclusions will be added only after experiments have actually been run.*

---

## 📁 Recommended Project Structure

As projects grow, use a structure like this:

```text
image_classification/
├── README.md
├── notebooks/
├── src/
│   ├── dataset.py
│   ├── model.py
│   ├── train.py
│   └── predict.py
├── tests/
├── reports/
├── requirements.txt
└── .gitignore
```

Adapt the structure to each project. Keep exploratory notebooks separate from reusable Python code as the implementation matures.

Avoid committing large datasets, private information, credentials, or model checkpoints that exceed repository limits. Document how to obtain external datasets and model artifacts instead.

---

## 📏 Deep Learning Project Checklist

Use this checklist for each project.

- [ ] Define the task and expected outputs.
- [ ] Understand the dataset and labels.
- [ ] Check data quality and class balance.
- [ ] Create appropriate data splits.
- [ ] Establish a baseline.
- [ ] Select a suitable architecture and loss function.
- [ ] Prepare datasets and DataLoaders.
- [ ] Implement a reproducible training loop.
- [ ] Monitor training and validation metrics.
- [ ] Check for overfitting and data leakage.
- [ ] Evaluate on held-out data.
- [ ] Inspect errors and limitations.
- [ ] Save the model and required preprocessing components.
- [ ] Test inference on new examples.
- [ ] Document dependencies and reproduction steps.
- [ ] Update the project README with actual results.

---

## 📈 Progress Tracker

| Learning Area | Status |
|---|---|
| Deep Learning Fundamentals | Planned |
| Tensors and Linear Algebra | Planned |
| Neural Networks | Planned |
| Forward Propagation and Backpropagation | Planned |
| Loss, Optimization, and Regularization | Planned |
| PyTorch Fundamentals | Planned |
| Datasets and DataLoaders | Planned |
| Model Training and Validation | Planned |
| CNNs and Computer Vision | Planned |
| RNNs, LSTMs, and Sequence Models | Planned |
| NLP Fundamentals | Planned |
| Tokenization and Embeddings | Planned |
| Attention and Transformers | Planned |
| Hugging Face | Planned |
| Transfer Learning | Planned |
| Deep Learning Exercises | Planned |
| Image Classification | Planned |
| Sentiment Analysis | Planned |
| Transformer Text Classifier | Planned |

**Projects completed:** 0

I will update the tracker after completing exercises, validating experiments, and documenting working projects.

---

## 🚀 Getting Started

Create and activate a Python virtual environment before installing project dependencies.

For a basic learning environment, install:

```bash
python -m pip install numpy pandas matplotlib scikit-learn jupyter
```

Install PyTorch using the current instructions on the official [PyTorch website](https://pytorch.org/get-started/locally/), selecting the configuration appropriate for your operating system and compute hardware.

For NLP and pretrained models, install these packages when needed:

```bash
python -m pip install transformers datasets
```

Recommended workflow:

1. Start with small tensor exercises.
2. Build a simple neural network.
3. Understand the training loop before using high-level training abstractions.
4. Train a small model and plot the learning curves.
5. Move to CNNs and sequence models.
6. Explore attention and Transformers after learning the foundations.
7. Save experiments, record results, and commit meaningful progress to GitHub.

---

## 📌 Learning Principles

- Understand tensors and shapes before building complex architectures.
- Learn the training loop instead of treating it as a black box.
- Start with simple models and baselines.
- Monitor both training and validation performance.
- Avoid data leakage and evaluate on held-out data.
- Use pretrained models thoughtfully rather than fine-tuning blindly.
- Record random seeds, configurations, and dependency versions when practical.
- Consider compute, memory, licensing, and reproducibility.
- Investigate errors instead of reporting only one performance score.
- Document limitations and avoid making unsupported claims.

---

## 🎯 Final Goal

Build a strong foundation in **Deep Learning engineering** by progressing from neural network fundamentals to PyTorch, computer vision, NLP, attention, Transformers, and transfer learning.

By completing this section, I aim to understand how neural networks learn, train and evaluate models systematically, work with pretrained architectures, and develop reproducible deep learning projects.

This folder is part of my long-term journey toward becoming an **AI/ML Engineer**, progressing toward Generative AI, Large Language Models, RAG systems, AI Agents, and production AI applications.

**Understand the foundations. Train with discipline. Evaluate carefully. Build reproducible AI systems.** 🚀

---

*This repository is a work in progress. All roadmap items remain planned until the corresponding exercises or projects have been completed and documented.*
