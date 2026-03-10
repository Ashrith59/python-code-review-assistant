import ast


class RulesEngine:

    def analyze(self, tree):

        issues = []

        issues.extend(self.check_range_len_loop(tree))
        issues.extend(self.check_print_statements(tree))
        issues.extend(self.check_nested_loops(tree))

        return issues


    # Rule 1
    def check_range_len_loop(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.For):

                if isinstance(node.iter, ast.Call):

                    if isinstance(node.iter.func, ast.Name):

                        if node.iter.func.id == "range":

                            args = node.iter.args

                            if len(args) == 1 and isinstance(args[0], ast.Call):

                                inner = args[0]

                                if isinstance(inner.func, ast.Name) and inner.func.id == "len":

                                    issues.append({
                                        "issue": "Inefficient loop using range(len())",
                                        "suggestion": "Use direct iteration like: for item in arr"
                                    })

        return issues


    # Rule 2
    def check_print_statements(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name) and node.func.id == "print":

                    issues.append({
                        "issue": "Debug print statement found",
                        "suggestion": "Remove print statements before production"
                    })

        return issues


    # Rule 3
    def check_nested_loops(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.For):

                for child in ast.walk(node):

                    if isinstance(child, ast.For) and child != node:

                        issues.append({
                            "issue": "Nested loop detected",
                            "suggestion": "Nested loops may cause performance issues"
                        })

        return issues


def calculate_score(issues):
    score = 100 - (len(issues) * 10)

    if score < 0:
        score = 0

    return score 

def check_security(code):
    warnings = []

    if "eval(" in code:
        warnings.append({
            "issue": "Security risk: eval() detected",
            "suggestion": "Avoid using eval() as it can execute arbitrary code."
        })

    if "exec(" in code:
        warnings.append({
            "issue": "Security risk: exec() detected",
            "suggestion": "Avoid using exec() in production code."
        })

    if "os.system(" in code:
        warnings.append({
            "issue": "Security risk: os.system() detected",
            "suggestion": "Use subprocess module instead of os.system()."
        })

    if "pickle.loads(" in code:
        warnings.append({
            "issue": "Security risk: pickle.loads() detected",
            "suggestion": "Avoid untrusted pickle data."
        })

    if "while True" in code:
        warnings.append({
        "issue": "Possible infinite loop detected",
        "suggestion": "Ensure the loop has a break condition."
    })

    if "except:" in code:
        warnings.append({
        "issue": "Bare except detected",
        "suggestion": "Use specific exception types instead of bare except."
    })

    if "import *" in code:
        warnings.append({
        "issue": "Wildcard import detected",
        "suggestion": "Avoid 'import *' because it pollutes the namespace."
    })
    return warnings 

    def get_code_metrics(code):
        import ast

        tree = ast.parse(code)

        functions = 0
        loops = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions += 1
            if isinstance(node, (ast.For, ast.While)):
                loops += 1

        lines = len(code.split("\n"))

        return {
            "functions": functions,
            "loops": loops,
            "lines": lines
        }

    def calculate_complexity(code):
        complexity = 1

        complexity += code.count("if ")
        complexity += code.count("for ")
        complexity += code.count("while ")
        complexity += code.count("and ")
        complexity += code.count("or ")

        return complexity