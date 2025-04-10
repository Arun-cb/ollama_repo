from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
print("1. Streamlit app Called")

prompt = ChatPromptTemplate.from_messages(
    [("system", "you're a helpful AI Assistant. Your name is Citta's AI"),
     ("user", "user query:{query}"),
     ("system", "please provide minimal greeting message to the user response"),
     ("user", "user query:{query}"),
     ("system", "don't provide greeting for every message starting"),
     ("user", "user query:{query}"),
     ("system", "don't provide any AI related question raised by the user. if you getting them please respone i're not train those type of questions"),
     ("user", "user query:{query}")
    ])

st.title("AI Chatbot")
user_input = st.text_input("Ask any doubts")

llm = Ollama(base_url='http://localhost:11434', model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser    

print("2. Streamlit app running")

exit_conditions = (":q", "quit", "exit")
user_inputs = []
user_inputs_with_count = {}

# query = input("> ")
query = user_input
print("3. Streamlit Input Triggered", query)
if query:
    print("Input Query comes under the if condition", query)
    if query in exit_conditions:
        print("Chat Ended")
    else:
        user_inputs.append(query)
        if not user_inputs_with_count:
            user_inputs_with_count[query] = 1
        else:
            if query in user_inputs_with_count:
                user_inputs_with_count[query] = user_inputs_with_count[query] + 1
                # count num.of same question raised by user and intimate to them
                if user_inputs_with_count[query] >= 3:
                    print("NOTE: You have raise the same before....")
            else:
                user_inputs_with_count[query] = 1
        print("4. Streamlit process comes end of the condition")
        # print(chain.invoke({"query": query}))
        res = chain.invoke({"query": query})
        st.write(res)
        print("5. Streamlit final response", res)