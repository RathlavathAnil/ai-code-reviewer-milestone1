# 🚀 AI Code Reviewer – (Infosys Springboard)

An AI-powered hybrid code analysis tool developed as part of the *Infosys Springboard Learning Program*.

This project combines **Python AST-based static analysis** with **LLM-powered intelligent suggestions** to help developers write cleaner, more optimized, and error-free Python code.

---

# 📌 Project Overview

The AI Code Reviewer is designed to:

- Parse and analyze Python code using Abstract Syntax Tree (AST)
- Detect syntax errors
- Identify logical issues (unused imports, unreachable code, undefined variables, infinite loops)
- Provide intelligent suggestions using Large Language Models (LLMs)
- Explain issues clearly for beginner-friendly understanding
- Analyze time and space complexity

The project is being built incrementally using milestone-based development.

---

# ⚙️ Features

## ✅ Milestone 1 – Static Code Analysis (AST Based)

- Safe parsing using Python's built-in `ast` module
- Syntax error detection
- Structured error reporting
- Modular visitor-based architecture

## ✅ Milestone 2 – AI-Powered Code Suggestions

- Integrated Groq LLM via LangChain
- Generates detailed explanations for:
  - Syntax errors
  - Undefined variables
  - Logical mistakes
- Suggests improvements with reasoning
- Provides time and space complexity analysis
- Beginner-friendly explanation style

---

# 🛠️ Tech Stack

- **Python**
- **AST (Abstract Syntax Tree)**
- **LangChain**
- **Groq LLM (LLaMA 3.1)**
- **python-dotenv**

---

# 📂 Project Structure
AI Code Reviewer/
│
├── code_parser.py # AST-based syntax parser
├── error_detector_visitor.py # Logical issue detection using AST
├── ai_suggester.py # LLM-powered suggestion engine
├── requirements.txt # Dependencies
├── README.md
└── .gitignore


---

# 🔒 Security

- API keys are stored securely in a `.env` file
- `.env` is excluded via `.gitignore`
- Virtual environments (`venv/`) are not committed
- No sensitive credentials are stored in the repository

---

# 📊 How It Works

1. User provides Python code.
2. AST module parses and checks for syntax errors.
3. Custom visitor detects logical issues.
4. LLM analyzes code contextually.
5. Tool returns structured + human-readable suggestions.

---
