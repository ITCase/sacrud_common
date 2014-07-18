all: test

test:
	nosetests --with-coverage --cover-package sacrud_common --cover-erase --with-doctest
