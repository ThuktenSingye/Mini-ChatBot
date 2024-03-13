from PyPDF2 import PdfReader
from  langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from typing_extensions import Concatenate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate


import os

# Get api key
api_key = os.environ.get("OPENAI_API_KEY") 
llm = ChatOpenAI(openai_api_key = api_key, temperature=0, model='gpt-3.5-turbo')

# Provide path to pdf file
pdfReader = PdfReader("/home/thukten/Documents/TechS/AI/LangChain/Karma Wangchuk CV.pdf")

# Read text from pdf
raw_text = ''

for i, page in enumerate(pdfReader.pages): # loop through each pages 
    content = page.extract_text() # extract text
    if content:
        raw_text += content

# We need to split the text using character text split such that it should not increase token size
# Chunk size one sentence length chunk overlap: next sentence can have overlap of 200 than the previous
text_splitter = CharacterTextSplitter(separator='\n', chunk_size = 800, chunk_overlap = 200, length_function = len)
texts = text_splitter.split_text(raw_text);

# embedding 
embedding = OpenAIEmbeddings()

# Get the vector stores
document_search = FAISS.from_texts(texts, embedding)

# Chain type stuff: whenever you try to ask the question you get answer
chain = load_qa_chain(llm=llm, chain_type="stuff")

chat_end  = False
while not chat_end:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        chat_end = True
    else:
        docs = document_search.similarity_search(user_input)
        response = chain.invoke({"question": HumanMessage(content=user_input), "input_documents": docs})
        # response = chain.invoke({"input": user_input})
        print("AI: ", response['output_text'])
