import requests
from .utils import parse_github_repo


GITHUB_API_BASE = "https://api.github.com"


def fetch_issue_with_comments(repo_url: str, issue_number: int, token: str | None = None):
    owner, repo = parse_github_repo(repo_url)

    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    # -------- Fetch issue --------
    issue_url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}"
    issue_resp = requests.get(issue_url, headers=headers)

    if issue_resp.status_code != 200:
        raise RuntimeError(f"GitHub issue fetch failed: {issue_resp.text}")

    issue_data = issue_resp.json()

    title = issue_data.get("title", "")
    body = issue_data.get("body", "")
    comments_url = issue_data.get("comments_url")

    # -------- Fetch comments --------
    comments_text = ""

    if comments_url:
        comments_resp = requests.get(comments_url, headers=headers)
        if comments_resp.status_code == 200:
            comments = comments_resp.json()
            for idx, c in enumerate(comments, start=1):
                comments_text += f"\nComment {idx}: {c.get('body', '')}"

    # -------- Combine text --------
    full_text = f"""
TITLE:
{title}

BODY:
{body}

COMMENTS:
{comments_text if comments_text else "No comments"}
"""

    return full_text
