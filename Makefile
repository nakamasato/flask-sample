init:
	pip install -r sample/requirements.txt -r tests/requirements.txt

test:
	pytest

.PHONY: init test
