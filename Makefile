install:
	pip install --upgrade pip && pip install -r requirements.txt

format:	
	black *.py 

lint:
	ruff check *.py lib/*.py 

test:
	python -m pytest -vv --nbval-lax -cov=lib -cov=main test_main.py *.ipynb --disable-warnings  

all: install format test lint

generate_and_push:
	python main.py  

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git add .; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi


