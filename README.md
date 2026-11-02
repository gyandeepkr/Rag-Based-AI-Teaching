# RAG-Based AI Teaching System

## Overview

A Retrieval-Augmented Generation (RAG) based AI teaching assistant that enables users to ask questions and receive contextually relevant answers from educational video content.

The system processes educational videos, converts speech into text using Whisper, generates semantic embeddings using BGE-M3, and retrieves relevant information using cosine similarity. Ollama with Llama 3 is used to generate context-aware answers based on the retrieved content.

## Features

* Educational video-to-audio conversion
* Speech-to-text transcription using Whisper
* Text chunking and embedding generation
* Semantic retrieval using cosine similarity
* Local LLM integration using Ollama
* Context-aware question answering

## Tech Stack

* Python
* OpenAI Whisper
* BGE-M3
* Ollama
* Llama 3
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Project Workflow

Educational Videos
↓
Audio Extraction
↓
Whisper Transcription
↓
Text Chunking
↓
BGE-M3 Embeddings
↓
Cosine Similarity Retrieval
↓
Relevant Context
↓
Llama 3 via Ollama
↓
AI-Generated Answer

## Project Structure

```text
RAG-Based-AI-Teaching-System/
├── videos_to_mp3.py
├── mp3_to_jsons.py
├── saving_chunks_into_joblib.py
├── process_embedding.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

* Develop an interactive Streamlit interface
* Improve retrieval accuracy
* Add support for multiple educational subjects
* Integrate a vector database
