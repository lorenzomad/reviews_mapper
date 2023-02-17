setup:
	python -m venv venv
	source ./venv/bin/activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	python -m nltk.downloader popular

test:
	pytest

lint:
	pylint