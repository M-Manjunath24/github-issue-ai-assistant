# AI-Powered GitHub Issue Assistant

An AI-powered web application that analyzes GitHub issues and provides structured insights such as summaries, issue type, priority, suggested labels, and potential impact.

This project fetches issue data from GitHub, processes it using a locally hosted Phi-3 language model via Ollama, and serves results through a FastAPI backend with a Streamlit frontend.

---

## ✨ Features

- Fetches GitHub issue title, description, and comments  
- AI-based analysis using Phi-3 (via Ollama)  
- Structured JSON output:
  - Summary  
  - Issue type  
  - Priority score  
  - Suggested labels  
  - Potential impact  
- Clean and simple Streamlit UI  
- FastAPI backend with REST API  
- Works fully on local machine (no paid APIs required)  

---

## 🧱 Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Model | Phi-3 (Ollama) |
| APIs | GitHub REST API |
| Language | Python 3.12 |
| OS | Windows / Linux |

---

## 📁 Project Structure

```text
github-issue-ai-assistant/
│
├── backend/
│   ├── main.py
│   ├── github_api.py
│   ├── llm_client.py
│   ├── models.py
│   └── utils.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
