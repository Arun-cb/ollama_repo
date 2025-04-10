from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


# user_input = input("Please enter your queries here...\n")

# print(f"query: {user_input}")

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

llm = Ollama(base_url='http://localhost:11434', model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# if user_input:
#     print(chain.invoke({"query": user_input}))
    
# Below code to ask question with continuously before doing exit conditions
exit_conditions = (":q", "quit", "exit")
user_inputs = []
user_inputs_with_count = {}
while True:
    query = input("> ")
    if query in exit_conditions:
        print("Chat Ended")
        break
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
        print(chain.invoke({"query": query}))