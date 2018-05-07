all: lint test doc

lint:
	find pvfr -name "*.py" | xargs pycodestyle --ignore=E501,E402,E701

test:
	tox

doc:
	cd docs && $(MAKE) html

upload:
	twine upload dist/*

.PHONY: all lint test doc upload
