# Simple Question Answering with RAG
Welcome to the Simple Question Answering RAG (Retrieval-Augmented Generation) application! This project demonstrates how to build a simple QA system using RAG, a method that combines retrieval-based and generation-based techniques to provide accurate and informative answers.

Table of Contents
* Introduction
* Features
* Architecture
* Setup
* Usage
* Contributing
* License

### Introduction
RAG leverages the power of both retrieval-based and generation-based models. It first retrieves relevant documents from a knowledge base and then generates an answer using those documents. This approach ensures that the answers are not only relevant but also coherent and contextually accurate.

### Features
* Hybrid Model: Combines retrieval-based and generation-based approaches for answering questions.
* Extensible: Easily extendable to use different retrieval models or generators.
* Configurable: Highly configurable to adjust retrieval parameters, model specifics, and more.

### Architecture
1. Query Processing: The user inputs a question.
2. Document Retrieval: Relevant documents are retrieved from the knowledge base using a retrieval model.
3. Answer Generation: An answer is generated based on the retrieved documents using a generative model.

### Setup
To set up the project locally, follow these steps:
1. Clone the repository:

```
https://github.com/nishan129/Q-A-llm.git
```

```
cd Q-A-llm
```

2. Create and activate a virtual environment:

```
conda create -p llmapp python==3.10 -y
```

```
conda activate llmapp
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Download and set up the necessary models:
 * Ensure you have the necessary models for retrieval and generation. You can specify the models in a configuration file or directly within the code and save model in model folder.

### Usage
1. Run the application:
```
python app.py
```
2. Interact with the application:
 * Open your web browser and navigate to http://localhost:8080
 * Input a question and receive an answer generated by the RAG model.

We hope this project helps you understand and implement retrieval-augmented generation for question answering. If you have any questions or feedback, feel free to open an issue or contact us directly.

Happy coding!
