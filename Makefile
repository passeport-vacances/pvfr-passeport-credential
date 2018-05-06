lint:
	find pvfr -name "*.py" | xargs pycodestyle --ignore=E501,E402,E701

test:
	tox

upload:
	twine upload dist/*

.PHONY: help lint test upload
