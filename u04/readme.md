# Langchain and OpenAI

## 1-Langchain
* introduction of Langchain with OpenAI models
* data ingestion
* split pdf
* embedding with OpenAI and Ollama
* Vector store with Chromadb and Faiss

## 2-Langchain smith
* Track and monitor the Langchain calls

## 3-Langchain prompt
* OpenAI prompt in the jupyter notebook
* Streamlit prompt using [Ollama](https://ollama.com/) "gemma2:2b" model

## 4-Langchain translate
* Language translation using [Groq](https://groq.com/)
* Language translation using Groq and [FastAPI](https://fastapi.tiangolo.com/)

## 5-Langchain chatbot
* Groq chatbot including message history
* Retrievers from vector store

## 6-Q&A OpenAI
* Q&A OpenAI model chatbot in Streamlit

## 7-Q&A Ollama
* Q&A Ollama model chatbot in Streamlit

## 8-Q&A RAG Grow
* RAG document Q&A With Groq And Lama3

## 9-Q&A RAG Grow from Pdf
* RAG document Q&A With Groq And Lama3


## Setup

```
conda create -p venv python==3.10 -y
```

-y is to set it has default

```
pip install -r requirements.txt
```

Setup in the .env file the keys
```
OPENAI_API_KEY=""
LANGCHAIN_API_KEY=""
LANGCHAIN_PROJECT="GenAIAPPWithOPENAI"
OPENWEATHERMAP_API_KEY=""
HF_TOKEN=""
GROQ_API_KEY=""
```

Install Ollama on your machine
