import requests
import json
import re
from tenacity import retry, stop_after_attempt, wait_fixed


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def build_prompt(issue_text: str) -> str:
    return f"""
You are an AI assistant that analyzes GitHub issues.

Return ONLY a valid JSON object in this exact format:

{{
  "summary": "One-sentence summary of the user's problem or request.",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "1 to 5 with short justification",
  "suggested_labels": ["label1", "label2", "label3"],
  "potential_impact": "Brief impact on users if this is a bug"
}}

Rules:
- Output ONLY JSON
- No explanation text
- No markdown

GitHub Issue:
----------------
{issue_text}
----------------
"""


def extract_json(text: str) -> dict:
    # remove leading text before first {
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found in LLM output")

    json_text = text[start:end + 1]
    return json.loads(json_text)


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def analyze_issue_with_llm(issue_text: str) -> dict:
    prompt = build_prompt(issue_text)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=180)

    if resp.status_code != 200:
        raise RuntimeError("Ollama API call failed")

    data = resp.json()

    output_text = data.get("response", "")
    print("\n====== RAW LLM OUTPUT ======\n", output_text, "\n============================\n")

    return extract_json(output_text)
