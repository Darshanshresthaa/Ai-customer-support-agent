from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import PromptTemplate,ChatMessagePromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv

import os


# Retriving API keys form.env file

load_dotenv()

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_templet = ChatMessagePromptTemplate([
    ("system", """You are a highly trained customer support assistant. Provide clear, polite, and helpful responses."
    " Always prioritize user satisfaction and accurate information.
     Rules u SHould Follow
     - Be polite and structured
- If user reports issue → ask for Order ID
- Give step-by-step solutions
- If refund → explain process clearly
- Keep answers short and clear
- If unsure → ask follow-up questions"""),

    MessagesPlaceholder(variable_name='chat_history'),
    ("human","{query}")
])


def detect_problms(query):
    prompt =f""" Chassify The intent of Customer who connect on help for Normal questioning about ourshou or not  intensify in single word :
    Issue , Normal Questioning ,
    message : {query}"""
    try:
        response = llm.invoke(query)
        reason = (response.content).strip().upper()
        if reason == "ISSUE":
            return "Issue"
        
        else:
            return "Normal Questioning"
    
    except:
        print("Error on Detectiong Problem Method")
        return False


def generate_ticketID(reason):
    i = 1

    if reason == 'Issue':
        




