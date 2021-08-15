init:
	pip install -r sample/requirements.txt -r tests/requirements.txt

test:
	python -m pytest

.PHONY: init test
