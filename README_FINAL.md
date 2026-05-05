# 📞 AI Customer Support Assistant  
### 🤖 LLM-Powered Ticketing System with RAG (In Progress)

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![LLM](https://img.shields.io/badge/LLM-LLaMA3-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎥 Demo

![Demo](assets/demo.gif)

---

## 📊 Architecture Diagram

![Architecture](assets/architecture.png)

---

## 🚀 Overview

The AI Customer Support Assistant is a production-style intelligent system designed to automate customer interactions using LLMs.

It includes:
- Intent detection  
- Ticket generation  
- Context-aware responses  
- (Upcoming) RAG integration  

---

## ✨ Features

- Intent Detection  
- Ticket System  
- Chat Memory  
- Modular Design  
- RAG (Planned)  

---

## 🧠 Architecture

```
User → Intent → Ticket/Response → LLM → Output → Storage
```

---

## 🧩 Tech Stack

- Python  
- LangChain  
- OpenRouter (LLaMA 3)  
- dotenv  
- FAISS (Planned)  

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/ai-support-assistant.git
cd ai-support-assistant

python -m venv venv
source venv/bin/activate
venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env`:
```
OPENAI_API_KEY=your_openrouter_api_key
```

---

## ▶️ Run

```bash
python app.py
```

---

## 🧪 Example

```
User: My order failed

Detected: Issue  
Ticket: ReportID-2026-05-05-000001  

AI: Please provide your Order ID.
```

---

## ⚠️ Limitations

- No DB  
- No RAG yet  
- Ticket reset issue  

---

## 🔥 Future (RAG)

```
Query → Retriever → Context → LLM → Answer
```

---

## 👨‍💻 Author

Darshan Shrestha
