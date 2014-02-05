readme: 
	pandoc --from=markdown-citations --to=rst --output=README.rst README.md

test:
	python -m unittest discover --buffer

test_verbose:
	python -m unittest discover
