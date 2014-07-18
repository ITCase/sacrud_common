from sacrud_common import __version__
from setuptools import setup


setup(
    name='sacrud_common',
    version=__version__,
    url='http://github.com/ITCase/sacrud_common/',
    author='Svintsov Dmitry',
    author_email='root@uralbash.ru',

    packages=['sacrud_common'],
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    license="BSD",
    description='Experemental Bells and Whistles for sacrud based project',
    long_description=open('README.md').read(),
    install_requires=[
        "sqlalchemy",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid ",
        "Framework :: Flask",
        "Topic :: Internet",
        "Topic :: Database",
        "License :: Repoze Public License",
    ],
)
