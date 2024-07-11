# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:36:01 2024

@author: Akhil Raghupatruni
"""
import os
from langchain_openai import ChatOpenAI
import streamlist as st


# os.environ['OPENAI_API_KEY'] = "sk-proj-I5cxQZwmgn2SaC5ml2KyT3BlbkFJGJJwp6iTgztbopugiti7"
# os.environ['GOOGLE_API_KEY']  = "AIzaSyAIh1kTbIpJMsInYh9SeMEIqTa3hsA2Nus"

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")
response = gpt3_model.invoke("Explain transformers architecture.")
print(response.content)

gpt4o_model = ChatOpenAI(model_name = "gpt-4o")
response = gpt4o_model.invoke("Explain transformers architecture.")
print(response.content)

from langchain_google_genai import ChatGoogleGenerativeAI

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")
response = gemini_model.invoke("Give me 3 tweets on World War 1")