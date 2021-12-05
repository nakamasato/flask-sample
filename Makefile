init:
	pip install -r sample/requirements.txt -r tests/requirements.txt

test:
	pytest --cov=./ --cov-report=xml

.PHONY: init test
