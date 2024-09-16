install:
	pip install --upgrade pip && pip install -r requirements.txt

run:
	python3 main.py

lint:
	pylint --disable=R,C main.py

test:
	python3 test_main.py 

cp C:/Users/ss1516/Downloads/Bob_PythonTemplate1-main/Bob_PythonTemplate1-main/.devcontainer .

all: install run test lint

