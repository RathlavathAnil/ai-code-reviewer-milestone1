from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

code_string = """
def calculate_sum(a, b):
    result = a + b
    if result > 10:
        print("Greater than 10")
    else:
        print("Less than or equal to 10")
    return result
"""

prompt = PromptTemplate(
    input_variables=["code_string"],
    template="""
You are an experienced coding teacher and static code analyzer.

Analyze the following Python code and:
1. Identify syntax errors.
2. Detect undefined variables.
3. Detect logical issues (unused imports, unreachable code, infinite loops).
4. Explain why each issue is problematic.
5. Suggest corrected code.
6. Analyze time and space complexity.

Code:
{code_string}
"""
)

def get_ai_suggestion(code_string):
    try:
        formatted_prompt = prompt.format(code_string=code_string)
        result = model.invoke(formatted_prompt)
        print(result.content if hasattr(result, "content") else result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    get_ai_suggestion(code_string)