all: rst lint test dist doc

rst:
	pandoc -t rst README.md  > README.rst

lint:
	pylint pvfr
	find pvfr -name "*.py" | xargs pycodestyle

test: rst
	tox

dist: rst
	python ./setup.py bdist_wheel

doc: rst
	$(MAKE) -C docs html

clean:
	python ./setup.py clean
	$(MAKE) -C docs clean

upload:
	twine upload dist/*

.PHONY: all rst lint test doc dist upload
