import streamlit as st
import requests 
import json
from analyzer.rules_engine import calculate_score

st.title("AI Code Review Assistant")

st.write("Paste your Python code below and analyze it.")

code = st.text_area("Enter Python Code")

uploaded_file = st.file_uploader("Upload Python File", type=["py"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    st.code(code, language="python")

if st.button("Analyze Code"):

    if code.strip() == "":
        st.warning("Please enter some code.")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/review",
            json={"code": code}
        )

        result = response.json()
        issues = result.get("analysis", [])
        score = calculate_score(issues)

    st.subheader("Analysis Result")

    if "analysis" in result:
        for issue in result["analysis"]:
            st.write("Issue:", issue["issue"])
            st.write("Suggestion:", issue["suggestion"])

    st.subheader("Code Metrics")

    metrics = result.get("metrics", {})

    st.write("Functions:", metrics.get("functions", 0))
    st.write("Loops:", metrics.get("loops", 0))
    st.write("Lines:", metrics.get("lines", 0))
    st.subheader("Code Complexity")

    complexity = result.get("complexity", 1)

    st.metric(
        label="Complexity Score",
        value=complexity
    )
    st.subheader("Code Quality Score")

    st.metric(
            label="Score",
            value=f"{score} / 100"
    )

if "result" in locals():
    st.download_button(
        label="Download Report",
        data=json.dumps(result, indent=4),
        file_name="code_review_report.json",
        mime="application/json"
    )




