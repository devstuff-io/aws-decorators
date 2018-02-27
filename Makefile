setup:
	pip install --editable .

clean:
	find . -name '*.pyc' -exec rm '{}' ';' && rm -rf *.egg-info build/ dist/

pypi-setup: clean
	pip install twine
	python setup.py sdist bdist_wheel

pypi-test-upload: pypi-setup
	# make sure TWINE_USERNAME and TWINE_PASSWORD are set
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi-upload: pypi-setup
	# make sure TWINE_USERNAME and TWINE_PASSWORD are set
	twine upload dist/*
