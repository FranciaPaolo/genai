from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

## **************************************************
# to run it from terminal:
# python 4.1-langserve.py
#
# then open the url: http://localhost:8000/docs
# from there try the /chain/invoke method, put in 
# "language": "French" 
# and in the "text": "hello"

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# 1. Create prompt template
system_template= "Translate the following into {language}, giving only one output in an informa way:"
prompt_template= ChatPromptTemplate.from_messages([
    ('system',system_template),
    ('user','{text}'),
])

parser=StrOutputParser()

##create chain
chain=prompt_template|model|parser

##App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple Api server using langchain runnable interfaces")

#Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost",port=8000)
