from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import PromptTemplate,ChatMessagePromptTemplate,MessagesPlaceholder,ChatPromptTemplate
from dotenv import load_dotenv

from datetime import datetime

import os


# Retriving API keys form.env file

load_dotenv()

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_templet = ChatPromptTemplate.from_messages([
    ("system", """You are a highly trained customer support assistant.
Provide clear, polite, and helpful responses.
Always prioritize user satisfaction and accurate information.

Rules you should follow:
- Be polite and structured
- If user reports issue → ask for Order ID
- Give step-by-step solutions
- If refund → explain process clearly
- Keep answers short and clear
- If unsure → ask follow-up questions
"""),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human","{query}")
])


def detect_problms(query):
    prompt = f"""
Classify the intent into ONLY ONE WORD:
ISSUE or NORMAL

Message: {query}
"""
    try:
        response = llm.invoke(prompt)
        reason = response.content.strip().upper()

        if "ISSUE" in reason:
            return "Issue"
        else:
            return "Normal Questioning"

    except Exception as e:
        print("Error:", e)
        return False

def generate_ticketID(reason):
    if reason == 'Issue':
        today = datetime.now()
        formatted_date = today.strftime("%Y-%m-%d")
        i = 1
        ticket_id = f"ReportID-{formatted_date}-{i:06d}"
        i +=1

        return ticket_id

    else:
        return False


def save_ticket(ticket_id,chat_history,Ticket_status):
    file_name = f"{ticket_id}.txt"

    with open(file_name,"w") as f:
        f.write(f"Trcket ID : {ticket_id}")
        f.write(f" Ticket Status : {Ticket_status}")

        for message in chat_history:
            role = message[0]
            content = message[1]
            f.write(f"{role.upper()} : {content}\n")




chat_history = []

while True:
    user_input = input("User : ")

    if user_input.lower() =='exit':
        break

    reason = detect_problms(user_input)

    print("Detected Problem : ",reason)

    ticket_id = generate_ticketID(reason)

    print("Ticket_id : ",ticket_id)


    message = chat_templet.format_messages(chat_history = chat_history,
                                           query = user_input)
    

    response = llm.invoke(message)

    ai_response = response.content

    print("Ai : ",ai_response)

    chat_history.append(('human',user_input))
    chat_history.append(("ai",ai_response))

    if ticket_id:
        save_ticket(ticket_id=ticket_id,chat_history=chat_history,Ticket_status="open")












