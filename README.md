python -m venv venv

(console administrateur)
python -m pip install --upgrade pip setuptools

python -m pip install flit

venv\Scripts\pip install -e ".[test]" 

venv\Scripts\pytest

venv\Scripts/pytest --cov