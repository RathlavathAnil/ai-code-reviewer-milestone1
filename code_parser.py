import ast

def parse_code(code_string):
    """
    Parse Python code and check for syntax errors.
    """

    try:
        tree = ast.parse(code_string)
        return {
            "success": True,
            "ast": ast.dump(tree, indent=2)
        }

    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "message": f"Syntax Error: {str(e)}",
                "line": e.lineno,
                "offset": e.offset
            }
        }


# Test
code = """
def calculate_sum(a, b):
    result = a + b
    return result
"""

result = parse_code(code)
print(result)
