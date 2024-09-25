install:
	pip install --upgrade pip && pip install -r requirements.txt

format:	
	black *.py 

run:
	python main.py

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest -vv --cov=. test_main.py --disable-warnings

all: install format run test lint

