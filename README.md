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

     ┌──────────────────────────┐

        │        User Input        │

        │ "My order not arrived"  │

        └────────────┬─────────────┘

                     │

                     ▼

        ┌──────────────────────────┐

        │   Intent Detection (LLM) │

        │  ISSUE / NORMAL / CLOSE  │

        └────────────┬─────────────┘

                     │

        ┌────────────┼──────────────┐

        │            │              │

        ▼            ▼              ▼

 ┌────────────┐ ┌────────────┐ ┌──────────────┐

 │   ISSUE    │ │   NORMAL   │ │ CLOSE-TICKET │

 └────┬───────┘ └────┬───────┘ └────┬─────────┘

      │              │              │

      ▼              ▼              ▼

┌──────────────┐  ┌──────────────┐  ┌────────────────┐

│ Generate     │  │ Send Query   │  │ Update Ticket  │

│ Ticket ID    │  │ to LLM       │  │ Status (Future)│

└────┬─────────┘  └────┬─────────┘  └────────────────┘

      │                 │

      ▼                 ▼

┌──────────────┐  ┌──────────────┐

│ Save Ticket  │  │ Generate AI  │

│ + Chat Log   │  │ Response     │

└────┬─────────┘  └────┬─────────┘

      │                 │

      └──────┬──────────┘

             ▼

    ┌──────────────────────┐

    │  Show Response to    │

    │        User          │

    └──────────────────────┘
