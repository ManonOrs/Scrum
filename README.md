python -m venv venv

(console administrateur)
venv\Scripts\python -m pip install --upgrade pip setuptools

venv\Scripts\python -m pip install flit

venv\Scripts\python -m pip install -e ".[test]" 

venv\Scripts\pytest

venv\Scripts\pytest --cov