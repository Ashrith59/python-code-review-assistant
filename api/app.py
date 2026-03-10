from fastapi import FastAPI
from pydantic import BaseModel
import ast
from analyzer.rules_engine import RulesEngine 
from analyzer.rules_engine import check_security

app = FastAPI()

# Initialize rules engine
rules_engine = RulesEngine()

# Input schema
class CodeInput(BaseModel):
    code: str


# Home route
@app.get("/")
def home():
    return {"message": "AI Code Review Assistant Running"}


# Code review API
@app.post("/review")
def review_code(data: CodeInput):

    try:
        # Convert code to AST
        tree = ast.parse(data.code)

        # Run analysis
        issues = rules_engine.analyze(tree)
        security_issues = check_security(data.code)
        issues.extend(security_issues)

        return {"analysis": issues}

    except Exception as e:
        return {"error": str(e)}
