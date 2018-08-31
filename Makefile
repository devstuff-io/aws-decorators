install: scrub
	pip install --editable .

clean:
	find . -name '*.pyc' -exec rm '{}' ';'
	find . -name '__pycache__' -type d -prune -exec rm -rf '{}' '+'
	find . -name '.pytest_cache' -type d -prune -exec rm -rf '{}' '+'

scrub: clean
	find . -name '*.egg-info' -type d -prune -exec rm -rf '{}' '+'
	rm -rf artifact
	rm -rf build
	rm -rf dist
	rm -rf htmlcov
	rm -f .coverage

pypi-setup: clean
	pip install twine
	python setup.py sdist bdist_wheel

pypi-test-upload: pypi-setup
	# make sure TWINE_USERNAME and TWINE_PASSWORD are set
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi-upload: pypi-setup
	# make sure TWINE_USERNAME and TWINE_PASSWORD are set
	twine upload dist/*
