import ast

class CodeParser:
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)

    def get_loops(self):
        loops = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.For):
                loops.append(node)
        return loops
