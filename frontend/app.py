import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="GitHub Issue AI Assistant", layout="centered")

st.title("🤖 GitHub Issue AI Assistant")
st.write("Analyze GitHub issues using AI and get structured insights.")

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/facebook/react"
)

issue_number = st.number_input(
    "Issue Number",
    min_value=1,
    step=1
)

analyze_btn = st.button("Analyze Issue 🚀")

if analyze_btn:
    if not repo_url or not issue_number:
        st.error("Please enter both repository URL and issue number.")
    else:
        with st.spinner("Analyzing issue with AI..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={
                        "repo_url": repo_url,
                        "issue_number": int(issue_number)
                    },
                    timeout=180
                )

                if response.status_code != 200:
                    st.error(f"Backend error: {response.text}")
                else:
                    data = response.json()

                    st.success("Analysis Complete ✅")

                    st.subheader("📝 Summary")
                    st.write(data.get("summary", ""))

                    st.subheader("🏷️ Type")
                    st.write(data.get("type", ""))

                    st.subheader("🔥 Priority")
                    st.write(data.get("priority_score", ""))

                    st.subheader("🏷️ Suggested Labels")
                    labels = data.get("suggested_labels", [])
                    if labels:
                        st.write(", ".join(labels))
                    else:
                        st.write("None")

                    st.subheader("⚠️ Potential Impact")
                    st.write(data.get("potential_impact", ""))

                    with st.expander("🔍 Raw JSON"):
                        st.json(data)

            except Exception as e:
                st.error(f"Request failed: {str(e)}")
