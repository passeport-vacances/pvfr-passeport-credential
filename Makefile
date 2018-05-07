all: lint test dist doc

lint:
	find pvfr -name "*.py" | xargs pycodestyle --ignore=E501,E402,E701

test:
	tox

dist:
	python ./setup.py bdist_wheel

doc:
	cd docs && $(MAKE) html

clean:
	python ./setup.py clean


upload:
	twine upload dist/*

.PHONY: all lint test doc dist upload
