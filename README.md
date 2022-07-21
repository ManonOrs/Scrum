python -m venv venv

python -m pip install --upgrade pip   

venv\Scripts\pip install -e ".[test]" 

venv\Scripts\pytest

venv\Scripts/pytest --cov