from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import IssueRequest, IssueAnalysis
from .github_api import fetch_issue_with_comments
from .llm_client import analyze_issue_with_llm


app = FastAPI(title="GitHub Issue AI Assistant")

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze", response_model=IssueAnalysis)
def analyze_issue(request: IssueRequest):

    try:
        issue_text = fetch_issue_with_comments(
            request.repo_url,
            request.issue_number
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        analysis = analyze_issue_with_llm(issue_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM analysis failed: {str(e)}")

    return analysis


@app.get("/")
def health():
    return {"status": "ok"}
