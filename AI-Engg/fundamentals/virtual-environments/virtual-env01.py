# A virtual environment in Python is an isolated environment where you can install packages 
# for a specific project without affecting other Python projects.


# Why do we need virtual environments?
# Imagine you are working on two projects.
# - Project A: Requires langchain version 0.2.
# - Project B: Requires langchain version 0.3.




# Create a virtual environment
# python3 -m venv .venv


# python3 — runs Python.
# -m venv — runs Python's virtual environment module.
# .venv — the directory where the environment is created.


# step1:- python3 -m venv .venv
# step2:- source .venv/bin/activate
# step3:- python -m pip install requests
# step4:- deactivate







# Task	                                    Command
# Create environment	                    python3 -m venv .venv
# Activate on macOS/Linux	                source .venv/bin/activate
# Activate on Windows CMD	                .venv\Scripts\activate.bat
# Activate on Windows PowerShell	        .venv\Scripts\Activate.ps1
# Install a package	                        python -m pip install package_name
# List installed packages	                python -m pip list
# Check Python executable	                which python
# Check pip version	                        python -m pip --version
# Deactivate	                            deactivate




# genai-project/
# │
# ├── .venv/
# │   ├── bin/             # Python executables on macOS/Linux
# │   └── lib/             # Installed packages (typical layout)
# │
# ├── main.py
# ├── requirements.txt
# └── .gitignore




# You never push this files in github
# .venv/  ,   __pycache__/  ,  .env




# # What is requirements.txt?
# A virtual environment stores installed packages locally, 
# but another developer needs a way to reproduce your project's dependencies.

# Export your installed packages:
# python -m pip freeze > requirements.txt




# Install the dependencies in another environment:
# python -m pip install -r requirements.txt







# no test all the things

# python3 -m venv .venv
# source .venv/bin/activate
# python -m pip install openai fastapi uvicorn
# python -m pip freeze > requirements.txt