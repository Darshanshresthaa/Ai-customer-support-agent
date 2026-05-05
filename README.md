🧠 AI Customer Support Assistant (LLM + Ticketing System)

An intelligent AI-powered customer support assistant that can understand user queries, detect issues, generate ticket IDs, and manage basic ticket workflows using LLMs.

🚀 Overview

This project simulates a real-world customer support system powered by an LLM. It can:

💬 Handle user queries conversationally
🧠 Detect whether a message is an issue or normal query
🎫 Automatically generate support tickets
📝 Store chat history with ticket details
🔄 Update and manage ticket status

The system is designed to be simple, modular, and extendable (with future RAG integration).

⚙️ Features

✅ Intent detection (Issue / Normal / Close Ticket)
✅ Automatic ticket generation with unique ID
✅ Chat history tracking
✅ File-based ticket storage
✅ LLM-powered structured responses
✅ Modular design for scalability

🧠 How It Works
User inputs a message
LLM classifies intent:
ISSUE → Create ticket
NORMAL → Respond normally
CLOSE-TICKET → (future handling)
If issue:
Generate Ticket ID
Save conversation to file
LLM generates a polite, structured response
Chat history is maintained
🧩 Tech Stack
LangChain – Prompt + LLM orchestration
OpenRouter (LLaMA 3) – Language model
Python – Core logic
dotenv – API key management
📦 Installation
1. Clone Repository
git clone https://github.com/your-username/ai-customer-support.git
cd ai-customer-support
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Setup Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openrouter_api_key
▶️ Run the Application
python main.py
💬 Example Usage
User: My order hasn’t arrived yet
Detected Problem: Issue
Ticket ID: ReportID-2026-05-05-000001

AI: I'm sorry for the inconvenience. Could you please provide your Order ID so I can assist you further?
📁 Ticket Format

Each issue creates a .txt file:

Ticket ID: ReportID-2026-05-05-000001
Status: open
Created Date: 2026-05-05
Updated Date: 2026-05-05

HUMAN: My order hasn’t arrived
AI: Please provide your Order ID
⚠️ Current Limitations

❌ Ticket ID counter resets (not persistent)
❌ Close ticket logic incomplete
❌ No database (file-based storage only)
❌ No UI (CLI-based system)

🧠 Future Improvements (RAG Integration 🚀)

Planned upgrade: Retrieval-Augmented Generation (RAG)

🔄 Why RAG?

Currently:

LLM answers generally
No access to company-specific data

With RAG:

Answers from knowledge base (FAQs, policies, docs)
More accurate, context-aware responses
🧩 Planned RAG Pipeline
User Query
    ↓
Embed Query
    ↓
Search Vector DB (FAISS)
    ↓
Retrieve Relevant Docs
    ↓
Send Context + Query → LLM
    ↓
Accurate Answer
🔧 Tools for RAG
FAISS – Vector database
HuggingFace Embeddings (MiniLM)
LangChain Retriever
Document loaders (PDF, CSV, Web)
📌 Example Use Case After RAG

User:

What is your refund policy?

Before RAG:
❌ Generic answer

After RAG:
✅ Exact answer from company policy

📌 Key Functions Explained
🔹 detect_problms(query)

Classifies user intent using LLM.

🔹 generate_ticketID(reason)

Generates unique ticket ID for issues.

🔹 save_ticket(...)

Stores ticket data and chat history.

🔹 open_existing_ticket(ticket_id)

Updates ticket activity.

💡 Prompt Design
You are a customer support assistant.

- Be polite
- Ask Order ID if issue
- Give step-by-step solutions
- Keep answers short
👨‍💻 Author

Darshan Shrestha
AI/ML Enthusiast | Building Real-World LLM Systems

⭐ Final Thoughts

This project demonstrates:

Practical LLM integration
Prompt engineering
Real-world system design
Foundation for scalable AI support systems

👉 Next step: Turn this into a production-ready RAG system with UI + database
