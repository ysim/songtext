readme: 
	pandoc --from=markdown-citations --to=rst --output=README.rst README.md

test:
	pytest tests/

test_verbose:
	python -m unittest discover
