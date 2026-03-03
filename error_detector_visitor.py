import ast

code = """
import os
import sys
from datetime import datetime, timedelta
score = 100
print(score)
"""

class AIReviewer(ast.NodeVisitor):
    def __init__(self):
        self.defined = set()
        self.used = set()

    def visit_Import(self, node):
        for alias in node.names:
            self.defined.add(alias.asname or alias.name.split(".")[0])
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.defined.add(alias.asname or alias.name)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)
        self.generic_visit(node)

    def report_unused(self):
        builtins = set(dir(__builtins__))
        unused = self.defined - self.used
        unused = {name for name in unused if name not in builtins}

        print("--- AI REVIEW REPORT ---")
        for item in sorted(unused):
            print(f"⚠ UNUSED ITEM FOUND: {item}")

tree = ast.parse(code)
reviewer = AIReviewer()
reviewer.visit(tree)
reviewer.report_unused()
