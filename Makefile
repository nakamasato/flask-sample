init:
	pip install -r requirements.txt -r tests/requirements.txt

test:
	python -m pytest

.PHONY: init test
