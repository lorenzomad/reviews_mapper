setup:
	pip -m venv venv
	soure ./venv/bin/activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	python -m nltk.downloader popular

test:
	pytest

lint:
	pylint