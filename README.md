# AI Code Review Assistant

A Python-based tool that analyzes Python code and detects common coding issues using static code analysis.

## Features

- Detect debug print statements
- Detect possible infinite loops
- Detect bare exception handling
- Security issue detection
- Code quality score
- Code complexity score
- Download analysis report
- Web interface using Streamlit

## Tech Stack

- Python
- FastAPI
- Streamlit
- AST (Abstract Syntax Tree)

## Project Structure

ai-code-review-assistant
│
├── analyzer       # Code analysis rules
├── api            # FastAPI backend
├── ui             # Streamlit frontend
└── README.md

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Start API

python -m uvicorn api.app:app --reload

3. Start UI

python -m streamlit run ui/app.py

## Author

Ashrith
