from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import PromptTemplate,ChatMessagePromptTemplate,MessagesPlaceholder,ChatPromptTemplate
from dotenv import load_dotenv

from datetime import datetime,timedelta

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
ISSUE or NORMAL or CLOSE-TICKET

Message: {query}
"""
    try:
        response = llm.invoke(prompt)
        reason = response.content.strip().upper()

        if "ISSUE" in reason:
            return "Issue"
        
        elif "CLOSE-TICKET" in reason:
            return "Close Ticket"
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
    parts = ticket_id.split("-")

    created_date = "-".join(parts[1:4])  #extracted created date from Report id 
    updated_date = created_date    

    with open(file_name,"w") as f:
        f.write(f"Ticket ID: {ticket_id}\n")
        f.write(f"Status: {Ticket_status}\n")
        f.write(f"Created Date: {created_date}\n")
        f.write(f"Updated Date: {created_date}\n")

        f.write("Note: This ticket will automatically close after 30 days of inactivity.\n\n")

        for message in chat_history:
            role = message[0]
            content = message[1]
            f.write(f"{role.upper()} : {content}\n")


def close_ticket(ticket_id):
    file_name =f"{ticket_id}.txt"
    new_line =[]
    if not os.path.exists(file_name):
        return None
    


    update_status = False
    
    with open(file_name,"r") as f:
        lines = f.readlines()
        for line in lines:
            
            if "Updated Data" in line:
                updated_date = line.split("-")

                current_date = datetime.now().strftime("%Y-%m-%d")
                present_date = current_date.split("-")[1] - updated_date[1]

                if present_date >=30:
                    new_line.append(line)





def open_existing_ticket(ticket_id):
    file_name = f"{ticket_id}.txt"
    if not os.path.exists(file_name):
        return None
    
    updated_date_bool = False
    updated_date = datetime.now().strftime("%Y-%m-%d")
    new_lines = []

    
    with open(file_name,"r") as f:
        lines = f.readlines()
    for line in lines:
        if "Updated Date" in line:
            new_lines.append(f"Updated Date : {updated_date}")
        else:
            new_lines.append(line)
    
    if not updated_date_bool:
         new_lines.append(f" Updated Date : {updated_date}")

    with open(file_name,"w") as f:
        f.writeline(new_lines)
        f.close()





chat_history = []

today = datetime.now()

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