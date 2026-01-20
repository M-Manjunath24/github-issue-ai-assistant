from pydantic import BaseModel, Field
from typing import List


class IssueRequest(BaseModel):
    repo_url: str = Field(..., example="https://github.com/facebook/react")
    issue_number: int = Field(..., example=123)


class IssueAnalysis(BaseModel):
    summary: str
    type: str
    priority_score: str
    suggested_labels: List[str]
    potential_impact: str
