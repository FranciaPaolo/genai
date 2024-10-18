import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# To run the app run in the terminal
# streamlit run 3.2-simpleapp_ollama.py

load_dotenv()

## Langsmith Tracking
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
#os.environ["LANGCHAIN_TRACING_V2"]="true"
#os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question: {question}"),
    ]
)

## Streamlit framework
st.title("Langchain Demo with LLAMA2 and Ollama")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama mode
llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

# when press enter on the input_text
if input_text:
    st.write(chain.invoke({"question":input_text}))
