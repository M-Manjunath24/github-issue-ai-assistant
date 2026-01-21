# AI-Powered GitHub Issue Assistant

An AI-powered web application that analyzes GitHub issues and provides structured insights such as summaries, issue type, priority, suggested labels, and potential impact.

This project fetches issue data from GitHub, processes it using a locally hosted Phi-3 language model via Ollama, and serves results through a FastAPI backend with a Streamlit frontend.

---

## Features

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

## Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Model | Phi-3 (Ollama) |
| APIs | GitHub REST API |
| Language | Python 3.12 |
| OS | Windows / Linux |

---

## Project Structure

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
```

## Quick Start
Prerequisites
 - Python 3.12+
 - Git
 - Ollama

## Installation & Setup
1️.Clone the Repository

```text
git clone https://github.com/M-Manjunath24/github-issue-ai-assistant.git
cd github-issue-ai-assistant
```

2️.Create Virtual Environment
 - python -m venv venv
 - venv\Scripts\activate

3️.Install Dependencies
 - pip install -r requirements.txt

4️.Install Ollama & Phi-3 Model
 - Download Ollama:
 - https://ollama.com/download

 - Pull Phi-3:
   ```text
    ollama pull phi3
   ```
5️.Start Backend (FastAPI)
  ```text
   python -m uvicorn backend.main:app --reload
  ```

 - Backend runs at:
 - ```
    http://127.0.0.1:8000
   ```
 - API Docs:
 ```text
   http://127.0.0.1:8000/docs
 ```
6️.Start Frontend (Streamlit)

 - Open a new terminal:
 ```
   venv\Scripts\activate
   streamlit run frontend/app.py
 ```
 - Frontend runs at:
 ```
   http://localhost:8501
 ```
## Architecture Overview
 - Frontend
    - Streamlit UI
 - Backend
    - FastAPI REST API
    - GitHub API Integration
    - Ollama (Phi-3) LLM

## Data Flow
```text
 User (Streamlit)
       ↓
 FastAPI Backend
       ↓
 GitHub REST API → Fetch issue data
       ↓
 Ollama Phi-3 → AI analysis
       ↓
 Structured JSON
       ↓
 Displayed in UI
```

## API Usage
 - Analyze Issue

    - POST /analyze
```text
{
  "repo_url": "https://github.com/facebook/react",
  "issue_number": 1
}
```
  - Response Example
```text 
 {
  "summary": "Tests should run in isolated iframes.",
  "type": "feature_request",
  "priority_score": "3 - Medium impact",
  "suggested_labels": ["testing", "isolation"],
  "potential_impact": "Improves test reliability."
 }

```
##  Project Demo Video link
 - Youtube video link
    - https://youtu.be/XSGPw2NE7xQ

## Notes

- Only public GitHub repositories are supported
- Phi-3 is used for better GPU compatibility (4GB VRAM)
- No API keys required
- GitHub API rate limits apply
- Structured JSON output for automation

## Future Improvements
 - Add caching
 - Add “Copy JSON” button
 - GitHub authentication
 - Auto-label GitHub issues
 - Batch issue analysis

## Author
M. Manjunath




