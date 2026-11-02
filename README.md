# RAG-Based AI Teaching System

## About the Project

The RAG-Based AI Teaching System is an AI-powered educational assistant that allows students to ask questions and receive context-aware answers based on educational video content.

It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from video transcripts and generate answers using a locally running Large Language Model (LLM).

## Features

* Converts educational videos into audio.
* Extracts and processes video transcripts using OpenAI Whisper.
* Generates text embeddings using the BGE-M3 embedding model.
* Retrieves relevant information using Cosine Similarity.
* Generates answers using a locally running LLM through Ollama.
* Provides context-based answers to student queries.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* OpenAI Whisper
* BGE-M3
* Ollama
* Llama 3
* FFmpeg

## How It Works

1. Educational videos are converted into audio using FFmpeg.
2. OpenAI Whisper transcribes the audio.
3. Transcripts are divided into smaller chunks.
4. BGE-M3 generates embeddings for the text chunks.
5. Embeddings are stored locally using Joblib.
6. When a student asks a question, the system generates its embedding.
7. Cosine Similarity identifies the most relevant text chunks.
8. Ollama's Llama 3 model generates an answer using the retrieved context.

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd RAG-AI-Teaching-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

Install FFmpeg and configure it in your system PATH.

### 4. Install Ollama

Download and install Ollama.

### 5. Download Required Models

```bash
ollama pull llama3
ollama pull bge-m3
```

### 6. Run the Project

Start Ollama and execute the Python application.

```bash
python main.py
```

## Future Improvements

* Develop an interactive interface using Streamlit.
* Integrate a vector database such as FAISS or ChromaDB.
* Improve retrieval accuracy.
* Add support for multiple educational subjects.
* Implement hallucination reduction techniques.

## Author

Gyandeep Kumar
