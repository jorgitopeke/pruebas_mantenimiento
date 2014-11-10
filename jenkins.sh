#! /bin/sh

pip install -r requirements.txt
autopep8 -ir *.py
flake8 --max-complexity=3 --exclude=*.txt,*.md --max-line-length=200 *.py
python TestFiguras.py -v
coverage run --branch TestFiguras.py
coverage report -m
coverage html
